from libqtile import widget
from .theme import colors

widget_defaults = dict(
    font="JetBrains Mono Nerd Font",
    fontsize=12,
    padding=3,
    foreground=colors[15]
)

extension_defaults = widget_defaults.copy()

primary_widgets = [
    widget.GroupBox(
        highlight_method='block',
        active=colors[15],
        inactive=colors[7],
        urgent_alert_method='block',
        urgent_border=colors[1],
        urgent_text=colors[15],
        this_current_screen_border=colors[4],
        rounded=False,
        spacing=0,
        padding_y=4,
        margin_x=0,
        use_mouse_wheel=False,
        disable_drag=True,
    ),
    widget.TextBox("|"),
    widget.CurrentLayout(),
    widget.Prompt(
        background=colors[8],
        ignore_dups_history=True
    ),
    widget.TextBox("|"),
    widget.WindowName(
        #format='|{state}{name}|'
        foreground=colors[3],
    ),
    widget.Systray(),
    widget.TextBox("|"),
    widget.Chord(
        chords_colors={
            "launch": ("#ff0000", "#ffffff"),
        },
        name_transform=lambda name: name.upper(),
    ),
    #widget.CurrentLayoutIcon(scale=0.5,padding=0),

    #widget.Battery(
    #    charge_char='󰂄',
    #    discharge_char='󰁹',
    #    empty_char='󱃌',
    #    show_short_text=False,
    #    format='{char} {percent:2.0%}'
    #),
    #widget.TextBox("|"),

    # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
    # widget.StatusNotifier(),
    widget.Volume(
        fmt='墳 {}',
        step=5
    ),

    # widget.PulseVolume(
    #     fmt='󰕾 {}',
    #     step=5,
    #     limit_max_volume=True
    # ),
    
    widget.TextBox("|"),
    widget.Net(format="󰖩 {total}"),
    # widget.TextBox("|"),
    # widget.Wlan(format="󰖩 {essid}"),
    widget.TextBox("|"),
    widget.Clock(format="󰸗 %Y.%m.%d %H:%M "),
    widget.QuickExit(
        background=colors[1],
        default_text=' 󰐥  ',
        countdown_format='󰐥 {} '
    ),
]
secondary_widgets = [
    widget.GroupBox(
        highlight_method='block',
        active=colors[15],
        inactive=colors[7],
        urgent_alert_method='block',
        urgent_border=colors[1],
        urgent_text=colors[15],
        this_current_screen_border=colors[4],
        rounded=False,
        spacing=0,
        padding_y=4,
        margin_x=0,
        use_mouse_wheel=False,
        disable_drag=True,
    ),
    widget.Prompt(
        background=colors[8],
        ignore_dups_history=True
    ),
    widget.TextBox("|"),
    widget.WindowName(
        #format='|{state}{name}|'
        foreground=colors[3],
    ),
    widget.TextBox("|"),
    widget.Chord(
        chords_colors={
            "launch": ("#ff0000", "#ffffff"),
        },
        name_transform=lambda name: name.upper(),
    ),
    #widget.CurrentLayoutIcon(scale=0.5,padding=0),
    widget.CurrentLayout(),
    widget.TextBox("|"),
    widget.Battery(
        charge_char='󰂄',
        discharge_char='󰁹',
        empty_char='󱃌',
        show_short_text=False,
        format='{char} {percent:2.0%}'
    ),
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
        fmt='󰕾 {}',
        step=5,
        limit_max_volume=True
    ),
    widget.TextBox("|"),
    widget.Net(format="󰖩 {total}"),
    widget.TextBox("|"),
    widget.Clock(format="󰸗 %Y.%m.%d %H:%M "),
    widget.QuickExit(
        background=colors[1],
        default_text=' 󰐥  ',
        countdown_format='󰐥 {} '
    ),
]
