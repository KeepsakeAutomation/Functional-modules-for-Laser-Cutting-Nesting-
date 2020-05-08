#length_sheet = 0
#width_sheet = 0

def horizontal_distance(px, py, x11, y11, x22, y22):  # Main function to determine the horizontal distance
    if (py < y11 and py < y22) or (py > y11 and py > y22):
        a = length_sheet  # "The point does not reach horizontally the segment"
        return a
    if (py == y11 and py == y22) and (px > x11 and px > x22):
        a = min(px - x11, px - x22)
        return a
    if (py == y11 and py == y22) and (px < x11 and px < x22):
        a = -(min((x11 - px), (x22 - px)))
        return a
    if (py == y11 and py == y22):
        return 0
    else:
        a = px - x11 + (x11 - x22) * (y11 - py) / (y11 - y22)
        return a

def vertical_distance(px, py, x11, y11, x22, y22):  # Main function to determine the horizontal distance
    if (px < x11 and px < x22) or (px > x11 and px > x22):
        a = width_sheet  # "The point does not reach horizontally the segment"
        return a
    if (px == x11 and px == x22) and (py > y11 and py > y22):
        a = min(py - y11, py - y22)
        return a
    if (px == x11 and px == x22) and (py < y11 and py < y22):
        a = -(min((y11 - py), (y22 - py)))
        return a
    if (px == x11 and px == x22):
        a = 0
        return a
    else:
        a = py - y11 + (y11 - y22) * (x11 - px) / (x11 - x22)
        return a
