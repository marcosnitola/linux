#!/bin/bash
if [ "$1" = "-f" ]; then
  notify-send $1
  xfce4-screenshooter -f -s "/home/marcos/Imágenes/Capturas de pantalla/qttest_$(date +%Y-%m-%d_%H-%M-%S).png"
elif [ "$1" = "-r" ]; then
  notify-send $1
  xfce4-screenshooter -r -s "/home/marcos/Imágenes/Capturas de pantalla/qttest_$(date +%Y-%m-%d_%H-%M-%S).png"
fi 
