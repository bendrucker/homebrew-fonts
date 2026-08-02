cask "font-monaspice-nerd-font@tip" do
  version "2026.08.02-81aef4b"
  sha256 "c17cf943e877051ea4a24cf43a8322d1c52a9a4506e2556f4d9e34b9555097da"

  url "https://github.com/bendrucker/homebrew-fonts/releases/download/monaspice-tip-#{version}/MonaspiceNeNerdFontMono.zip"
  name "MonaspiceNe Nerd Font Mono (nerd-fonts tip)"
  desc "Monaspace Neon patched from nerd-fonts master, ahead of the next Nerd Fonts release"
  homepage "https://github.com/bendrucker/homebrew-fonts"

  # The family name is identical to the released cask's, so both would install
  # the same filenames into ~/Library/Fonts.
  conflicts_with cask: "font-monaspice-nerd-font"

  font "MonaspiceNeNerdFontMono-Regular.otf"
  font "MonaspiceNeNerdFontMono-Bold.otf"
  font "MonaspiceNeNerdFontMono-Italic.otf"
  font "MonaspiceNeNerdFontMono-BoldItalic.otf"
end
