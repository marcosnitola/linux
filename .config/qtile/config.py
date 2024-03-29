# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
import subprocess
from libqtile import hook

mod = "mod4"
terminal = guess_terminal()
#terminal = "alacritty"
browser = "google-chrome"

# Colors based on Gruvbox theme
colors = [
    '282828',
    'CC241D',
    '98971A',
    'D79921',
    '458588',
    'b16286',
    '689D6A',
    'A89984',
    '928374',
    'FB4934',
    'B8BB26',
    'FABD2F',
    '83A598',
    'D3869B',
    '8EC07C',
    'EBDBB2'
]

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
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "Shift"], "Tab", lazy.prev_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating on focused window"),
    # Take screenshots
    Key([], "Print", lazy.spawn("bash /home/marcos/.config/qtile/screenshot.sh -f"), desc="Save full screenshot"),
    Key(["control"], "Print", lazy.spawn("bash /home/marcos/.config/qtile/screenshot.sh -F"), desc="Copy to clipboard full screenshot"),
    Key(["shift"], "Print", lazy.spawn("bash /home/marcos/.config/qtile/screenshot.sh -r"), desc="Save regional screenshot"),
    Key(["control", "shift"], "Print", lazy.spawn("bash /home/marcos/.config/qtile/screenshot.sh -R"), desc="Copy to clipboard regional screenshot"),
    # Execute apps
    Key([mod], "b", lazy.spawn(browser), desc="Launch terminal"),
    Key([mod], "e", lazy.spawn("thunar"), desc="Launch terminal"),
]

groups = [
    Group("NET", layout="max", matches=[Match(wm_class="google-chrome")]),
    Group("TERM"),
    Group("DEV"),
    Group("SYS"),
    Group("CHAT", matches=[Match(wm_class="telegram-desktop")]),
    Group("MEDIA", matches=[Match(wm_class="zoom")]),
    Group("GFX", layout="floating")
]

for i, group in zip(["1","2","3","4","5","6","7","8","9","0"], groups):
    keys.append(Key([mod], i, lazy.group[group.name].toscreen()))
    keys.append(Key([mod, "shift"], i, lazy.window.togroup(group.name, switch_group=True)))

layout_theme = {
    "margin": 7,
    "border_width": 3,
    "border_focus": colors[4],
    "border_normal": colors[7]
}

layouts = [
    layout.Columns(border_on_single=True, **layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.Spiral(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrains Mono Nerd Font",
    #font="sans",
    fontsize=12,
    padding=3,
    foreground="#EBDBB2"
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method='block',
                    active=colors[15],
                    inactive=colors[7],
                    urgent_alert_method='block',
                    urgent_border=colors[1],
                    urgent_text='EBDBB2',
                    this_current_screen_border=colors[4],
                    rounded=False,
                    spacing=0,
                    padding_y=4,
                    margin_x=0
                ),
                widget.Prompt(
                    background="#928374",
                    ignore_dups_history=True
                ),
                widget.TextBox("|"),
                widget.WindowName(
                    #format='|{state}{name}|'
                ),
                widget.TextBox("|"),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayout(),
                widget.TextBox("|"),
                #widget.TextBox("New config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                #widget.Volume(
                #    fmt='墳 {}',
                #    step=5
                #),
                widget.PulseVolume(
                    fmt='墳 {}',
                    step=5,
                    limit_max_volume=True
                ),
                #widget.Net(),
                widget.Systray(),
                widget.TextBox("|"),
                widget.Clock(format=" %Y.%m.%d %H:%M "),
                widget.QuickExit(
                    background=colors[1],
                    default_text='   ',
                    countdown_format=' {} '
                ),
            ],
            24,
            background=colors[0],
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        wallpaper="/home/marcos/Imágenes/wp4720954.jpg",
        wallpaper_mode="fill"
    ),
]

keys.extend([
    #Key([],"XF86AudioRaiseVolume", lazy.widget["volume"].increase_vol(), desc="Increase volume"),
    #Key([],"XF86AudioLowerVolume", lazy.widget["volume"].decrease_vol(), desc="Decrease volume"),
    #Key([],"XF86AudioMute", lazy.widget["volume"].mute(), desc="Mute volume"),
    Key([],"XF86AudioRaiseVolume", lazy.widget["pulsevolume"].increase_vol(), desc="Increase volume"),
    Key([],"XF86AudioLowerVolume", lazy.widget["pulsevolume"].decrease_vol(), desc="Decrease volume"),
    Key([],"XF86AudioMute", lazy.widget["pulsevolume"].mute(), desc="Mute volume"),
    #Key([],"XF86AudioRaiseVolume", lazy.spawn("amixer sset Master playback 5%+"), desc="Increase volume"),
    #Key([],"XF86AudioLowerVolume", lazy.spawn("amixer sset Master playback 5%-"), desc="Decrease volume"),
    #Key([],"XF86AudioMute", lazy.spawn("amixer sset Master toggle"), desc="Mute volume"),
    Key([],"XF86MonBrightnessUp", lazy.spawn("brightnessctl s 5%+"), desc="Increase brightness"),
    Key([],"XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%-"), desc="Decrease brightness"),
])

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod, "shift"], "Button1", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    **layout_theme
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# Initial script shell once Qtile starts
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
