from libqtile import bar
from libqtile.config import Screen
from .theme import colors
from .widgets import primary_widgets, secondary_widgets
import subprocess

def status_bar(widgets):
    return bar.Bar(
        widgets,
        24,
        background=colors[0],
        # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
        # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
    )

wallpaper_settings = {
    "wallpaper":"/home/marcos/Imágenes/Wallpapers/wp11977058-puss-in-boots-the-last-wish-death-wallpapers.jpg",
    "wallpaper_mode":"fill"
}

screens = [
    Screen( top=status_bar(primary_widgets),**wallpaper_settings),
]

xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if command.returncode != 0:
    error = command.stderr.decode("UTF-8")
    logger.error(f"Failed counting monitors using {xrandr}:\n{error}")
    connected_monitors = 1
else:
    connected_monitors = int(command.stdout.decode("UTF-8"))

if connected_monitors > 1:
    for _ in range(1, connected_monitors):
        screens.append(Screen(top=status_bar(secondary_widgets), **wallpaper_settings))
