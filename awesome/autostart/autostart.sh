#!/bin/bash

# AutoStart
compton &
# variety &
fcitx5 &
feh --bg-scale /home/cy/Downloads/background/desktop.jpg &
# oneko &
# screenkey &

# TIM gnome-settings-daemon
/usr/lib/gsd-xsettings &

# lock
xset s 180 # time
xss-lock -n 'i3lock -i /home/cy/Downloads/background/lock.png' -- i3lock -n &

# notice
python3 /home/cy/.config/awesome/autostart/notice.py &

# fcitx
gsettings set \
org.gnome.settings-daemon.plugins.xsettings overrides \
"{Gtk/IMModule:<fcitx>}"
