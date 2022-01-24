# bash
alias l="ls -CF"
alias la="ls -aF"
alias ll="ls -l"
alias quit="exit"
alias lrm="ranger $HOME/.local/recycle"
alias rm="python3 $HOME/Python/script/rm.py"
alias timedate="timedatectl set-ntp true"

# shutdown
alias Q="shutdown -h now"
alias R="shutdown -r now"

# status
alias cm="cmatrix -C blue"
alias aq="asciiquarium"
alias sne="screenfetch"
alias ne="neofetch --ascii_distro blackarch"

# simplify
# alias ln="ln -sf"
alias ra="ranger"
alias du="sudo du -hc --max-depth=0"
alias df="df -h"
alias lg="lazygit"
alias py="python3"
alias ipy="ipython"
alias sudo="sudo -E"
alias alsa="alsamixer"
alias mkdir="mkdir -p"
alias mysql="mysql -uroot -p"
alias rename="python3 $HOME/Python/script/rename.py"
alias qv2ray="sudo -b qv2ray && quit"
alias p="ping rescld.cn"
alias zsh="source $HOME/.zshrc"
alias cat="bat"

# vim
alias vi="nvim"
alias vim="nvim"
alias ivim="vim $HOME/.config/nvim/init.vim"
alias pvim="vim $HOME/.config/nvim/config/plugins.vim"
alias svim="vim $HOME/.config/nvim/config/settings.vim"
alias mvim="vim $HOME/.config/nvim/config/mappings.vim"
export EDITOR=/usr/bin/nvim
