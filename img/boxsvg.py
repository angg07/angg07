"""Animated contribution-grid SVG for a GitHub profile.
Regenerate: python3 img/boxsvg.py ANGGA LARAVEL VUE+GO DOCKER > img/readmebox.svg"""
import sys, random
F = {  # 5x7 pixel font
'A':["01110","10001","10001","11111","10001","10001","10001"],'B':["11110","10001","11110","10001","10001","10001","11110"],
'C':["01111","10000","10000","10000","10000","10000","01111"],'D':["11110","10001","10001","10001","10001","10001","11110"],
'E':["11111","10000","11110","10000","10000","10000","11111"],'F':["11111","10000","11110","10000","10000","10000","10000"],
'G':["01111","10000","10000","10011","10001","10001","01111"],'H':["10001","10001","11111","10001","10001","10001","10001"],
'I':["11111","00100","00100","00100","00100","00100","11111"],'J':["00111","00010","00010","00010","00010","10010","01100"],
'K':["10001","10010","11100","10010","10001","10001","10001"],'L':["10000","10000","10000","10000","10000","10000","11111"],
'M':["10001","11011","10101","10101","10001","10001","10001"],'N':["10001","11001","10101","10011","10001","10001","10001"],
'O':["01110","10001","10001","10001","10001","10001","01110"],'P':["11110","10001","10001","11110","10000","10000","10000"],
'Q':["01110","10001","10001","10001","10101","10010","01101"],'R':["11110","10001","10001","11110","10010","10001","10001"],
'S':["01111","10000","01110","00001","00001","00001","11110"],'T':["11111","00100","00100","00100","00100","00100","00100"],
'U':["10001","10001","10001","10001","10001","10001","01110"],'V':["10001","10001","10001","10001","01010","01010","00100"],
'W':["10001","10001","10001","10101","10101","11011","10001"],'X':["10001","01010","00100","00100","01010","10001","10001"],
'Y':["10001","01010","00100","00100","00100","00100","00100"],'Z':["11111","00010","00100","01000","10000","10000","11111"],
'0':["01110","10011","10101","11001","10001","10001","01110"],'7':["11111","00001","00010","00100","01000","01000","01000"],
'+':["00000","00100","00100","11111","00100","00100","00000"],'-':["00000","00000","00000","11111","00000","00000","00000"],
' ':["000","000","000","000","000","000","000"],
}
HEART=["0110110","1111111","1111111","0111110","0011100","0001000"]
COLS, ROWS, CELL, GAP = 60, 16, 11, 3
STEP = CELL + GAP
W, H = COLS*STEP - GAP, ROWS*STEP - GAP
SHADES = ["#0e4429", "#006d32", "#26a641", "#39d353"]
random.seed(7)  # ponytail: fixed seed so the SVG is reproducible

def glyph_rows(word):
    rows = [""] * 7
    for ch in word.upper():
        g = F[ch]
        for i in range(7): rows[i] += g[i] + "0"
    return [r[:-1] for r in rows]

def cells(bitmap):
    h, w = len(bitmap), len(bitmap[0])
    assert w <= COLS, f"too wide: {w} cols > {COLS}"
    x0, y0 = (COLS - w)//2, (ROWS - h)//2
    return [(x0+x, y0+y) for y in range(h) for x in range(w) if bitmap[y][x] == "1"]

def svg(words):
    slides = [cells(glyph_rows(w)) for w in words] + [cells(HEART)]
    n, dur = len(slides), 2.5 * len(slides)
    seg = 100 / n
    css = [f".s{{opacity:0;transform-box:fill-box;transform-origin:center;animation:{dur}s infinite}}"]
    out = []
    for i, cs in enumerate(slides):
        a, b, c, d = i*seg, i*seg + seg*0.15, i*seg + seg*0.8, (i+1)*seg
        css.append(f".s{i}{{animation-name:k{i}}}@keyframes k{i}{{0%,{a:.2f}%{{opacity:0;transform:scale(.2) translateY(40px)}}"
                   f"{b:.2f}%,{c:.2f}%{{opacity:1;transform:scale(1)}}{d:.2f}%,100%{{opacity:0;transform:scale(1.1)}}}}")
        rects = "".join(f'<rect x="{x*STEP}" y="{y*STEP}" width="{CELL}" height="{CELL}" rx="2" fill="{random.choice(SHADES[1:])}"/>' for x, y in cs)
        out.append(f'<g class="s s{i}">{rects}</g>')
    bg = "".join(f'<rect x="{x*STEP}" y="{y*STEP}" width="{CELL}" height="{CELL}" rx="2"/>' for y in range(ROWS) for x in range(COLS))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<style>{"".join(css)}</style><rect width="{W}" height="{H}" fill="#0d1117"/>'
            f'<g fill="#161b22">{bg}</g>{"".join(out)}</svg>')

if __name__ == "__main__":
    print(svg(sys.argv[1:] or ["ANGGA", "LARAVEL", "VUE+GO", "DOCKER"]))
