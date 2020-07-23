def area_at_the_left_of_given_piece(list_shape1, x, y):
    list = []
    list1 = [y, (0, y[1]), (0, x[1])]
    for i in range(len(list_shape1)):  # Fatchinf co_ordinates between leftmost high and leftmost low co-ordinates
        if list_shape1[i] == x:
            while i <= len(list_shape1):
                list.append(list_shape1[i])
                if list_shape1[i] == y:
                    break
                elif list_shape1[i] != y and i == len(list_shape1) - 1:
                    for j in range(len(list_shape1)):
                        if list_shape1 != y:
                            list.append(list_shape1[j])
                        if list_shape1[j] == y:
                            break
                    break
                i += 1
    for i in range(len(list) - 1):
        list1.append(list[i])
    return list1
