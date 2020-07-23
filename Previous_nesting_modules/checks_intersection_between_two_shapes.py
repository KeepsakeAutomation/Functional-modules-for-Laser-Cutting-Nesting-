from checks_intrsection_of_two_segments import closed_segment_intersect

def intersection_of_shapes(list_shape1, list_shape2):
    if (list_shape1 == list_shape2):
        return True
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

    if low_y1 > high_y2 or low_y2 > high_y1:  # Checks the condition for intersection
        return False

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

    if left_x1 > right_x2 or left_x2 > right_x1:  # Checks the condition for intersection
        return False

    for e1 in range(len(list_shape1)):  # Creates the edges from co-ordinates of shape-1
        if e1 == len(list_shape1) - 1:
            a = list_shape1[0 + int(e1)]
            b = list_shape1[0]
        else:
            a = list_shape1[0 + int(e1)]
            b = list_shape1[1 + int(e1)]
        for e2 in range(len(list_shape2)):  # Creates the edges from co-ordinates of shape-2
            if e2 == len(list_shape2) - 1:
                c = list_shape2[0 + int(e2)]
                d = list_shape2[0]
            else:
                c = list_shape2[0 + int(e2)]
                d = list_shape2[1 + int(e2)]
            if (closed_segment_intersect(a, b, c, d) == True):
                return True
                break
    if (closed_segment_intersect(a, b, c, d) == True):  # Checks the condition for intersection
        return True
    else:
        return False
