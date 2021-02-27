#!/bin/bash

# AutoStart
compton -i 1&
# variety &
# fcitx5 &
feh --bg-scale $HOME/.config/awesome/background/desktop.jpg &
# oneko &
# screenkey &

# TIM gnome-settings-daemon
/usr/lib/gsd-xsettings &

# lock
xset s 180 # time
lock_img="i3lock -i $HOME/.config/awesome/background/lock.png"
xss-lock -n "$lock_img" -- i3lock -n &

# notice
python3 $HOME/.config/awesome/autostart/script/notice.py &
python3 $HOME/.config/awesome/autostart/script/bilibili/status.py &

# clock in
python3 $HOME/.config/awesome/autostart/script/bilibili/clockIn.py &
python3 $HOME/.config/awesome/autostart/script/weibo/chlockIn.py &

# fcitx
gsettings set \
org.gnome.settings-daemon.plugins.xsettings overrides \
"{Gtk/IMModule:<fcitx>}"
