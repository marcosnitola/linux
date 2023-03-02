#!/bin/bash
if [ "$1" = "-f" ]; then
  pathimage="/home/marcos/Imágenes/Capturas de pantalla/qt_$(date +%Y-%m-%d_%H-%M-%S).png"
  xfce4-screenshooter -f -s "$pathimage"
  notify-send -u low -i "$pathimage" "Full screenshot saved" "$pathimage"
elif [ "$1" = "-r" ]; then
  pathimage="/home/marcos/Imágenes/Capturas de pantalla/qt_$(date +%Y-%m-%d_%H-%M-%S).png"
  xfce4-screenshooter -r -s "$pathimage"
  notify-send -u low -i "$pathimage" "Region screenshot saved" "$pathimage"
elif [ "$1" = "-F" ]; then
  pathimage="/tmp/screenshot.png"
  xfce4-screenshooter -f -s "$pathimage"
  xclip -selection clipboard -t image/png -i "/tmp/screenshot.png"
  notify-send -u low -i "$pathimage" "Full screenshot copied" "$pathimage"
elif [ "$1" = "-R" ]; then
  pathimage="/tmp/screenshot.png"
  xfce4-screenshooter -r -s "$pathimage"
  xclip -selection clipboard -t image/png -i "/tmp/screenshot.png"
  notify-send -u low -i "$pathimage" "Region screenshot copied" "$pathimage"
fi 
