#!/bin/sh
# Copies all the files from ~ to this repo
if [ "$1" = ".vimrc" ]; then
  cp -v ~/.vimrc .
elif [ "$1" = "" ]; then
  cp -v ~/.vimrc .
  cp -v ~/.bashrc .
  cp -v ~/.config/qtile/config.py ./.config/qtile/
  cp -v ~/.config/i3/* ./.config/i3/
  cp -v ~/.config/alacritty/alacritty.yml ./.config/alacritty/alacritty.yml
  cp -v ~/.config/nvim/init.vim ./.config/nvim/init.vim
else
  echo "Can't recognize $1"
fi
