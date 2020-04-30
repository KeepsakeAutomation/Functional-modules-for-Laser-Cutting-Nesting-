from calculation_for_point_inside_the_shape import D_function
from check_if_point_along_the_side_or_not import point_along_side
from check_if_side_intersects_segment_or_not import side_intersects_segment

def point_inside_the_shape(list_shape, x, y):                      # return "True" if point is inside the shape
    if point_along_side(list_shape, x, y) == True:
        M = 1000                                                    # point"(M,y)" where "M" is a very large number
        count = side_intersects_segment(list_shape, M, x, y)
        if count >= 0:
            return D_function(list_shape, M, x, y, count)
        else:
            return False
    else:
        return False
