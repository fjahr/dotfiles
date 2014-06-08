# content ~/.bashrc

source ~/bin/dotfiles/bashrc

# content ~/.bash_profile

if [ -f `brew --prefix`/etc/bash_completion ];
then
  source `brew --prefix`/etc/bash_completion
fi
if [ -f ~/.bashrc ];
then
	source ~/.bashrc
fi
