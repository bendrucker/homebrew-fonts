cask "font-monaspice-nerd-font@tip" do
  version "2026.08.03-edf0118"
  sha256 "4b20ab272fa5f0c2ab3903949e0c38d4cce642294f3272ed3a2809aaf921a562"

  url "https://github.com/bendrucker/homebrew-fonts/releases/download/monaspice-tip-#{version}/MonaspiceNeNerdFontMono.zip"
  name "MonaspiceNe Nerd Font Mono (nerd-fonts tip)"
  desc "Monaspace Neon patched from nerd-fonts master"
  homepage "https://github.com/bendrucker/homebrew-fonts"

  # The family name is identical to the released cask's, so both would install
  # the same filenames into ~/Library/Fonts.
  conflicts_with cask: "font-monaspice-nerd-font"

  font "MonaspiceNeNerdFontMono-Regular.otf"
  font "MonaspiceNeNerdFontMono-Bold.otf"
  font "MonaspiceNeNerdFontMono-Italic.otf"
  font "MonaspiceNeNerdFontMono-BoldItalic.otf"
end
