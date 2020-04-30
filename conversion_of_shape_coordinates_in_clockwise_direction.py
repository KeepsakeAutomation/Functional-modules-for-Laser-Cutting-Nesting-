def clockwise_list(list_shape2):
    j = 0
    list_shape1 = []
    for i in range(len(list_shape2)):                           # Check => shape co-ordinates are clockwise or anti-clockwise
        if i != len(list_shape2) - 1:
            j = j + ((list_shape2[i + 1][0] - list_shape2[i][0]) * (list_shape2[i + 1][1] + list_shape2[i][1]))
        else:
            j = j + ((list_shape2[i][0] - list_shape2[0][0]) * (list_shape2[i][1] + list_shape2[0][1]))
    if j > 0:                                                    # If shape co-ordinates are anti-clockwise then arrange it in clockwise
        list_shape1 = list_shape2
    else:
        for i in range(len(list_shape2)):
            list_shape1.append(
                list_shape2[len(list_shape2) - 1 - i])           # list_shape1 = clockwise arrangement of co-ordinates
    return list_shape1
