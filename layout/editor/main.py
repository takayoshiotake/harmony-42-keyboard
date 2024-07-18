import os

import kls


def svg_key_element(
    loc: kls.CenteredLocation,
    dx: float = 0,
    dy: float = 0,
    unit_size: float = 1,
    key_size: float = 18 / 19.05,
    key_r: float = 1 / 19.05,
    width: float = 0.2 / 19.05,
) -> str:
    key_size *= unit_size
    key_r *= unit_size
    width *= unit_size
    return f"""\
<g transform="translate({dx + loc.cx * unit_size},{dy + loc.cy * unit_size}) translate({0.5 * unit_size}, {0.5 * unit_size}) rotate({loc.r})">
    <rect fill="none" stroke="magenta" stroke-width="{width}" transform="translate({-0.5 * unit_size},{-0.5 * unit_size})" x="0" y="0" width="{unit_size}" height="{unit_size}" />
    <rect fill="none" rx="{key_r}" stroke="black" stroke-width="{width}" transform="translate({-0.5 * key_size},{-0.5 * key_size})" x="0" y="0" width="{key_size}" height="{key_size}" />
    <rect fill="none" stroke="#00FF00" stroke-width="{width}" transform="translate({-7},{-7})" x="0" y="0" width="14" height="14" />
</g>"""


locations = kls.layout()

os.makedirs("out", exist_ok=True)

with open("out/locations.csv", "w") as f:
    print("r, cx, cy", file=f)
    for loc in locations:
        print(f"{loc.r}, {loc.cx}, {loc.cy}", file=f)
    print(f"Written: {f.name}")

with open("out/locations-pcb.csv", "w") as f:
    print("r, cx, cy", file=f)
    for loc in locations:
        print(f"{loc.r}, {(loc.cx + 2) * 19.05}, {(loc.cy + 2) * 19.05}", file=f)
    print(f"Written: {f.name}")

kle_locations = list(map(lambda it: kls.KleLocation.from_center(it), locations))

with open("out/keyboard-layout.rawdata.json", "w") as f:
    for i, kle_loc in enumerate(kle_locations):
        legend = f"{i + 1}"
        print(f'[{kle_loc}, "{legend}"],', file=f)
    print(f"Written: {f.name}")

with open("out/keyboard-layout.svg", "w") as f:
    print(
        """\
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="297mm" height="210mm" viewPort="0 0 297mm 210mm" viewBox="0 0 297 210">""",
        file=f,
    )
    for i, loc in enumerate(locations):
        print(
            svg_key_element(loc, dx=19.05, dy=19.05, unit_size=19.05, key_r=4 / 19.05),
            file=f,
        )
    print("""</svg>""", file=f)
    print(f"Written: {f.name}")
