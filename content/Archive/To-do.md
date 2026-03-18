* gpt-5 mini using :
creating a script running in background in termux
gpt 5 mini via copilot , liniking this auth .
for example creating highly digestible notes , which must bee seen before the day ends (can be implement using if seen kind o feature)
if not seen the gpt does smth
script can use termux-open , other apis etc


* find better browser for firefox , i have problem navigating with bookmarks
maybe use a different ligic . use nvim to store bookmarks 

create a super jobbseeker goes deep into internet to seek job add a pipeline to send notification when found
must be done before 2 years of the final year of college

fix speed in nvim for large md file with latex , when fold unfolding it lags
may due tot rendering
analyze plugin by plugin to find hotsopt
just like zsh plugin load time
one solution : split the headings into files and use wikilink to link them

* add quick input dialog in pc that takes input prompt for an ai which has context . and in background runs a opencode , which i could toggle when needed

* https://github.com/ggml-org/whisper.cpp integerate with agora scaler stream to get text from audio
* modify tesseract to something better for ocr

quant course
(improve workflow) easy way to work with tasker complete integereation with pc scrcpy , etc 

* create termux-nvim toools to flex
use termux api to capture photo and in md file in nvim

* make contribution in termux to add more api like tasker , add widgets
* maybe use ai farming. let the ai contribut in termux for weeks

note taking : how ideas emerge path to traceback
* serious project (think before investing on long time ) : convert termux to chroot shell . make termux api available to chroot
create a seperate to do list for nvim
compare codecompanion and copilotchatnvim , especially the git diff feature
* change the notify in pc - for git stat help
* nexdrive pro use this to fill gdrive https://nexdrive.pro/genxfm784776215406/
add history  
class implm for kitty , size and position 
add rules in hypr, expiry  
add hyprland background border since it is difficult to identufy and close
* idea to show image in nvim in termux get the cursour position and show it on some overlay  
or stop and modify termux sorce code
* download app from lite apk and compare with play store , to find change , how it works
* create / find better memory management app for android. which categorize essential and non essential apps 
* create quiz app in nvim with timer etc
* in termux project add feature to swipe left (right side performs bringing keyboard) the special key bars to show more keys which can be customised , like a key when pressed perform ctrl-> c
* in nvim  add feature such that substitution inside math , doesnt change syntax / symbols like frac etc [2026-03-02]


time pass stuff create animation in tasker widget , may be pipe video convert to svg and loop through svg
create a project  :mutation app framework , where user can intergate his ideas into the app using ai , and also export the mutations .

ai that could monitor my activity and predict future , prevent when needed

create a potential field visualizer , for physics . where it would calcualte the potential field from given force field and a reference point

tusharmac = ee:5e:39:d0:41:7f
unify .zshrc
create quick launch command , scripts . inside rofi (add key bind to launch that ) . add a way to quickly add / remove utilities / shortcuts too . 
or
. modify the existining quick shortcuts to launch directly    
rm git-marks nvim
google-one-2tb aug-2026
gcp jan-end 2025 use gpus look for ai 
azure nov 2026  use gpu , ec engines
change yay for fzf https://wiki.archlinux.org/title/Fzf#Pacman
see more fzfs
cht.sh / tldr (the primeagen setup)
data map number - email - mac (whatsapp)
* quick way to disable plugins in nvim 
* qick launch scaler class related woks
* nvim optimise for html - java
*  git sync fix . 
* look for modification in auto comp and acceptin code suggestion in phone and pc (add enable disable auto suggestion fastly / in phone modify tab behaviour or add copilot.lua)
.general web scraping with ai 
future time bombs
for rclone : 
to change the upload ip , connect to both networks , check the default one (it will route all network) . the rest via below rules 
echo "101 wlan0_route" | sudo tee -a /etc/iproute2/rt_tables 
# gateway ip
sudo ip route add default via 192.168.1.1 dev wlan0 table wlan0_route 
# iface ip
sudo ip rule add from 192.168.8.182 lookup wlan0_route 

update youtube notes to also add something like overlay on pressing it , btings obsidian to add more
what is irc

research on wifi calling and wifi sms try wireshark to see network packets
update notify script in laptop to use kitty add option for expiry(defult) and hold the shell  

create session locker , for example youtube overlay locked as overlay to resume work incase of distraction

create general overlay for tasker (exmple just a button when on pressing does smth)

reserve 2hours time for creative works 
gdrive : add photos daily into it.

merge yazi_0 with yazi , axlefublr

create honey pot for android should include adb ssh etc , also add fake server or show the device as some other server .

push dotfile to git , add tab in nvim phone .

create accessibility button app

try - hyprland in arch-chroot https://www.reddit.com/r/termux/comments/1ib9ytn/arch_linux_on_android_chroot/

general way to create wigdget for daily use files images

proper browser bookmarks

1click browser 
create a wrapper that could take big commands directly fed to terminal into another file contain all the big commands append the last command execute , this keeps history clean  (or) modify ctrl o history feature to show only samll one or large one indvidually 

quiz in phone :
(tasker to auto launch browser , termux autorun server)
sync quiz state (github - auto push  )

nvim in phone :
add init and exit with git sync
some kind of function with argument to take notes as parameter 
add this in tasker widget over the notes display 

download Tamil movie from 1tamilmv and auto push it to gdrive


ultimate notes :
yt notes + question notes(notes when solving special questions) + general notes

WhatsApp automatic food schedule to widget
whatsapp data manipulation 

obsidian in phone : 
auto sync , tasker . 

youtube history on widgets to avoid time wate

 logger:
money tracker

fishnet:
liner algebra (khan academy )[[]]

edge 20 , rtl332





ai file manager

xposed

ok

easy git sync for a particular folder (make some genreal helpful script to git sync two files/folder in two devices)

* see future and predict

public initiative : 
ultimate way to learn (reddit) - moving from the traditional bullshit
learn more things in less time and in structured way.

some sort of jee -mode 
show everything related to chapter , example notes misc yt videos

plan for ai - speedrun(make simple tools) use uniqueness-ai for checking duplicates
reddit : find the popular / helpful members in a community (it would help soneone to directly ask to someone knowledgable)

add sponsors to 3b1b , termux , josias along with yours

plan for adding phillosiphical intricacy in life.

strategic(show useful things cool stuff , why important to why important to others , future prediction time estimation) , revolt against android , why not work on existing linux binary instead of bs api . 

a way to create rough notes , and then also way to reorganize in different way like heading wise , (ex: notes made like tree/flowxhart to be reorganized as heading like the tree could have multiple headings but we vould select the important one to be shown as heading )


learn manim
read axlefublr dotfile/blog
creating personal dot file with 
rust:
yay - paru 
nvim - helix
kitty - wezterm , alacritty , foot.ini(fastest) 
tmux - zellij
hyprland - sway , niri 
zsh - fish , nushell



install fzf ohmyposh (ml4w zen.tom) ohmyzish (ml4w) nvim clone 
curl -s https://ohmyposh.dev/install.sh | bash -s

    # Installing oh-my-zsh
    if [ ! -d "$HOME/.oh-my-zsh" ]; then
        echo ":: Installing oh-my-zsh"
        sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
        cp ~/.config/ml4w/tpl/.zshrc ~/
    else
        echo ":: oh-my-zsh already installed"
    fi

    # Installing zsh-autosuggestions
    if [ ! -d "$HOME/.oh-my-zsh/custom/plugins/zsh-autosuggestions" ]; then
        echo ":: Installing zsh-autosuggestions"
        git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
    else
        echo ":: zsh-autosuggestions already installed"
    fi

    # Installing zsh-syntax-highlighting
    if [ ! -d "$HOME/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting" ]; then
        echo ":: Installing zsh-syntax-highlighting"
        git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
    else
        echo ":: zsh-syntax-highlighting already installed"
    fi

    # Installing fast-syntax-highlighting
    if [ ! -d "$HOME/.oh-my-zsh/custom/plugins/fast-syntax-highlighting" ]; then
        echo ":: Installing fast-syntax-highlighting"
        git clone https://github.com/zdharma-continuum/fast-syntax-highlighting.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/fast-syntax-highlighting
    else
        echo ":: fast-syntax-highlighting already installed"
    fi

dev env setup :
1.) check existing setups with ai
2.) create
example manim


easy dev setup with ai 
https://drive.google.com/file/d/1G8ko_VUWRfbr9xu_ue--9sRXnTXetoZI/view




projects:

uniqueness ai
wifi triangulation / Bluetooth 
wifi captive
tampermonkey ai 

list of hacked wifi on map 

screen sync

mini projects (youtube widget / youtube time calculator )

youtube comment search

youtube money calculate
grab a single frame from torrent.

create youtube chanell deploy webpage with serverless backend which scans youtube comments and shows it in our webpage

mipsel bin

math / physics proj

mipsel bin

math / physics proj

linkedin ai 

fun-proj:





math:
systematic count a+b , a-b multiple of 4 ab chosen fro 0 to 1
Ah = 2rcosa plot to find out if constant . h = ortho centre
