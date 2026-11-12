BIG_FONT = {
    "R": [
        " RRRR  ",
        " R   R ",
        " R   R ",
        " RRRR  ",
        " R R   ",
        " R  R  ",
        " R   R ",
    ],
    "T": [
        " TTTTT ",
        "   T   ",
        "   T   ",
        "   T   ",
        "   T   ",
        "   T   ",
        "   T   ",
    ],
    "H": [
        " H   H ",
        " H   H ",
        " H   H ",
        " HHHHH ",
        " H   H ",
        " H   H ",
        " H   H ",
    ],
    "S": [
        " SSSSS ",
        " S     ",
        " S     ",
        "  SSSS ",
        "     S ",
        "     S ",
        " SSSSS ",
    ],
    " ": [
        "   ",
        "   ",
        "   ",
        "   ",
        "   ",
        "   ",
        "   ",
    ]
}

def print_big(text):
    text = text.upper()
    lines = [""] * 7
    for ch in text:
        pattern = BIG_FONT.get(ch, BIG_FONT[" "])
        for i in range(7):
            lines[i] += pattern[i] + "  "
    for line in lines:
        print(line)


# Example
print_big("RTHS")