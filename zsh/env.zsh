# virtualenv
# export WORKON_HOME=$HOME/.virtualenvs
# export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
# export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
# source /usr/local/bin/virtualenvwrapper.sh

# FZF
# [ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
[ -f /usr/share/fzf/completion.zsh ] && source /usr/share/fzf/completion.zsh
[ -f /usr/share/fzf/key-bindings.zsh ] && source /usr/share/fzf/key-bindings.zsh
export FZF_COMPLETION_TRIGGER='\'
# export FZF_DEFAULT_OPTS="--height 40% --layout=reverse --preview '(highlight -O ansi {} || cat {}) 2> /dev/null | head -500'"
export FZF_DEFAULT_OPTS="--height 40% --layout=reverse --preview 'bat --color=always --style=numbers --line-range=:500 {}'"

# jdk
# export JAVA_HOME=$HOME/.jdk8/
# export PATH=$JAVA_HOME/bin:$PATH
# export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar

# Maven
# export M2_HOME=$HOME/.Maven/bin
# export MAVEN_HOME=$HOME/.Maven
# export PATH=$PATH:$MAVEN_HOME/bin

# PyPi
export PATH=$PATH:$HOME/.local/bin

# Conda
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
# __conda_setup="$('/opt/anaconda/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
# if [ $? -eq 0 ]; then
#     eval "$__conda_setup"
# 	alias base='conda deactivate'
# 	alias rescld='conda activate rescld'
# else
#     if [ -f "/opt/anaconda/etc/profile.d/conda.sh" ]; then
#         . "/opt/anaconda/etc/profile.d/conda.sh"
#     else
#         export PATH="/opt/anaconda/bin:$PATH"
#     fi
# fi
# unset __conda_setup
# <<< conda initialize <<<

# golang
export GO111MODULE=auto
export GOPATH=$HOME/.go
export PATH=$PATH:$GOPATH/bin
export GOPROXY=https://goproxy.cn,direct

# ranger
export RANGER_LOAD_DEFAULT_RC=FALSE

# alacritty
# fpath+=${ZDOTDIR:-~}/.zsh_functions

