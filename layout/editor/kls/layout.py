import math
from typing import List, NamedTuple


class CenteredLocation(NamedTuple):
    r: float
    cx: float
    cy: float


class KleLocation(NamedTuple):
    rx: float
    ry: float
    r: float
    x: float
    y: float

    @classmethod
    def from_center(cls, loc: CenteredLocation):
        # (r, cx, cy) -> (rx, ry, r, cx, cy) for KLE
        #
        # (rx, ry, r, x, y)
        #
        # <svg>
        #   <g transform="translate(rx ry) rotate(r) translate(x, y)">
        #     ...
        # |
        # V
        # <svg>
        #   <g transform="translate(cx cy) translate(0.5 0.5) rotate(r) translate(-0.5, -0.5)">
        #     ...
        # |
        # V
        rx = loc.cx + 0.5
        ry = loc.cy + 0.5
        r = loc.r
        x = -0.5
        y = -0.5
        return cls(rx, ry, r, x, y)

    def __str__(self) -> str:
        return f"{{rx:{self.rx}, ry:{self.ry}, r:{self.r}, x:{self.x}, y:{self.y}}}"


def layout() -> List[CenteredLocation]:
    locations = []

    radius0 = 6.5
    distance = 13
    for y in range(4):
        # image:
        #
        #    <--- u --->
        # A  +---------+
        # |  |         |
        # u  +    . <---- (x0, y0)  A
        # |  |         |            |
        # V  +---------+            |
        #    \         /            |
        #     \       /             radius
        #      \     /              |
        #       \   /               |
        #        \ /                |
        #         V <---- angle     V
        #
        radius = radius0 + (3 - y)
        angle = math.atan2(0.5, radius - 0.5) * 2
        cx: float
        cy: float
        for lr in ["L", "R"]:
            if lr == "L":
                for x in range(6):
                    if y == 3 and x < 3:
                        continue
                    r = angle * (x - 1) if x >= 2 else 0
                    if x == 0:
                        cx = 0
                        cy = y + 0.75
                    elif x == 1:
                        cx = 1
                        cy = y + 0.25
                    else:
                        cx = 1 + radius * math.sin(r)
                        cy = y + radius - radius * math.cos(r)
                    locations.append(CenteredLocation(math.degrees(r), cx, cy))
            elif lr == "R":
                for x in reversed(range(6)):
                    if y == 3 and x < 3:
                        continue
                    r = angle * (x - 1) if x >= 2 else 0
                    if x == 0:
                        cx = distance
                        cy = y + 0.75
                    elif x == 1:
                        cx = distance - 1
                        cy = y + 0.25
                    else:
                        cx = distance - 1 + radius * math.sin(-r)
                        cy = y + radius - radius * math.cos(-r)
                    locations.append(CenteredLocation(math.degrees(-r), cx, cy))

    return locations
