export ZSH=$HOME/.oh-my-zsh
ZSH_THEME="gentoo"
COMPLETION_WAITING_DOTS="true"
plugins=(git sudo zsh-autosuggestions zsh-syntax-highlighting zsh-completions history-substring-search)
autoload -U compinit && compinit
source $ZSH/oh-my-zsh.sh
export LANG=en_US.UTF-8
export EDITOR='vim'
alias c='clear'
alias ll='ls -l'
alias la='ls -a'
alias vi='vim'
alias -s jar='java -jar'
alias e='exit'

if [[ -z "$TMUX" ]] ;then
    ID="`tmux ls | grep -vm1 attached | cut -d: -f1`" # get the id of a deattached session
    if [[ -z "$ID" ]] ;then # if not available create a new one
        tmux new-session
    else
        tmux attach-session -t "$ID" # if available attach to it
    fi
fi
