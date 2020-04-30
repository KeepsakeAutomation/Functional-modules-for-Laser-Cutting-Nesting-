def point_along_side(list, x, y):  # function for (if point is along the side)
    for i in range(int(len(list))):  # returns "False" if point is along the side
        if i != (len(list) - 1):
            if list[i + 1][1] == list[i][1]:
                if list[i][0] < list[i + 1][0]:
                    x1 = round(list[i][0], 2)
                    while round(x1, 2) != round(list[i + 1][0], 2):
                        x1 = round(x1, 2) + 0.01
                        if x1 == x and y == list[i][1]:
                            return False
                if list[i][0] > list[i + 1][0]:
                    x1 = round(list[i][0], 2)
                    while round(x1, 2) != round(list[i + 1][0], 2):
                        x1 = round(x1, 2) - 0.01
                        if x1 == x and y == list[i][1]:
                            return False
            elif list[i + 1][0] == list[i][0]:
                if list[i][1] < list[i + 1][1]:
                    y1 = round(list[i][1], 2)
                    while round(y1, 2) != round(list[i + 1][1], 2):
                        y1 = round(y1, 2) + 0.01
                        if y1 == y and x == list[i][0]:
                            return False
                elif list[i][1] > list[i + 1][1]:
                    y1 = round(list[i][1], 2)
                    while round(y1, 2) != round(list[i + 1][1], 2):
                        y1 = round(y1, 2) - 0.01
                        if y1 == y and x == list[i][0]:
                            return False
            if list[i + 1][1] != list[i][1] and list[i + 1][0] != list[i][0]:
                j1 = list[i][0]
                list1 = []
                if list[i][0] < list[i + 1][0]:
                    while round(j1, 2) != round(list[i + 1][0], 2):
                        list1.append(round(j1, 2))
                        j1 = round(j1, 2) + 0.01
                        list1.append(round(j1, 2))
                if list[i][0] > list[i + 1][0]:
                    while round(j1, 2) != round(list[i + 1][0], 2):
                        list1.append(round(j1, 2))
                        j1 = round(j1, 2) - 0.01
                        list1.append(round(j1, 2))
                m = (list[i + 1][1] - list[i][1]) / (list[i + 1][0] - list[i][0])
                c = list[i][1] - (m * list[i][0])
                for i in range(len(list1)):
                    y1 = (m * list1[i]) + c
                    if round(y1, 2) == y and list1[i] == x:
                        return False
        else:
            if list[0][1] == list[i][1]:
                if list[i][0] < list[0][0]:
                    x1 = round(list[i][0], 2)
                    while round(x1, 2) != round(list[0][0], 2):
                        x1 = round(x1, 2) + 0.01
                        if x1 == x and y == list[i][1]:
                            return False
                if list[i][0] > list[0][0]:
                    x1 = round(list[i][0], 2)
                    while round(x1, 2) != round(list[0][0], 2):
                        x1 = round(x1, 2) - 0.01
                        if x1 == x and y == list[i][1]:
                            return False
            if list[0][0] == list[i][0]:
                if list[i][1] < list[0][1]:
                    y1 = round(list[i][1], 2)
                    while round(y1, 2) != round(list[0][1], 2):
                        y1 = round(y1, 2) + 0.01
                        if y1 == y and x == list[i][0]:
                            return False
                if list[i][1] > list[0][1]:
                    y1 = round(list[i][1], 2)
                    while round(y1, 2) != round(list[0][1], 2):
                        y1 = round(y1, 2) - 0.01
                        if y1 == y and x == list[i][0]:
                            return False
            if list[0][1] != list[i][1] and list[0][0] != list[i][0]:
                j1 = list[i][0]
                list1 = []
                if list[i][0] < list[0][0]:
                    while round(j1, 2) != round(list[0][0], 2):
                        list1.append(round(j1, 2))
                        j1 = round(j1, 2) + 0.01
                        list1.append(round(j1, 2))
                if list[i][0] > list[0][0]:
                    while round(j1, 2) != round(list[0][0], 2):
                        list1.append(round(j1, 2))
                        j1 = round(j1, 2) - 0.01
                        list1.append(round(j1, 2))
                m = (list[0][1] - list[i][1]) / (list[0][0] - list[i][0])
                c = list[i][1] - (m * list[i][0])
                for i in range(len(list1)):
                    y1 = (m * list1[i]) + c
                    if y1 == y and list1[i] == x:
                        return False
    return True