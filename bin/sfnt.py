"""Minimal sfnt reader: enough to list the Unicode codepoints a font maps.

fontTools is not available on a stock macOS or Alpine runner, and pulling it in
for a presence check is more dependency than the check is worth.
"""

import struct

SFNT_VERSIONS = (b"\x00\x01\x00\x00", b"OTTO", b"true", b"typ1")


class FontError(Exception):
    pass


def codepoints(path):
    """Return the set of Unicode codepoints that map to a real glyph."""
    with open(path, "rb") as font:
        data = font.read()
    return _cmap_codepoints(data, _table_offset(data, b"cmap"))


def _table_offset(data, tag):
    if len(data) < 12:
        raise FontError("file is too short to be a font")
    version = data[:4]
    if version == b"ttcf":
        raise FontError("font collections (.ttc) are not supported")
    if version not in SFNT_VERSIONS:
        raise FontError("unrecognized sfnt version {!r}".format(version))

    (count,) = struct.unpack_from(">H", data, 4)
    for index in range(count):
        entry, _, offset, _ = struct.unpack_from(">4sLLL", data, 12 + 16 * index)
        if entry == tag:
            return offset
    raise FontError("font has no {} table".format(tag.decode()))


def _cmap_codepoints(data, cmap):
    (count,) = struct.unpack_from(">H", data, cmap + 2)
    found = set()
    read = 0

    for index in range(count):
        platform, encoding, offset = struct.unpack_from(">HHL", data, cmap + 4 + 8 * index)
        if not _is_unicode(platform, encoding):
            continue

        subtable = cmap + offset
        (fmt,) = struct.unpack_from(">H", data, subtable)
        if fmt == 4:
            found |= _segment_mapping(data, subtable)
        elif fmt == 12:
            found |= _segmented_coverage(data, subtable)
        else:
            continue
        read += 1

    if not read:
        raise FontError("font has no readable Unicode cmap subtable")
    return found


def _is_unicode(platform, encoding):
    return platform == 0 or (platform == 3 and encoding in (1, 10))


def _segment_mapping(data, subtable):
    """cmap format 4, the BMP-only segment mapping every font carries."""
    (double_segments,) = struct.unpack_from(">H", data, subtable + 6)
    segments = double_segments // 2

    ends = struct.unpack_from(">{}H".format(segments), data, subtable + 14)
    starts_at = subtable + 16 + double_segments
    starts = struct.unpack_from(">{}H".format(segments), data, starts_at)
    deltas = struct.unpack_from(">{}h".format(segments), data, starts_at + double_segments)
    ranges_at = starts_at + 2 * double_segments
    ranges = struct.unpack_from(">{}H".format(segments), data, ranges_at)

    found = set()
    for index in range(segments):
        for codepoint in range(starts[index], min(ends[index], 0xFFFE) + 1):
            if ranges[index] == 0:
                glyph = (codepoint + deltas[index]) & 0xFFFF
            else:
                at = ranges_at + 2 * index + ranges[index] + 2 * (codepoint - starts[index])
                (glyph,) = struct.unpack_from(">H", data, at)
                if glyph:
                    glyph = (glyph + deltas[index]) & 0xFFFF
            if glyph:
                found.add(codepoint)
    return found


def _segmented_coverage(data, subtable):
    """cmap format 12, which is where anything above the BMP lives."""
    (groups,) = struct.unpack_from(">L", data, subtable + 12)

    found = set()
    for index in range(groups):
        start, end, glyph = struct.unpack_from(">LLL", data, subtable + 16 + 12 * index)
        found.update(range(start + 1 if glyph == 0 else start, end + 1))
    return found
