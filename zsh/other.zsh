# clock in
alias weibo="python3 $HOME/.config/awesome/autostart/script/weibo/clockIn.py"
alias bilibili="python3 $HOME/.config/awesome/autostart/script/bilibili/clockIn.py"
function clockIn(){
	python3 $HOME/.config/awesome/autostart/script/weibo/clockIn.py
	python3 $HOME/.config/awesome/autostart/script/bilibili/clockIn.py
}

# home wifi
# alias link="sudo -b wpa_supplicant -B -c $HOME/.wifi/home.conf -i wlp3s0"

# school wifi
alias link="sudo -b wpa_supplicant -B -c $HOME/.wifi/FJPIT.conf -i wlp3s0"
alias submit="python3 $HOME/Python/script/FJPIT.py"

alias unlink="sudo killall wpa_supplicant"

# backlight
# alias ilight="sudo xbacklight -inc 10"
# alias dlight="sudo xbacklight -dec 10"
alias light="sudo chown cyun:cyun /sys/class/backlight/intel_backlight/brightness"

# server
alias ser="ssh -i $HOME/.ssh/rescld.cn.pem ubuntu@rescld.cn"
alias sscp="python3 $HOME/Python/script/scp.py"

# raspberry pi
alias pi="ssh pi@192.168.1.111"
alias nas="sudo mount.cifs -o username='pi',dir_mode=0777,file_mode=0777 //192.168.1.111/share /mnt"
