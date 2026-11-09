# puzzlo wordmark generator — stroke-built rounded geometric lettering
import sys, os
W=22  # stroke weight on a 100-unit x-height
def letters():
    p  = "M11 128 V11 M11 50 A39 39 0 1 0 89 50 A39 39 0 1 0 11 50"
    u  = "M129 11 V50 A39 39 0 0 0 207 50 V11 M207 11 V89"
    z1 = "M243 11 H301 L243 89 H337"          # bottom bar runs on into z2
    z2 = "M337 11 H395 L337 89 H395"
    l  = "M435 -31 V89"
    o  = "M473 50 A39 39 0 1 0 551 50 A39 39 0 1 0 473 50"
    return [p,u,z1,z2,l,o]
# puzzle-edge cut through the shared baseline: a knob from the 2nd z locks into the 1st
CUT = "M299 72.5 A16.5 16.5 0 0 1 299 105.5"
VB = "-6 -48 574 193"
def svg(fg, bg=None, mid="m"):
    paths = "".join(f'<path d="{d}"/>' for d in letters())
    bgrect = f'<rect x="-6" y="-48" width="574" height="193" fill="{bg}"/>' if bg else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VB}" role="img" aria-label="puzzlo">
<title>puzzlo</title>
<defs><mask id="cut-{mid}" maskUnits="userSpaceOnUse" x="-6" y="-48" width="574" height="193"><rect x="-6" y="-48" width="574" height="193" fill="#fff"/><path d="{CUT}" fill="none" stroke="#000" stroke-width="3.4" stroke-linejoin="round"/></mask></defs>
{bgrect}<g mask="url(#cut-{mid})" fill="none" stroke="{fg}" stroke-width="{W}" stroke-linecap="round" stroke-linejoin="round">{paths}</g>
</svg>
'''
out = sys.argv[1]
INK, IVORY, CORAL = "#182C55", "#F7F5EF", "#D76B55"
files = {
 "puzzlo-logo-primary.svg": svg(INK, None, "p"),
 "puzzlo-logo-mono-black.svg": svg("#000000", None, "k"),
 "puzzlo-logo-reversed.svg": svg(IVORY, INK, "r"),
 "puzzlo-logo-reversed-transparent.svg": svg(IVORY, None, "t"),
 "puzzlo-logo-on-ivory.svg": svg(INK, IVORY, "i"),
}
for n,s in files.items(): open(os.path.join(out,n),"w").write(s)
# favicon: lowercase p on ink tile
fav = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="{INK}"/>
<g transform="translate(15 9) scale(.345)" fill="none" stroke="{IVORY}" stroke-width="22" stroke-linecap="round"><path d="M11 128 V11 M11 50 A39 39 0 1 0 89 50 A39 39 0 1 0 11 50"/></g></svg>
'''
open(os.path.join(out,"favicon.svg"),"w").write(fav)
