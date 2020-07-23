
def vertical_check(list_shape1, list_shape2):
    for y1 in range(len(list_shape1)):  # Get the lowest y-coordinate of shape-1
        if y1 == 0:  # Get the highest y-coordinate of shape-1
            high_y1 = list_shape1[y1][1]
            low_y1 = list_shape1[y1][1]
        else:
            if list_shape1[y1][1] > high_y1:
                high_y1 = list_shape1[y1][1]
            if list_shape1[y1][1] < low_y1:
                low_y1 = list_shape1[y1][1]

    for y2 in range(len(list_shape2)):  # Get the lowest y-coordinate of shape-2
        if y2 == 0:  # Get the highest y-coordinate of shape-2
            high_y2 = list_shape2[y2][1]
            low_y2 = list_shape2[y2][1]
        else:
            if list_shape2[y2][1] > high_y2:
                high_y2 = list_shape2[y2][1]
            if list_shape2[y2][1] < low_y2:
                low_y2 = list_shape2[y2][1]
    return high_y2, low_y2, high_y1, low_y1


def horizontal_check(list_shape1, list_shape2):
    for x1 in range(len(list_shape1)):  # Get the leftmost x-coordinate of shape-1
        if x1 == 0:  # Get the rightmost x-coordinate of shape-1
            right_x1 = list_shape1[x1][0]
            left_x1 = list_shape1[x1][0]
        else:
            if list_shape1[x1][0] > right_x1:
                right_x1 = list_shape1[x1][0]
            if list_shape1[x1][0] < left_x1:
                left_x1 = list_shape1[x1][0]

    for x2 in range(len(list_shape2)):  # Get the leftmost x-coordinate of shape-2
        if x2 == 0:  # Get the rightmost x-coordinate of shape-2
            right_x2 = list_shape2[x2][0]
            left_x2 = list_shape2[x2][0]
        else:
            if list_shape2[x2][0] > right_x2:
                right_x2 = list_shape2[x2][0]
            if list_shape2[x2][0] < left_x2:
                left_x2 = list_shape2[x2][0]
    return right_x2, left_x2, right_x1, left_x1
