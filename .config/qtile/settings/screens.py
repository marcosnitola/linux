from libqtile import bar
from libqtile.config import Screen
from .theme import colors
from .widgets import primary_extensions

screens = [
    Screen(
        top=bar.Bar(
            primary_extensions,
            24,
            background=colors[0],
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        wallpaper="/home/marcos/Imágenes/Wallpapers/wp11977058-puss-in-boots-the-last-wish-death-wallpapers.jpg",
        wallpaper_mode="fill"
    ),
]
