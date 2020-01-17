# Position Meanings:
# 0 -> Hitted
# 1-24 -> On Board
# 25 -> Beared Off

# Backgammon board pattern is like this image:
# https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Bg-movement.svg/1024px-Bg-movement.svg.png


# start = 24 -> 1
# end   = 1 -> 24

home_start = [
    6,
    6,
    6,
    6,
    6,
    8,
    8,
    8,
    13,
    13,
    13,
    13,
    13,
    24,
    24,
]

home_end = [
    19,
    19,
    19,
    19,
    19,
    17,
    17,
    17,
    12,
    12,
    12,
    12,
    12,
    1,
    1,
]

# Default
black_home_start = {
    'black': home_start,
    'white': home_end,
}

black_home_end = {
    'black': home_end,
    'white': home_start,
}
