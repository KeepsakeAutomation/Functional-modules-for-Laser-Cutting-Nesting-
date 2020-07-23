def D_function(list, p, x, y, count):  # function checks (if the point is inside the shape or not using maths formula)
    j = x  # returns "True" if point is inside the shape
    list3 = []
    list4 = []
    list3.append(j)
    while round(j, 2) != round(p, 2):
        j = round(j, 2) + 0.01
        list3.append(round(j, 2))
    for i1 in range(len(list)):
        for i2 in range(len(list3)):
            if list[i1][0] == list3[i2] and list[i1][1] == y:
                if list[i1] == list[0]:
                    d1 = ((x - p) * (y - list[len(list) - 1][1])) - ((y - y) * (x - list[len(list) - 1][0]))
                    d2 = ((x - p) * (y - list[i1 + 1][1])) - ((y - y) * (x - list[i1 + 1][0]))
                if list[i1] == list[len(list) - 1]:
                    d1 = ((x - p) * (y - list[i1 - 1][1])) - ((y - y) * (x - list[i1 - 1][0]))
                    d2 = ((x - p) * (y - list[0][1])) - ((y - y) * (x - list[0][0]))
                if list[i1] != list[0] and list[i1] != list[len(list) - 1]:
                    d1 = ((x - p)(y - list[i1 - 1][1])) - ((y - y)(x - list[i1 - 1][0]))
                    d2 = ((x - p)(y - list[i1 + 1][1])) - ((y - y)(x - list[i1 + 1][0]))
                if (d1 < 0 and d2 > 0) or (d1 > 0 and d2 < 0):
                    count = count + 1
        list3 = []
        list3.append(j)
        while round(j, 2) != round(p, 2):
            j = round(j, 2) + 0.01
            list3.append(round(j, 2))
        for i1 in range(len(list)):
            for i2 in range(len(list3)):
                if list[i1][0] == list3[i2] and list[i1][1] == y:
                    list4.append(list[i1])
                    count = count + 1
                    if len(list4) % 2 == 0:
                        count = count + 1
    if (count % 2) != 0:
        return True
    else:
        return False
