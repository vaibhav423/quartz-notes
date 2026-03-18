# DOTFILES-LOGIC
## dotfiles layout
* all  files are symlinked from ~/.config/{conf} to files inside ~/.mydotfiles/com.ml4w.dotfiles/.config/
* keybindings , windowrule , autostart files are in ~/.config/hypr
## dotfiles-settings-app
* when u choose conf from the app for example keybindings(eg: mykeybind.conf) , it goes into ~/.config/hypr/conf/keybinding.conf
* which is then sourced form hyprland.conf
* similar thing happens to monitor.conf , layout , animation
* which implies the selected variation can be identified by looking those files
## hyprland
* ~/.config/hypr/conf
* copy and edit default.conf , dont modify default.conf for monitor animation keybinding etc..
* last file sourced by hyprland.conf is ~/.config/hypr/conf/custom.conf
## zshrc
* the main ~/.zshrc is symlinked to .mydotfiles
* it loads/sources files from ~/.config/zshrc/* in ascednding order based on number example 00-custom to 999-end
* note that the files can be overriden or skipped if there is a file of same name present in ~/.config/zshrc/custom
* eg 00-custom can be skipped if i put ~/.config/zshrc/custom/00-custom 
* and at last .zshrc sources ~/.zshrc-custom
## waybar
* when u choose a custom theme the theme selector modifies and writes to ~/.mydotfiles/com.ml4w.dotfiles/.config/ml4w/settings/waybar-theme.sh 
* which is then loaded
### /.mydotfiles/com.ml4w.dotfiles/.config/waybar/themes/my-waybar-theme
* the config file is the file which is responsible for the final layout.
* config.sh contains the name for theme.
* modules.json is the core file responbile for main modules / tool which is used to show on waybar from config file
* style.css (css file responsible font size colour marigin of waybar itself)
## overriden/extra files
* removed symlinks nvim / vim in the default installation of ml4w and copied from /home/ixdire/.var/app/com.ml4w.dotfilesinstaller/data/backup/com.ml4w.dotfiles/20260216-225821/.config/nvim
* .config/zshrc -> custom/ , 21-my-custom , 26-my-aliase , 999-endscri
* waybar -> added waybar/themes/my-waybar-theme
* hypr/conf -> keybindings/custom.conf ,windows/custom.conf , custom.conf (containing window rule, autstart files)
## changes made
### adding kitty -e nvim
mkdir -p ~/.local/share/applications
cat <<EOF > ~/.local/share/applications/nvim-kitty.desktop
[Desktop Entry]
Type=Application
Name=Neovim (Kitty)
Exec=kitty -e nvim %u
Terminal=false
Icon=nvim
MimeType=text/plain;text/markdown;application/x-shellscript;
EOF

update-desktop-database ~/.local/share/applications
xdg-mime default nvim-kitty.desktop text/plain
xdg-mime default nvim-kitty.desktop text/markdown
xdg-mime default nvim-kitty.desktop application/x-shellscript
### adding markdown oxide termux
cargo githubliknkn 
