from minimum_and_maximum_x_y_of_list import maximum_x_coordinate,minimum_y_coordinate,maximum_y_coordinate,minimum_x_coordinate




def arg_shapes(list2,length_sheet,width_sheet):
    list4 = []
    for i in range(len(list2)):
        list3 = []
        minimum_x = minimum_x_coordinate(list2[i])
        minimum_y = minimum_y_coordinate(list2[i])
        maximum_x = maximum_x_coordinate(list2[i])
        for j in range(len(list2[i])):
            a = (int(length_sheet) + (list2[i][j][0] - minimum_x)) - (maximum_x - minimum_x)
            b = list2[i][j][1] - minimum_y + int(width_sheet)
            c = a, b, 0
            list3.append(c)
        list4.append(list3)
    return list4
