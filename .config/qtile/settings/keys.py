from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    #     Split = all windows displayed
    #     Unsplit = 1 window displayed, like Max layout, but still with
    #     multiple stack panes
    Key([mod, "shift"],"Return",lazy.layout.toggle_split(),desc="Toggle between split and unsplit sides of stack",),
    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "Shift"], "Tab", lazy.prev_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn('rofi -show run'), desc="Spawn Rofi command"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating on focused window"),
    Key([mod, "Shift"], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on focused window"),
    # Take screenshots
    Key([], "Print", lazy.spawn("bash /home/marcos/.config/qtile/screenshot.sh -f"), desc="Save full screenshot"),
    Key(["control"], "Print", lazy.spawn("bash /home/marcos/.config/qtile/screenshot.sh -F"), desc="Copy to clipboard full screenshot"),
    Key(["shift"], "Print", lazy.spawn("bash /home/marcos/.config/qtile/screenshot.sh -r"), desc="Save regional screenshot"),
    Key(["control", "shift"], "Print", lazy.spawn("bash /home/marcos/.config/qtile/screenshot.sh -R"), desc="Copy to clipboard regional screenshot"),
    # Execute apps
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch browser"),
    Key([mod], "e", lazy.spawn("thunar"), desc="Launch file explorer"),
    Key([mod], "t", lazy.spawn("Portables/Telegram/Telegram"), desc="Launch file explorer"),
    # Control volume
    Key([],"XF86AudioRaiseVolume", lazy.widget["volume"].increase_vol(), desc="Increase volume"),
    Key([],"XF86AudioLowerVolume", lazy.widget["volume"].decrease_vol(), desc="Decrease volume"),
    Key([],"XF86AudioMute", lazy.widget["volume"].mute(), desc="Mute volume"),
    #Key([],"XF86AudioRaiseVolume", lazy.spawn("amixer sset Master playback 5%+"), desc="Increase volume"),
    #Key([],"XF86AudioLowerVolume", lazy.spawn("amixer sset Master playback 5%-"), desc="Decrease volume"),
    #Key([],"XF86AudioMute", lazy.spawn("amixer sset Master toggle"), desc="Mute volume"),
    # Control brightness
    Key([],"XF86MonBrightnessUp", lazy.spawn("brightnessctl s 5%+"), desc="Increase brightness"),
    Key([],"XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%-"), desc="Decrease brightness"),
    Key([mod],"s", lazy.spawn("xscreensaver-command -lock"), desc="Lock screen"),
]
