from libqtile.config import Group, Match, Key
from libqtile.lazy import lazy
from .keys import keys, mod

groups = [
    Group("NET",   label=" 󰖟 ",
        layout="max",
        matches=[
            Match(wm_class="google-chrome"),
            Match(wm_class="firefox"),
            Match(wm_class="chromium"),
            Match(wm_class="midori")]),
    Group("TERM",  label="  "),
    Group("DEV",   label=" 󰅩 "),
    Group("SYS",   label=" 󰣖 "),
    Group("FILE",  label=" 󰉋 ",
        matches=[Match(wm_class="thunar")]),
    Group("CHAT",  label=" 󰊌 ",
        matches=[Match(wm_class="telegram-desktop")]),
    Group("MEDIA", label=" 󰎁 ",
        matches=[Match(wm_class="zoom"),Match(wm_class="vlc")]),
    Group("GFX",   label=" 󰘔 ",
        layout="floating"),
    Group("MISC",  label=" 󰛄 "),
    Group("MISC2", label=" 󰛄 ")
]

for i, group in zip(["1","2","3","4","5","6","7","8","9","0"], groups):
    keys.append(Key([mod], i, lazy.group[group.name].toscreen()))
    keys.append(Key([mod, "shift"], i, lazy.window.togroup(group.name, switch_group=True)))
