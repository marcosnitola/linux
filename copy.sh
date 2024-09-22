#!/bin/sh
# Copies all the files from ~ to this repo
if [ "$1" = ".vimrc" ]; then
  cp -v ~/.vimrc .
elif [ "$1" = "" ]; then
  cp -v ~/.vimrc .
  cp -v ~/.bashrc .
  cp -vr ~/.config/qtile/* ./.config/qtile/
  cp -vr ~/.config/i3/* ./.config/i3/
  cp -v ~/.config/alacritty/alacritty.yml ./.config/alacritty/alacritty.yml
  cp -vr ~/.config/nvim/* ./.config/nvim/
else
  echo "Can't recognize $1"
fi
