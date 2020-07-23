def minimum_x_coordinate(list_shape1):  # get minimum x-coordinate of list_shap1
    for i in range(len(list_shape1)):
        if i == 0:
            min_x = list_shape1[0][0]
        else:
            if min_x >= list_shape1[i][0]:
                min_x = list_shape1[i][0]
    return min_x


def maximum_x_coordinate(list_1):   # get maximum x-coordinate of list_1
    for i in range(len(list_1)):
        if i == 0:
            max_x = list_1[0][0]
        else:
            if max_x <= list_1[i][0]:
                max_x = list_1[i][0]
    return max_x


def minimum_y_coordinate(list_2):       # get minimum y-coordinate of list2
    for i in range(len(list_2)):
        if i == 0:
            min_y = list_2[0][1]
        else:
            if min_y >= list_2[i][1]:
                min_y = list_2[i][1]
    return min_y


def maximum_y_coordinate(list_2):   # get maximum y-coordinate of list_2
    for i in range(len(list_2)):
        if i == 0:
            max_y = list_2[0][1]
        else:
            if max_y <= list_2[i][1]:
                max_y = list_2[i][1]
    return max_y
