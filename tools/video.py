"""Puzzlo hero: 100 interlocking pieces assemble an illustrated Arabian coastline.
Renders a seamless 6 s loop (empty board -> assembled -> empty board)."""
import cairo, math, random, subprocess, sys

W, H = 1000, 800
COLS, ROWS = 10, 10
PW, PH = W / COLS, H / ROWS
S = 80.0  # tab scale
FPS, DUR = 30, 6.0
NF = int(FPS * DUR)
random.seed(7)

INK = (0x18/255, 0x2C/255, 0x55/255)
IVORY = (0xF7/255, 0xF5/255, 0xEF/255)
CORAL = (0xD7/255, 0x6B/255, 0x55/255)
def hx(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16)/255 for i in (0,2,4))

# ---------------- illustration ----------------
def illustration():
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    c = cairo.Context(surf)
    # sky bands
    g = cairo.LinearGradient(0, 0, 0, 470)
    g.add_color_stop_rgb(0, *hx('#F3E7D6')); g.add_color_stop_rgb(1, *hx('#F6DCC7'))
    c.set_source(g); c.rectangle(0, 0, W, 480); c.fill()
    # sun with sliced lower half
    c.set_source_rgb(*CORAL); c.arc(660, 330, 96, 0, 2*math.pi); c.fill()
    c.set_source_rgb(*hx('#F6DCC7'))
    for y, h in ((352, 5), (374, 8), (398, 11), (414, 14)):
        c.rectangle(560, y, 200, h); c.fill()
    # flat clouds
    c.set_source_rgba(*IVORY, 0.9)
    for cx0, cy0, sc in ((170, 120, 1.0), (840, 150, 0.8), (520, 70, 0.55)):
        for dx, dy, rr in ((0, 0, 26), (30, -12, 32), (66, 0, 24), (-26, 6, 18)):
            c.arc(cx0 + dx * sc, cy0 + dy * sc, rr * sc, 0, 2 * math.pi); c.fill()
        c.rectangle(cx0 - 44 * sc, cy0, 134 * sc, 24 * sc); c.fill()
    # far mountains (Hajar silhouette)
    def ridge(pts, col):
        c.set_source_rgb(*hx(col)); c.move_to(0, 480)
        for x, y in pts: c.line_to(x, y)
        c.line_to(W, 480); c.close_path(); c.fill()
    ridge([(0,360),(90,330),(160,350),(250,300),(330,345),(420,330),(520,380),(620,372),(760,398),(880,360),(1000,385)], '#E9CDB6')
    ridge([(0,410),(120,392),(220,410),(300,385),(420,420),(560,430),(700,425),(840,410),(1000,425)], '#DFB99D')
    # sea
    c.set_source_rgb(*hx('#2B4A7C')); c.rectangle(0, 470, W, 200); c.fill()
    c.set_source_rgb(*hx('#3E6094')); c.rectangle(0, 470, W, 22); c.fill()
    c.set_source_rgb(*hx('#22406F')); c.rectangle(0, 560, W, 120); c.fill()
    # sun glints
    c.set_source_rgb(*CORAL)
    for i, (w, y) in enumerate(((120, 482), (84, 500), (140, 520), (60, 542), (100, 566), (40, 592))):
        c.rectangle(660 - w/2 + (i % 2) * 14, y, w, 4); c.fill()
    # wave dashes
    c.set_source_rgba(*IVORY, 0.55); c.set_line_width(3); c.set_line_cap(cairo.LINE_CAP_ROUND)
    rnd = random.Random(3)
    for _ in range(36):
        x = rnd.uniform(20, 980); y = rnd.uniform(500, 640); w = rnd.uniform(14, 40)
        if 560 < x < 760 and y < 600: continue
        c.move_to(x, y); c.line_to(x + w, y); c.stroke()
    # left town on a spit of land
    c.set_source_rgb(*hx('#E6CFAE')); c.move_to(0, 430); c.line_to(330, 440); c.curve_to(400, 446, 430, 470, 470, 488)
    c.line_to(0, 500); c.close_path(); c.fill()
    def building(x, y, w, h, wall, shade, tower=False, dome=False):
        c.set_source_rgb(*hx(wall)); c.rectangle(x, y - h, w, h); c.fill()
        c.set_source_rgb(*hx(shade)); c.rectangle(x + w * 0.72, y - h, w * 0.28, h); c.fill()
        c.set_source_rgb(*INK)
        for i in range(max(1, int(w // 26))):
            wx = x + 9 + i * 24
            if wx + 8 > x + w * 0.7: break
            c.rectangle(wx, y - h * 0.55, 8, 12); c.fill(); c.arc(wx + 4, y - h * 0.55, 4, math.pi, 0); c.fill()
        if tower:  # barjeel wind tower
            tw = 30; tx = x + w * 0.2
            c.set_source_rgb(*hx(wall)); c.rectangle(tx, y - h - 56, tw, 56); c.fill()
            c.set_source_rgb(*hx(shade)); c.rectangle(tx + tw * 0.7, y - h - 56, tw * 0.3, 56); c.fill()
            c.set_source_rgb(*INK)
            for k in range(3): c.rectangle(tx + 4 + k * 8, y - h - 48, 4, 26); c.fill()
            c.set_source_rgb(*hx(wall)); c.rectangle(tx - 3, y - h - 60, tw + 6, 6); c.fill()
        if dome:
            c.set_source_rgb(*hx(wall)); c.arc(x + w/2, y - h, w * 0.32, math.pi, 0); c.fill()
            c.set_source_rgb(*CORAL); c.rectangle(x + w/2 - 1.5, y - h - w*0.32 - 16, 3, 16); c.fill()
    building(20, 452, 96, 60, '#EFDFC4', '#D8BF98', tower=True)
    building(118, 456, 70, 92, '#EADAC0', '#CFB38A')
    c.set_source_rgb(*hx('#EADAC0')); c.rectangle(140, 300, 18, 70); c.fill()  # minaret
    c.set_source_rgb(*hx('#CFB38A')); c.rectangle(152, 300, 6, 70); c.fill()
    c.set_source_rgb(*hx('#EADAC0')); c.arc(149, 300, 11, math.pi, 0); c.fill()
    c.rectangle(136, 330, 26, 5); c.fill()
    building(190, 458, 110, 54, '#F1E3CB', '#D9C29C', dome=True)
    building(300, 462, 74, 70, '#EBD8B9', '#D2B68E', tower=True)
    building(374, 470, 54, 34, '#F0E1C6', '#D8BF98')
    # dhow
    c.save(); c.translate(500, 548)
    c.set_source_rgb(*hx('#8E5638'))
    c.move_to(-92, -18); c.line_to(96, -26); c.curve_to(80, 4, 40, 14, -40, 14); c.curve_to(-70, 10, -86, -2, -92, -18); c.close_path(); c.fill()
    c.set_source_rgb(*hx('#6E3F28')); c.rectangle(-60, -6, 130, 4); c.fill()
    c.set_source_rgb(*INK); c.set_line_width(4); c.move_to(4, -24); c.line_to(-6, -170); c.stroke()
    c.set_source_rgb(*IVORY); c.move_to(-4, -168); c.curve_to(40, -150, 84, -100, 92, -36); c.line_to(2, -36); c.close_path(); c.fill()
    c.set_source_rgb(*CORAL); c.move_to(-4, -168); c.line_to(6, -168); c.curve_to(48, -146, 86, -98, 92, -36); c.line_to(84, -36)
    c.curve_to(76, -96, 40, -142, -4, -168); c.close_path(); c.fill()
    c.restore()
    c.set_source_rgba(*IVORY, 0.6); c.set_line_width(3)
    for dx, w in ((-60, 70), (20, 90)): c.move_to(500 + dx, 572); c.line_to(500 + dx + w, 572); c.stroke()
    # tiny far boat
    c.set_source_rgb(*INK); c.move_to(880, 492); c.line_to(916, 490); c.line_to(910, 498); c.line_to(886, 498); c.close_path(); c.fill()
    c.set_source_rgb(*IVORY); c.move_to(896, 489); c.line_to(897, 466); c.line_to(912, 488); c.close_path(); c.fill()
    # beach
    c.set_source_rgb(*hx('#D7BB92')); c.move_to(0, 650); c.curve_to(260, 610, 520, 640, 760, 612); c.curve_to(860, 600, 940, 596, W, 600)
    c.line_to(W, H); c.line_to(0, H); c.close_path(); c.fill()
    c.set_source_rgba(*IVORY, 0.85); c.set_line_width(5)
    c.move_to(0, 652); c.curve_to(260, 612, 520, 642, 760, 614); c.curve_to(860, 602, 940, 598, W, 602); c.stroke()
    c.set_source_rgb(*hx('#E9D5B2')); c.move_to(0, 690); c.curve_to(300, 650, 560, 690, 780, 660); c.curve_to(880, 646, 950, 640, W, 642)
    c.line_to(W, H); c.line_to(0, H); c.close_path(); c.fill()
    c.set_source_rgb(*hx('#DFC59D'))
    for x, y, r in ((120, 740, 16), (150, 748, 10), (430, 760, 12), (640, 720, 8)):
        c.save(); c.translate(x, y); c.scale(1, 0.55); c.arc(0, 0, r, 0, 2*math.pi); c.restore(); c.fill()
    # palms
    def palm(bx, by, lean, height, scale):
        c.save(); c.set_line_cap(cairo.LINE_CAP_ROUND)
        tx, ty = bx + lean, by - height
        steps = 14
        for i in range(steps):
            t0, t1 = i / steps, (i + 1) / steps
            def pt(t): return (bx + lean * t * t, by - height * t)
            x0, y0 = pt(t0); x1, y1 = pt(t1)
            c.set_source_rgb(*hx('#8A5A3A' if i % 2 else '#7A4D31'))
            c.set_line_width(16 * scale * (1 - t0 * 0.45)); c.move_to(x0, y0); c.line_to(x1, y1); c.stroke()
        for ang, ln, col in ((-170, 150, '#3F5E45'), (-140, 135, '#4E6E4E'), (-105, 110, '#3F5E45'), (-60, 125, '#4E6E4E'),
                             (-25, 150, '#3F5E45'), (10, 135, '#4E6E4E'), (165, 120, '#4E6E4E'), (-200, 120, '#3F5E45')):
            a = math.radians(ang); L = ln * scale
            ex, ey = tx + math.cos(a) * L, ty + math.sin(a) * L + L * 0.35
            mx, my = tx + math.cos(a) * L * 0.5, ty + math.sin(a) * L * 0.5 - 18 * scale
            c.set_source_rgb(*hx(col)); c.set_line_width(2)
            c.move_to(tx, ty); c.curve_to(mx, my - 10 * scale, mx + 6, my + 6, ex, ey)
            c.curve_to(mx + 8, my + 22 * scale, mx, my + 8 * scale, tx, ty + 6 * scale); c.close_path(); c.fill()
        c.set_source_rgb(*hx('#6E4A2E'))
        for dx, dy in ((-6, 6), (6, 8), (0, 12)): c.arc(tx + dx * scale, ty + dy * scale, 6 * scale, 0, 2*math.pi); c.fill()
        c.restore()
    palm(905, 760, -70, 430, 1.0)
    palm(830, 772, 50, 330, 0.8)
    # birds
    c.set_source_rgb(*INK); c.set_line_width(2.6); c.set_line_cap(cairo.LINE_CAP_ROUND)
    for x, y, s in ((300, 170, 1.0), (340, 150, 0.8), (372, 186, 0.7)):
        c.move_to(x - 12 * s, y - 4 * s); c.curve_to(x - 6 * s, y - 9 * s, x - 2 * s, y - 4 * s, x, y)
        c.curve_to(x + 2 * s, y - 4 * s, x + 6 * s, y - 9 * s, x + 12 * s, y - 4 * s); c.stroke()
    return surf

# ---------------- jigsaw geometry ----------------
TAB = [((0.36, 0), (0.36, 0), (0.36, 0))]  # placeholder to show structure
def tab_segments(f, jitter, hs):
    # (t, n) in tab units of S around edge centre; f = +-1 direction
    pts = [
        ((-0.16, 0), (-0.10, 0), (-0.08, 0.05)),
        ((-0.05, 0.12), (-0.18, 0.20), (-0.13, 0.26)),
        ((-0.08, 0.34), (0.08, 0.34), (0.13, 0.26)),
        ((0.18, 0.20), (0.05, 0.12), (0.08, 0.05)),
        ((0.10, 0), (0.16, 0), (0.20, 0)),
    ]
    out = []
    for seg in pts:
        out.append(tuple(((t + jitter) * S, n * S * hs * f) for t, n in seg))
    return out

def make_edge(p0, p1, f, jitter, hs):
    (x0, y0), (x1, y1) = p0, p1
    L = math.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / L, (y1 - y0) / L
    nx, ny = -uy, ux
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    def P(t, n): return (cx + ux * t + nx * n, cy + uy * t + ny * n)
    segs = []
    start_t = -0.16 * S + jitter * S - 0.04 * S
    a = P(-0.20 * S + jitter * S, 0)
    segs.append(((x0, y0), a, a))  # straight lead (as degenerate cubic)
    for seg in tab_segments(f, jitter, hs):
        segs.append(tuple(P(t, n) for t, n in seg))
    segs.append((segs[-1][2], (x1, y1), (x1, y1)))
    return (x0, y0), segs

def straight(p0, p1): return p0, [(p0, p1, p1)]
def reverse(edge):
    start, segs = edge
    pts = [start]
    for s in segs: pts.append(s)
    out = []; cur = segs[-1][2]
    prev_ends = [start] + [s[2] for s in segs]
    for i in range(len(segs) - 1, -1, -1):
        c1, c2, _ = segs[i]
        out.append((c2, c1, prev_ends[i]))
    return cur, out

hedges = {}; vedges = {}
for r in range(1, ROWS):
    for col in range(COLS):
        p0 = (col * PW, r * PH); p1 = ((col + 1) * PW, r * PH)
        hedges[(r, col)] = make_edge(p0, p1, random.choice((-1, 1)), random.uniform(-0.05, 0.05), random.uniform(0.88, 1.04))
for col in range(1, COLS):
    for r in range(ROWS):
        p0 = (col * PW, r * PH); p1 = (col * PW, (r + 1) * PH)
        vedges[(r, col)] = make_edge(p0, p1, random.choice((-1, 1)), random.uniform(-0.05, 0.05), random.uniform(0.88, 1.04))

def piece_path(r, col):
    tl = (col * PW, r * PH); tr = ((col + 1) * PW, r * PH); br = ((col + 1) * PW, (r + 1) * PH); bl = (col * PW, (r + 1) * PH)
    top = hedges[(r, col)] if r > 0 else straight(tl, tr)
    right = vedges[(r, col + 1)] if col < COLS - 1 else straight(tr, br)
    bottom = reverse(hedges[(r + 1, col)]) if r < ROWS - 1 else straight(br, bl)
    left = reverse(vedges[(r, col)]) if col > 0 else straight(bl, tl)
    segs = top[1] + right[1] + bottom[1] + left[1]
    return tl, segs

def trace(c, path, dx=0, dy=0):
    (sx, sy), segs = path
    c.move_to(sx + dx, sy + dy)
    for (a, b, p) in segs:
        c.curve_to(a[0] + dx, a[1] + dy, b[0] + dx, b[1] + dy, p[0] + dx, p[1] + dy)
    c.close_path()

# ---------------- pieces ----------------
art = illustration()
PAD = 30
pieces = []
for r in range(ROWS):
    for col in range(COLS):
        path = piece_path(r, col)
        ox, oy = col * PW - PAD, r * PH - PAD
        sw, sh = int(PW + 2 * PAD), int(PH + 2 * PAD)
        ps = cairo.ImageSurface(cairo.FORMAT_ARGB32, sw, sh)
        pc = cairo.Context(ps)
        trace(pc, path, -ox, -oy); pc.clip()
        pc.set_source_surface(art, -ox, -oy); pc.paint()
        # order: diagonal reveal wave from bottom-left to top-right, with jitter
        order = (col / COLS) * 0.55 + ((ROWS - 1 - r) / ROWS) * 0.45 + random.uniform(-0.08, 0.08)
        side = random.choice('LRTB')
        if side == 'L': sx, sy = random.uniform(-260, -140), random.uniform(-100, H + 100)
        elif side == 'R': sx, sy = W + random.uniform(60, 180), random.uniform(-100, H + 100)
        elif side == 'T': sx, sy = random.uniform(-100, W + 100), random.uniform(-220, -120)
        else: sx, sy = random.uniform(-100, W + 100), H + random.uniform(40, 160)
        pieces.append(dict(r=r, col=col, path=path, surf=ps, ox=ox, oy=oy, cx=col * PW + PW / 2, cy=r * PH + PH / 2,
                           order=order, sx=sx, sy=sy, rot=math.radians(random.uniform(-70, 70)), dur=random.uniform(0.42, 0.58)))
orders = sorted(p['order'] for p in pieces); lo, hi = orders[0], orders[-1]
for p in pieces:
    p['t0'] = 0.12 + (p['order'] - lo) / (hi - lo) * 3.05      # all landed by ~3.75 s
    p['fade0'] = 5.05 + (p['order'] - lo) / (hi - lo) * 0.55   # exit wave 5.05 -> 6.0

def ease_out_back(t, s=1.25):
    t -= 1; return t * t * ((s + 1) * t + s) + 1
def ease_out_cubic(t): return 1 - (1 - t) ** 3
def smooth(t): t = max(0, min(1, t)); return t * t * (3 - 2 * t)

BOARD = hx('#ECE6DA')
def frame(t):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    c = cairo.Context(surf)
    c.set_source_rgb(*BOARD); c.paint()
    # ghost outlines on the mat
    c.set_source_rgba(*INK, 0.10); c.set_line_width(1.2)
    for p in pieces: trace(c, p['path'])
    c.stroke()
    seam_a = 0.28 - 0.18 * smooth((t - 3.9) / 0.8)
    moving = []
    for p in pieces:
        if t < p['t0']: continue
        k = min(1, (t - p['t0']) / p['dur'])
        alpha = 1 - smooth((t - p['fade0']) / 0.4)
        if alpha <= 0: continue
        e = ease_out_back(k) if k < 1 else 1
        pos = ease_out_cubic(k)
        x = p['sx'] + (p['cx'] - p['sx']) * pos
        y = p['sy'] + (p['cy'] - p['sy']) * pos
        rot = p['rot'] * (1 - e)
        sc = 1.06 - 0.06 * smooth(k) - 0.03 * (1 - alpha)
        lift = 1 - smooth(k)
        (moving if k < 1 else []).append(p)
        p['_st'] = (x, y, rot, sc, alpha, lift)
    def draw(p, shadow):
        x, y, rot, sc, alpha, lift = p['_st']
        c.save(); c.translate(x, y); c.rotate(rot); c.scale(sc, sc); c.translate(-p['cx'], -p['cy'])
        if shadow and lift > 0.02:
            trace(c, p['path'], 3 + 5 * lift, 5 + 8 * lift); c.set_source_rgba(0.09, 0.12, 0.2, 0.16 * lift * alpha); c.fill()
        c.set_source_surface(p['surf'], p['ox'], p['oy']); c.paint_with_alpha(alpha)
        trace(c, p['path']); c.set_source_rgba(*INK, (seam_a if lift < 0.02 else 0.35) * alpha); c.set_line_width(1.1); c.stroke()
        c.restore()
    placed = [p for p in pieces if t >= p['t0'] and p not in moving and '_st' in p and p['_st'][4] > 0]
    for p in placed: draw(p, False)
    for p in moving: draw(p, True)
    for p in pieces: p.pop('_st', None)
    return surf

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'poster':
        s = frame(4.8); s.write_to_png(sys.argv[2]); art.write_to_png(sys.argv[3])
    elif mode == 'test':
        for tt in (0.0, 1.2, 2.4, 3.2, 4.4, 5.5): frame(tt).write_to_png(f'/home/claude/build/f{tt:.1f}.png')
    else:
        out = sys.argv[2]
        ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'bgra', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                               '-c:v', 'ffv1', out], stdin=subprocess.PIPE)
        for i in range(NF):
            ff.stdin.write(bytes(frame(i / FPS).get_data()))
        ff.stdin.close(); ff.wait()
