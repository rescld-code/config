#!/bin/bash

# AutoStart
compton &
# variety &
fcitx &
feh --bg-scale /home/cy/Pictures/yousa/3D/6.jpg &
# oneko &
# screenkey &

# TIM gnome-settings-daemon
/usr/lib/gsd-xsettings &

# monitor
python3 /home/cy/.config/awesome/autostart/monitor.py &
