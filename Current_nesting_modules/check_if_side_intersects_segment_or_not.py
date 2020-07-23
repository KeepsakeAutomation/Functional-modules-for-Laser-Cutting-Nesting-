
from checks_intrsection_of_two_segments import closed_segment_intersect

def side_intersects_segment(list_shape, p, x, y):  # function for (if side of shape intresects the segment(x,y),(M,y))
    count = 0  # returns "number of times the segment intersects the shape" if side of shape intersects the segment
    j = x
    list3 = []
    list3.append(j)
    c = (x, y)
    d = (p, y)
    for e1 in range(len(list_shape)):  # Creates the edges from co-ordinates of shape-1
        list4 = []
        if e1 == len(list_shape) - 1:
            a = list_shape[0 + int(e1)]
            b = list_shape[0]
        else:
            a = list_shape[0 + int(e1)]
            b = list_shape[1 + int(e1)]

        if closed_segment_intersect(a, b, c, d) == True:  # Checks the condition for intersection
            count = count + 1
        while round(j, 2) != round(p, 2):
            j = round(j, 2) + 0.01
            list3.append(round(j, 2))
        for i1 in range(len(list_shape)):
            for i2 in range(len(list3)):
                if list_shape[i1][0] == list3[i2] and list_shape[i1][1] == y:
                    list4.append(list_shape[i1])
                    count = count + 1
                    if len(list4) % 2 == 0:
                        count = count + 1

    if count < 0:
        count = 0
        return count
    else:
        return count
