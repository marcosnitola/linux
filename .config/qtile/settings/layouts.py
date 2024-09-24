from libqtile import layout 
from libqtile.config import Match
from .theme import colors

layout_theme = {
    "margin": 7,
    "border_width": 3,
    "border_focus": colors[4],
    "border_normal": colors[7]
}

layouts = [
    layout.Columns(border_on_single=True, **layout_theme),
    layout.Max(
        border_focus=colors[3],
        border_normal=colors[3],
        border_width=layout_theme["border_width"],
        margin=layout_theme["margin"]),
    layout.Floating(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    #layout.Spiral(**layout_theme),
    #layout.MonadTall(**layout_theme),
    #layout.MonadWide(**layout_theme),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    #layout.Zoomy(),
]

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
