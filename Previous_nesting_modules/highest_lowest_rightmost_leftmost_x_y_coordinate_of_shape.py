def horizontal_checking(list_shape1):
    right_x1 = 0
    left_x1 = 0
    for x1 in range(len(list_shape1)):                  # Get the lowest y-coordinate of shape-1
        if x1 == 0:                                     # Get the highest y-coordinate of shape-1
            right_x1 = list_shape1[x1][0]
            a = list_shape1[0 + int(x1)]
            left_x1 = list_shape1[x1][0]
            b = list_shape1[0 + int(x1)]
        else:
            if list_shape1[x1][0] == right_x1:
                if list_shape1[x1][1] < a[1]:
                    a = list_shape1[0 + int(x1)]
            if list_shape1[x1][0] > right_x1:
                right_x1 = list_shape1[x1][0]
                a = list_shape1[0 + int(x1)]
            if list_shape1[x1][0] == left_x1:
                if list_shape1[x1][1] < b[1]:
                    b = list_shape1[0 + int(x1)]
            if list_shape1[x1][0] < left_x1:
                left_x1 = list_shape1[x1][0]
                b = list_shape1[0 + int(x1)]
    return b, a

def vertical_checking(list_shape1):
    high_y1 = 0
    low_y1 = 0
    for y1 in range(len(list_shape1)):                      # Get the lowest y-coordinate of shape-1
        if y1 == 0:                                         # Get the highest y-coordinate of shape-1
            high_y1 = list_shape1[y1][1]
            a = list_shape1[0 + int(y1)]
            low_y1 = list_shape1[y1][1]
            b = list_shape1[0 + int(y1)]
        else:
            if list_shape1[y1][1] == high_y1:
                if list_shape1[y1][0] < a[0]:
                    a = list_shape1[0 + int(y1)]
            if list_shape1[y1][1] > high_y1:
                high_y1 = list_shape1[y1][1]
                a = list_shape1[0 + int(y1)]
            if list_shape1[y1][1] == low_y1:
                if list_shape1[y1][0] < b[0]:
                    b = list_shape1[0 + int(y1)]
            if list_shape1[y1][1] < low_y1:
                low_y1 = list_shape1[y1][1]
                b = list_shape1[0 + int(y1)]
    return b, a
