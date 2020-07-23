def area_at_the_bottom_of_given_piece(list_shape1, x, y):
    list = []
    list1 = [x, (x[0], 0), (y[0], 0)]
    for i in range(len(list_shape1)):                                # Fatching coordinates between leftmost high and leftmost low co-ordinates
        if list_shape1[i] == y:
            while i <= len(list_shape1):
                list.append(list_shape1[i])
                if list_shape1[i] == x:
                    break
                elif list_shape1[i] != x and i == len(list_shape1) - 1:
                    for j in range(len(list_shape1)):
                        if list_shape1 != x:
                            list.append(list_shape1[j])
                        if list_shape1[j] == x:
                            break
                    break
                i += 1
    for i in range(len(list) - 1):
        list1.append(list[i])
    return list1
