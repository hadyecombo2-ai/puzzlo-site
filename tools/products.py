"""Product imagery for the Puzzlo sample catalogue (4:5 WebP)."""
import cairo, math, random, sys, os
import video as V
from video import hx, INK, IVORY, CORAL, trace, straight, reverse

OUT = sys.argv[1]
PWID, PHEI = 1000, 1250

def jig_paths(cols, rows, w, h, seed, S):
    rnd = random.Random(seed); V.S = S
    pw, ph = w / cols, h / rows
    he, ve = {}, {}
    for r in range(1, rows):
        for c in range(cols):
            he[(r, c)] = V.make_edge((c*pw, r*ph), ((c+1)*pw, r*ph), rnd.choice((-1, 1)), rnd.uniform(-.05, .05), rnd.uniform(.9, 1.04))
    for c in range(1, cols):
        for r in range(rows):
            ve[(r, c)] = V.make_edge((c*pw, r*ph), (c*pw, (r+1)*ph), rnd.choice((-1, 1)), rnd.uniform(-.05, .05), rnd.uniform(.9, 1.04))
    out = {}
    for r in range(rows):
        for c in range(cols):
            tl, tr, br, bl = (c*pw, r*ph), ((c+1)*pw, r*ph), ((c+1)*pw, (r+1)*ph), (c*pw, (r+1)*ph)
            top = he[(r, c)] if r else straight(tl, tr)
            right = ve[(r, c+1)] if c < cols-1 else straight(tr, br)
            bot = reverse(he[(r+1, c)]) if r < rows-1 else straight(br, bl)
            left = reverse(ve[(r, c)]) if c else straight(bl, tl)
            out[(r, c)] = (tl, top[1] + right[1] + bot[1] + left[1])
    return out

# ---------- scenes (draw into w x h) ----------
def sky(c, w, h, top, bot, y1):
    g = cairo.LinearGradient(0, 0, 0, y1); g.add_color_stop_rgb(0, *hx(top)); g.add_color_stop_rgb(1, *hx(bot))
    c.set_source(g); c.rectangle(0, 0, w, y1); c.fill()

def corniche(c, w, h):
    sky(c, w, h, '#F2D9C6', '#E9A58C', h*.62)
    c.set_source_rgb(*hx('#F7E6D6')); c.arc(w*.72, h*.30, 70, 0, 2*math.pi); c.fill()
    rnd = random.Random(11); x = 30
    while x < w - 30:
        bw = rnd.uniform(40, 80); bh = rnd.uniform(140, 360)
        c.set_source_rgb(*hx(rnd.choice(['#2B4A7C', '#203A66', '#34548A'])))
        c.rectangle(x, h*.62 - bh, bw, bh); c.fill()
        if rnd.random() < .35: c.arc(x + bw/2, h*.62 - bh, bw/2, math.pi, 0); c.fill()
        c.set_source_rgba(*hx('#F4C9A8'), .8)
        for yy in range(int(h*.62 - bh + 16), int(h*.62 - 10), 22):
            c.rectangle(x + 8, yy, bw - 16, 3); c.fill()
        x += bw + rnd.uniform(4, 14)
    c.set_source_rgb(*hx('#22406F')); c.rectangle(0, h*.62, w, h*.2); c.fill()
    c.set_source_rgba(*hx('#F4C9A8'), .55); c.set_line_width(3)
    for i in range(26):
        yy = h*.64 + rnd.uniform(0, h*.16); xx = rnd.uniform(0, w); c.move_to(xx, yy); c.line_to(xx + rnd.uniform(20, 60), yy); c.stroke()
    c.set_source_rgb(*hx('#E6CFAE')); c.rectangle(0, h*.82, w, h*.18); c.fill()
    c.set_source_rgb(*hx('#D7BB92')); c.rectangle(0, h*.82, w, 14); c.fill()
    for lx in range(60, int(w), 180):  # lamps
        c.set_source_rgb(*INK); c.rectangle(lx, h*.82 - 110, 5, 110); c.fill()
        c.set_source_rgb(*CORAL); c.arc(lx + 2.5, h*.82 - 114, 9, 0, 2*math.pi); c.fill()

def windtowers(c, w, h):
    sky(c, w, h, '#BFD3E6', '#EEF0EA', h*.5)
    rnd = random.Random(5)
    walls = ['#EFDFC4', '#E7D2B1', '#F2E5CE', '#E3CAA4']
    xs = [(-20, 300, .55), (260, 260, .42), (500, 280, .5), (760, 280, .38)]
    for i, (x, bw, top) in enumerate(xs):
        y0 = h * top
        c.set_source_rgb(*hx(walls[i])); c.rectangle(x, y0, bw, h - y0); c.fill()
        c.set_source_rgb(*hx('#D2B68E')); c.rectangle(x + bw * .78, y0, bw * .22, h - y0); c.fill()
        tx, tw = x + bw * .25, 90
        c.set_source_rgb(*hx(walls[i])); c.rectangle(tx, y0 - 170, tw, 170); c.fill()
        c.set_source_rgb(*hx('#D2B68E')); c.rectangle(tx + tw*.72, y0 - 170, tw*.28, 170); c.fill()
        c.set_source_rgb(*INK)
        for k in range(4): c.rectangle(tx + 10 + k * 18, y0 - 150, 8, 90); c.fill()
        c.set_source_rgb(*hx(walls[i])); c.rectangle(tx - 8, y0 - 182, tw + 16, 14); c.fill()
        for k in range(3):
            c.set_source_rgb(*INK); wx = x + 30 + k * 70
            if wx + 30 > x + bw * .75: break
            c.rectangle(wx, y0 + 90, 30, 46); c.fill(); c.arc(wx + 15, y0 + 90, 15, math.pi, 0); c.fill()
    c.set_source_rgb(*CORAL); c.rectangle(560, h - 260, 110, 260); c.fill(); c.arc(615, h - 260, 55, math.pi, 0); c.fill()
    c.set_source_rgb(*hx('#B5523F')); c.rectangle(612, h - 300, 6, 300); c.fill()
    c.set_source_rgb(*hx('#E2C9A2')); c.rectangle(0, h - 40, w, 40); c.fill()

def dhows(c, w, h):
    sky(c, w, h, '#F4EADB', '#F3D9C2', h*.45)
    c.set_source_rgb(*CORAL); c.arc(w*.2, h*.25, 60, 0, 2*math.pi); c.fill()
    c.set_source_rgb(*hx('#2B4A7C')); c.rectangle(0, h*.45, w, h*.55); c.fill()
    c.set_source_rgb(*hx('#22406F')); c.rectangle(0, h*.7, w, h*.3); c.fill()
    def boat(x, y, s, sail):
        c.save(); c.translate(x, y); c.scale(s, s)
        c.set_source_rgb(*hx('#8E5638')); c.move_to(-92, -18); c.line_to(96, -26); c.curve_to(80, 4, 40, 14, -40, 14); c.curve_to(-70, 10, -86, -2, -92, -18); c.close_path(); c.fill()
        c.set_source_rgb(*INK); c.set_line_width(4); c.move_to(4, -24); c.line_to(-6, -170); c.stroke()
        c.set_source_rgb(*hx(sail)); c.move_to(-4, -168); c.curve_to(40, -150, 84, -100, 92, -36); c.line_to(2, -36); c.close_path(); c.fill()
        c.restore()
    boat(300, h*.62, 1.6, '#F7F5EF'); boat(720, h*.56, 1.1, '#F0C4B6'); boat(860, h*.5, .6, '#F7F5EF'); boat(140, h*.86, 1.9, '#F7F5EF')
    c.set_source_rgba(*IVORY, .5); c.set_line_width(3); rnd = random.Random(2)
    for i in range(30):
        yy = rnd.uniform(h*.47, h); xx = rnd.uniform(0, w); c.move_to(xx, yy); c.line_to(xx + rnd.uniform(16, 50), yy); c.stroke()

def desert(c, w, h):
    c.set_source_rgb(*INK); c.rectangle(0, 0, w, h); c.fill()
    rnd = random.Random(9); c.set_source_rgb(*IVORY)
    for i in range(120): c.arc(rnd.uniform(0, w), rnd.uniform(0, h*.55), rnd.uniform(.8, 2.4), 0, 2*math.pi); c.fill()
    c.set_source_rgb(*hx('#F7E6C8')); c.arc(w*.74, h*.2, 54, 0, 2*math.pi); c.fill()
    c.set_source_rgb(*INK); c.arc(w*.74 + 22, h*.2 - 10, 50, 0, 2*math.pi); c.fill()
    for col, y0, amp in (('#7A4D5A', .56, 40), ('#B8604E', .66, 50), ('#D76B55', .76, 46), ('#E6A27E', .88, 36)):
        c.set_source_rgb(*hx(col)); c.move_to(0, h)
        c.line_to(0, h*y0)
        c.curve_to(w*.25, h*y0 - amp, w*.45, h*y0 + amp, w*.7, h*y0 - amp*.6); c.curve_to(w*.85, h*y0 - amp, w*.95, h*y0, w, h*y0 - 10)
        c.line_to(w, h); c.close_path(); c.fill()
    c.set_source_rgb(*hx('#F2E5CE')); c.move_to(300, h*.7); c.line_to(380, h*.6); c.line_to(460, h*.7); c.close_path(); c.fill()
    c.set_source_rgb(*hx('#F4B860')); c.move_to(365, h*.7); c.line_to(380, h*.64); c.line_to(395, h*.7); c.close_path(); c.fill()
    c.set_source_rgb(*hx('#2A1E3A'))
    for cx0, s in ((650, 1), (760, .85)):
        c.save(); c.translate(cx0, h*.66); c.scale(s, s)
        c.move_to(-50, 0); c.curve_to(-40, -40, -10, -50, 0, -30); c.curve_to(10, -50, 40, -40, 45, -10); c.line_to(70, -50); c.line_to(82, -46); c.line_to(55, 4)
        c.line_to(40, 50); c.line_to(32, 50); c.line_to(30, 6); c.line_to(-30, 6); c.line_to(-34, 50); c.line_to(-42, 50); c.close_path(); c.fill(); c.restore()

def mangroves(c, w, h):
    sky(c, w, h, '#F6EBDC', '#F7E3D2', h*.5)
    c.set_source_rgb(*hx('#3E6094')); c.rectangle(0, h*.5, w, h*.5); c.fill()
    c.set_source_rgb(*hx('#2B4A7C')); c.rectangle(0, h*.78, w, h*.22); c.fill()
    for x0, s in ((120, 1.2), (420, 1.0), (760, 1.3)):
        c.set_source_rgb(*hx('#4E6E4E')); c.arc(x0, h*.36, 110*s, 0, 2*math.pi); c.fill()
        c.set_source_rgb(*hx('#3F5E45')); c.arc(x0 + 60*s, h*.4, 80*s, 0, 2*math.pi); c.fill()
        c.set_source_rgb(*hx('#7A4D31')); c.set_line_width(12)
        for dx in (-50, -20, 20, 50): c.move_to(x0, h*.42); c.curve_to(x0 + dx*.5, h*.48, x0 + dx, h*.5, x0 + dx*1.3, h*.56); c.stroke()
    for fx, fy in ((290, .62), (560, .66), (690, .58)):  # flamingos
        c.save(); c.translate(fx, h*fy)
        c.set_source_rgb(*INK); c.set_line_width(5); c.move_to(-6, 20); c.line_to(-8, 120); c.move_to(8, 20); c.line_to(14, 120); c.stroke()
        c.set_source_rgb(*CORAL); c.save(); c.scale(1.5, 1); c.arc(0, 0, 36, 0, 2*math.pi); c.restore(); c.fill()
        c.set_line_width(13); c.set_line_cap(cairo.LINE_CAP_ROUND); c.move_to(40, -10); c.curve_to(76, -50, 30, -100, 56, -130); c.stroke()
        c.arc(60, -134, 15, 0, 2*math.pi); c.fill()
        c.set_source_rgb(*INK); c.move_to(70, -138); c.line_to(92, -128); c.line_to(72, -124); c.close_path(); c.fill()
        c.restore()

def coast(c, w, h):
    c.save(); c.scale(w / V.W, h / V.H); c.set_source_surface(V.art, 0, 0); c.paint(); c.restore()

# ---------- compositions ----------
def jigsaw_product(name, scene, cols, rows, bg, seed, angle=-2.5, loose=2, pw_=780, ph_=620):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, PWID, PHEI); c = cairo.Context(surf)
    c.set_source_rgb(*hx(bg)); c.paint()
    art = cairo.ImageSurface(cairo.FORMAT_ARGB32, pw_, ph_); ac = cairo.Context(art); scene(ac, pw_, ph_)
    paths = jig_paths(cols, rows, pw_, ph_, seed, min(pw_ / cols, ph_ / rows) * .78)
    rnd = random.Random(seed); keys = list(paths); rnd.shuffle(keys)
    edge_keys = [k for k in keys if 0 < k[0] < rows - 1 and 0 < k[1] < cols - 1]
    missing = edge_keys[:loose]
    ox, oy = (PWID - pw_) / 2, (PHEI - ph_) / 2 - 40
    c.save(); c.translate(PWID/2, oy + ph_/2); c.rotate(math.radians(angle)); c.translate(-pw_/2, -ph_/2)
    c.set_source_rgba(0.09, 0.12, 0.2, .10); c.rectangle(6, 12, pw_, ph_); c.fill()
    for k, p in paths.items():
        if k in missing: continue
        trace(c, p); c.save(); c.clip(); c.set_source_surface(art, 0, 0); c.paint(); c.restore()
    c.set_source_rgba(*INK, .22); c.set_line_width(1.2)
    for k, p in paths.items():
        if k in missing: continue
        trace(c, p)
    c.stroke(); c.restore()
    spots = [(220, oy + ph_ + 150, 18), (720, oy + ph_ + 120, -24), (520, oy + ph_ + 190, 8)]
    for (k, (sx, sy, rot)) in zip(missing, spots):
        p = paths[k]; cx = (k[1] + .5) * pw_ / cols; cy = (k[0] + .5) * ph_ / rows
        c.save(); c.translate(sx, sy); c.rotate(math.radians(rot)); c.translate(-cx, -cy)
        trace(c, p, 4, 8); c.set_source_rgba(0.09, 0.12, 0.2, .14); c.fill()
        trace(c, p); c.save(); c.clip(); c.set_source_surface(art, 0, 0); c.paint(); c.restore()
        trace(c, p); c.set_source_rgba(*INK, .25); c.set_line_width(1.2); c.stroke(); c.restore()
    save(surf, name)

def steel(c, x0, y0, x1, y1):
    g = cairo.LinearGradient(x0, y0, x1, y1)
    for t, col in ((0, '#6F7787'), (.25, '#D9DDE3'), (.45, '#9AA1AE'), (.6, '#EEF0F3'), (.8, '#8A92A0'), (1, '#C9CDD4')):
        g.add_color_stop_rgb(t, *hx(col))
    return g

def wire(c, draw, width=26):
    c.save(); draw(); c.set_line_width(width + 6); c.set_source_rgba(0.09, 0.12, 0.2, .12); c.translate(8, 14); c.restore()
    c.save(); c.translate(8, 14); draw(); c.set_line_width(width); c.set_line_cap(cairo.LINE_CAP_ROUND); c.set_source_rgba(0.09, 0.12, 0.2, .13); c.stroke(); c.restore()
    draw(); c.set_line_width(width); c.set_line_cap(cairo.LINE_CAP_ROUND); c.set_line_join(cairo.LINE_JOIN_ROUND)
    c.set_source(steel(c, 200, 300, 800, 900)); c.stroke_preserve()
    c.set_line_width(width * .28); c.set_source_rgba(1, 1, 1, .45); c.stroke()

def metal_product(name, kind, bg):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, PWID, PHEI); c = cairo.Context(surf)
    c.set_source_rgb(*hx(bg)); c.paint()
    c.set_source_rgba(*INK, .06); c.arc(PWID/2, PHEI/2, 360, 0, 2*math.pi); c.fill()
    cx, cy = PWID/2, PHEI/2
    if kind == 'crescent':
        def a(): c.new_path(); c.arc(cx - 90, cy, 190, math.radians(40), math.radians(320))
        def b(): c.new_path(); c.arc(cx + 90, cy, 190, math.radians(220), math.radians(140) + 2*math.pi)
        wire(c, a, 30); wire(c, b, 30)
        def a2(): c.new_path(); c.arc(cx - 90, cy, 190, math.radians(-40), math.radians(20))
        wire(c, a2, 30)
    elif kind == 'knot':
        def k():
            c.new_path(); n = 3
            for i in range(361):
                t = math.radians(i)
                r = 200 + 110 * math.cos(n * t)
                x, y = cx + r * math.cos(t) * 1.0, cy + r * math.sin(t) * 1.05
                c.line_to(x, y) if i else c.move_to(x, y)
            c.close_path()
        wire(c, k, 24)
        def ring(): c.new_path(); c.arc(cx + 150, cy + 210, 70, 0, 2*math.pi)
        wire(c, ring, 22)
    elif kind == 'palm':
        def ring(): c.new_path(); c.arc(cx, cy + 120, 230, 0, 2*math.pi)
        def stem():
            c.new_path(); c.move_to(cx, cy + 330); c.curve_to(cx + 20, cy + 150, cx - 20, cy - 20, cx, cy - 170)
            for ang in (-160, -125, -55, -20):
                a = math.radians(ang); c.move_to(cx, cy - 170)
                c.curve_to(cx + math.cos(a) * 80, cy - 170 + math.sin(a) * 80 - 40, cx + math.cos(a) * 170, cy - 170 + math.sin(a) * 60, cx + math.cos(a) * 210, cy - 120 + math.sin(a) * 40)
        wire(c, ring, 24); wire(c, stem, 22)
        def loop(): c.new_path(); c.arc(cx + 210, cy + 290, 60, 0, 2*math.pi)
        wire(c, loop, 20)
    save(surf, name)

def duo(name):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, PWID, PHEI); c = cairo.Context(surf)
    c.set_source_rgb(*hx('#EFE7DA')); c.paint()
    for (x, y, rot, scene) in ((110, 230, -5, dhows), (420, 520, 4, desert)):
        bw, bh = 470, 380
        art = cairo.ImageSurface(cairo.FORMAT_ARGB32, bw, bh); scene(cairo.Context(art), bw, bh)
        c.save(); c.translate(x + bw/2, y + bh/2); c.rotate(math.radians(rot)); c.translate(-bw/2, -bh/2)
        c.set_source_rgba(0.09, 0.12, 0.2, .14); c.rectangle(8, 14, bw, bh + 40); c.fill()
        c.set_source_rgb(*IVORY); c.rectangle(0, 0, bw, bh + 40); c.fill()
        c.set_source_surface(art, 0, 0); c.paint()
        c.set_source_rgb(*INK); c.rectangle(0, bh, bw, 40); c.fill()
        c.restore()
    def ring(): c.new_path(); c.arc(260, 1020, 80, 0, 2*math.pi)
    def ring2(): c.new_path(); c.arc(360, 1010, 80, math.radians(200), math.radians(520))
    wire(c, ring, 18); wire(c, ring2, 18)
    save(surf, name)

def save(surf, name):
    from PIL import Image
    p = os.path.join('/tmp', name + '.png'); surf.write_to_png(p)
    Image.open(p).convert('RGB').save(os.path.join(OUT, name + '.webp'), quality=80, method=6)

jigsaw_product('corniche-at-dusk', corniche, 10, 8, '#EEE6D8', 1)
jigsaw_product('old-town-wind-towers', windtowers, 8, 7, '#E9DCCB', 2, angle=2)
jigsaw_product('dhow-harbour', dhows, 10, 8, '#E4E8EE', 3)
jigsaw_product('desert-camp-night', desert, 9, 7, '#EFE3D6', 4, angle=1.5)
jigsaw_product('arabian-coastline', coast, 10, 8, '#EEE9DD', 5, angle=-1.5)
jigsaw_product('mangrove-morning-family', mangroves, 6, 5, '#F1E6D4', 6, angle=-3, loose=3)
metal_product('crescent-lock', 'crescent', '#ECE7DE')
metal_product('falcon-knot', 'knot', '#E3E6EC')
metal_product('palm-ring', 'palm', '#EFE5DA')
duo('weekend-duo')
