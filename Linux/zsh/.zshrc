export ZSH=$HOME/.oh-my-zsh

setopt HIST_IGNORE_DUPS

ZSH_THEME="gentoo"

COMPLETION_WAITING_DOTS="true"

plugins=(git sudo zsh-autosuggestions zsh-syntax-highlighting zsh-completions)

[[ -s /user/share/autojump/autojump.zsh ]] && . /user/share/autojump/autojump.zsh

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
[[ -e ./.zshrc ]] && neofetch

export DEFAULT_USER='breathiness'
TERM=xterm-256color
