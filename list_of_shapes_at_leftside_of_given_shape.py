from conversion_of_shape_coordinates_in_clockwise_direction import clockwise_list
from checks_intersection_between_two_shapes import intersection_of_shapes
from checks_if_point_inside_the_shape_or_not import point_inside_the_shape

def formation_of_set_S_horizontal(list_left, S1, list_shape1):   # get list of shapes which are already placed left side of given shape
    list_shape3 = []
    for g in range(len(list_left)):
        if g > 2:
            list_shape3.append(list_left[g])
    list_shape3.append(list_left[0])
    list_shape3 = clockwise_list(list_shape3)
    S = []
    for i in range(len(S1)):
        S2 = []
        if intersection_of_shapes(list_left, S1[i]) == True and intersection_of_shapes(list_shape1, S1[i]) == False:
            if S1[i] != list_shape1:
                S.append(S1[i])
        for j in range(len(S1[i])):
            if point_inside_the_shape(list_left, S1[i][j][0], S1[i][j][1]) == True and point_inside_the_shape(
                    list_shape1, S1[i][j][0], S1[i][j][1]) == False:
                S3 = S1[i][j][0], S1[i][j][1]
                S2.append(S3)
            if S2 == S1[i]:
                S.append(S1[i])
    return S, list_shape3