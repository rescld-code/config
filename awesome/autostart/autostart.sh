#!/bin/bash

# AutoStart
compton &
# variety &
fcitx &
feh --bg-scale /home/cy/Pictures/ruki/12.jpg &
# oneko &
# screenkey &

# TIM gnome-settings-daemon
/usr/lib/gsd-xsettings &

# lock
xset s 180 # time
xss-lock -n 'i3lock -i /home/cy/Downloads/background.png' -- i3lock -n &

# notice
python3 /home/cy/.config/awesome/autostart/notice.py &
