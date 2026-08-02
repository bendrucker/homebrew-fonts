# Monaspice Nerd Font, Built From Tip

Monaspace Neon, patched weekly from [nerd-fonts][] `master` so the Codicon brand
marks land before the next Nerd Fonts release does.

Nerd Fonts has not cut a release since [v3.4.0][] (2025-04-24). `cod-cursor`
(`U+EC5C`), `cod-openai` (`U+EC81`), and `cod-claude` (`U+EC82`) were added to
`master` after it, so no 3.4.0 font has them.

The family name matches upstream (`MonaspiceNe Nerd Font Mono`), so a terminal
config that names the released font needs no change to pick this one up.

## Install

```sh
brew tap bendrucker/fonts
brew trust bendrucker/fonts
brew uninstall --cask font-monaspice-nerd-font
brew install --cask "font-monaspice-nerd-font@tip"
```

Homebrew refuses to load casks from an untrusted third-party tap, hence `brew
trust`. The uninstall is required too: this cask declares `conflicts_with` the
released one, because both write the same filenames into `~/Library/Fonts`.

The `@tip` token is what lets `brew bundle` swap between this cask and the
released one automatically, in both directions. The quotes are belt and braces,
since `@` is not special in bash or zsh.

## Updates

The build publishes a release and bumps the cask on its own. Picking it up is
still `brew update && brew upgrade --cask`, same as any other cask.

Nothing notifies you when a release lands. Most builds add no glyph anyone would
notice, so "there was a build" is the wrong thing to push. Each release lists the
codepoints it added since the previous one, and that list is what tells you
whether an iOS re-import earns the trip. Watch this repo's releases if you would
rather be told.

## iOS

Rootshell and Moshi both read imported fonts. Each [release][releases] carries
the four `.otf` files as individual assets so a single style can be tapped and
imported from Safari without unzipping.

Import is manual, so every release lists the codepoints it added since the
previous one. Most weekly builds add nothing worth an iPad round trip.

## Checking a font

`bin/check-glyphs` asserts a font maps the codepoints this tap exists to
deliver. It reads the cmap directly and needs nothing but Python 3.

```sh
bin/check-glyphs ~/Library/Fonts/MonaspiceNeNerdFontMono-Regular.otf
```

`bin/new-codepoints OLD NEW` lists what a build gained, which is what fills in
the release notes.

## Licensing

Monaspace is [SIL OFL 1.1][ofl] with the reserved font name "Monaspace", and the
patched output inherits it. Every release ships `LICENSE-Monaspace.txt`, both
inside the zip and as its own asset. The glyphs added by patching carry their own
authors and copyrights, which the patcher records in the font's own metadata.

## Retirement

This tap is temporary. When nerd-fonts ships a release whose symbols contain
`U+EC82`, the build opens an issue saying so, and the tap goes away:

```sh
brew uninstall --cask "bendrucker/fonts/font-monaspice-nerd-font@tip"
brew untap bendrucker/fonts
brew install --cask font-monaspice-nerd-font
```

Nothing else changes, because the family name is the same.

[nerd-fonts]: https://github.com/ryanoasis/nerd-fonts
[v3.4.0]: https://github.com/ryanoasis/nerd-fonts/releases/tag/v3.4.0
[releases]: https://github.com/bendrucker/homebrew-fonts/releases
[ofl]: https://openfontlicense.org/
