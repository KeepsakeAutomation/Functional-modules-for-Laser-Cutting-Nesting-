# ---------------------------------------------------------------------------------------------------------------#
# MAIN CODE FOR CREATING THE SHAPES AS WELL AS NESTING THOSE SHAPES
# ---------------------------------------------------------------------------------------------------------------#

# ---------------------------------------------------------------------------------------------------------------#
#Brief: The code takes the user input by taking the dimensions of the shapes and nests those shapes into a sheet in the best way possible.

#Importing the required libraries and external functions from other files
from math import sqrt, sin, cos, pi, asin
import time, sys, winsound
from highest_lowest_rightmost_leftmost_x_y_coordinate_of_shape import horizontal_checking , vertical_checking
from conversion_of_shape_coordinates_in_clockwise_direction import clockwise_list
from area_at_the_bottom_of_shape import area_at_the_bottom_of_given_piece
from calculation_of_horizontal_and_vertical_distance import horizontal_distance , vertical_distance
from area_at_the_left_side_of_shape import area_at_the_left_of_given_piece
from check_if_point_along_the_side_or_not import point_along_side
from check_if_side_intersects_segment_or_not import side_intersects_segment
from calculation_for_point_inside_the_shape import D_function
from check_if_point_in_closed_segment_or_not import is_point_in_closed_segment
from checks_intrsection_of_two_segments import side , closed_segment_intersect
from highest_lowest_y_and_rightmost_leftmost_x_of_two_shapes import vertical_check , horizontal_check
from checks_intersection_between_two_shapes import intersection_of_shapes
from checks_if_point_inside_the_shape_or_not import point_inside_the_shape
from minimum_and_maximum_x_y_of_list import minimum_x_coordinate , maximum_y_coordinate , maximum_x_coordinate , minimum_y_coordinate
from list_of_shape_below_the_given_shape import formation_of_set_S_vertical
from list_of_shapes_at_leftside_of_given_shape import formation_of_set_S_horizontal
from progress_in_percentage_and_beep_sound import update_progress , beep_sound

# ---------------------------------------------------------------------------------------------------------------#
#PART-1: CREATING THE SHAPES AND SHEET WITH THE HELP OF THEIR DIMENSIONS
# ---------------------------------------------------------------------------------------------------------------#

# Developing the sheet through its dimensions
length_sheet = float(input("Enter the length for sheet: "))
width_sheet = float(input("Enter the width for sheet: "))
vertices_sheet = [(0, 0, 0), (int(length_sheet), 0, 0), (int(length_sheet), (int(width_sheet)), 0),
                  (0, (int(width_sheet)), 0)]
sheet_area = 0
for i in range(len(vertices_sheet)):
    if i <= (len(vertices_sheet) - 2):
        b = (vertices_sheet[i + 1][1] + vertices_sheet[i][1]) / 2
        e = vertices_sheet[i + 1][0] - vertices_sheet[i][0]
        sheet_area = sheet_area + (b * e)
    else:
        b = (vertices_sheet[i][1] + vertices_sheet[0][1]) / 2
        e = vertices_sheet[0][0] - vertices_sheet[i][0]
        sheet_area = sheet_area + (b * e)
    area_of_sheet = abs(sheet_area)  # area of piece after calculation
print("area of sheet:", area_of_sheet)

# Developing the shapes through their dimensions
number_shape = input("Enter the number of shapes you want to form: ")
no_shape = 0
if number_shape.isnumeric() == False or int(number_shape) < 0: #Checking whether the number is numeric or not
    print("Please enter only positive value")
vertices_shapes = []
vertices_for_other_shapes = []
while (int(number_shape) != no_shape):
    type_shape = input(
        "Choose the shape: 1.Circle 2.Triangle 3.Square 4.Rectangle 5.Regular Pentagon 6.Regular Hexagon 7.Polygon: ")
    type_sh = int(type_shape)
    if type_shape.isnumeric() == False or int(type_shape) < 0:
        print("Please enter only positive value")

    if type_sh == 1: # Developing a circle
        Circle_shape = []
        radius = float(input("Enter the radius: "))
        area_through_radius = (pi * radius * radius)
        angle = 1
        times = 360 / angle
        x = radius
        y = radius
        theta = 0
        circle_area = 0
        # Developing a polygon which contains 360 sides and also resembles circle completely
        for i in range(int(times)):
            point_circle = (round(int(length_sheet) + (x + ((radius) * sin(theta * (pi / 180)))) - (2 * radius), 6),
                            round(int(width_sheet) + (y + ((radius) * cos(theta * (pi / 180)))), 6), 0)
            Circle_shape.append(point_circle)
            theta = theta + angle
        vertices_for_other_shapes.append(Circle_shape)
        no_shape = no_shape + 1
    elif type_sh == 2: # Developing a triangle
        temp1_triangle = float(input("Enter length-1 of Triangle: "))
        temp2_triangle = float(input("Enter length-2 of Triangle: "))
        temp3_triangle = float(input("Enter length-3 of Triangle: "))
        var_d = temp1_triangle + temp2_triangle
        var_e = temp2_triangle + temp3_triangle
        var_f = temp3_triangle + temp1_triangle
        #To check whether the triangle is valid or not
        if var_d > temp3_triangle and var_e > temp1_triangle and var_f > temp2_triangle:
        #Calculations for triangle
            # Equilateral Triangle
            if temp1_triangle == temp2_triangle == temp3_triangle:
                Triangle_shape = [(int(length_sheet) - temp2_triangle, int(width_sheet), 0),
                                  (int(length_sheet), int(width_sheet), 0), (
                                      (int(length_sheet) + round((temp1_triangle / 2), 2)) - temp2_triangle,
                                      round(sqrt((temp1_triangle * 2) - ((temp1_triangle / 2) * 2)), 2) + int(
                                          width_sheet),
                                      0)]
                vertices_shapes.append(Triangle_shape)
            # Isosceles Triangle
            elif temp1_triangle == temp2_triangle or temp2_triangle == temp3_triangle or temp3_triangle == temp1_triangle:
                if temp1_triangle == temp3_triangle:
                    var_t2 = temp2_triangle
                    var_t1 = temp1_triangle
                elif temp1_triangle == temp2_triangle:
                    var_t2 = temp3_triangle
                    var_t1 = temp2_triangle
                else:
                    var_t2 = temp1_triangle
                    var_t1 = temp3_triangle
                # Isosceles Triangle's calculations
                Triangle_shape = [(int(length_sheet) - var_t2, int(width_sheet), 0),
                                  (int(length_sheet), int(width_sheet), 0), (
                                      (int(length_sheet) + (var_t2 / 2)) - var_t2,
                                      round(sqrt((var_t1 * var_t1) - ((var_t2 / 2) * (var_t2 / 2))), 2) + int(
                                          width_sheet),
                                      0)]
                vertices_shapes.append(Triangle_shape)
            # Scalene Triangle
            else:
                if temp2_triangle > temp1_triangle and temp2_triangle > temp3_triangle:
                    var_t1 = temp1_triangle
                    var_t2 = temp2_triangle
                    var_t3 = temp3_triangle
                elif temp1_triangle > temp3_triangle and temp1_triangle > temp2_triangle:
                    var_t2 = temp1_triangle
                    var_t1 = temp3_triangle
                    var_t3 = temp2_triangle
                else:
                    var_t2 = temp3_triangle
                    var_t1 = temp1_triangle
                    var_t3 = temp2_triangle
                # Scalene Triangle's calculations
                S = (var_t1 + var_t2 + var_t3) / 2
                A = sqrt(S * (S - var_t1) * (S - var_t2) * (S - var_t3))
                H = round((2 * A) / var_t2, 2)
                G = asin(H / var_t1)
                F = round(var_t1 * cos(G), 2)
                E = asin(H / var_t3)
                I = var_t3 * cos(E)
                W = round(((F + I) - var_t2) / 2, 2)
                R = F - W
                X = sqrt((var_t1 * var_t1) - (R * R))
                T = round(X - H, 2)
                Triangle_shape = [(int(length_sheet) - var_t2, int(width_sheet), 0),
                                  (int(length_sheet), int(width_sheet), 0),
                                  ((int(length_sheet) + (F - W)) - var_t2, int(width_sheet) + (H + T), 0)]
                vertices_shapes.append(Triangle_shape)
            no_shape = no_shape + 1
        else:
            print("\nEnter the correct length for triangle")
    elif type_sh == 3: # Developing a square
        Square = float(input("Enter length of square: "))
        #Calculations for square
        Square_shape = [(int(length_sheet) - Square, int(width_sheet), 0),
                        (int(length_sheet) - Square, Square + int(width_sheet), 0),
                        (int(length_sheet), Square + int(width_sheet), 0), (int(length_sheet), int(width_sheet), 0)]
        vertices_shapes.append(Square_shape)
        no_shape = no_shape + 1
    elif type_sh == 4: #Develpoing a rectangle
        Rect_length = float(input("Enter length of rectangle: "))
        Rect_width = float(input("Enter width of rectangle: "))
        #Calculation for rectangle
        Rectangle_shape = [(int(length_sheet) - Rect_length, int(width_sheet), 0),
                           (int(length_sheet) - Rect_length, Rect_width + int(width_sheet), 0),
                           (int(length_sheet), Rect_width + int(width_sheet), 0),
                           (int(length_sheet), int(width_sheet), 0)]
        vertices_shapes.append(Rectangle_shape)
        no_shape = no_shape + 1
    elif type_sh == 5: #Developing a pentagon
        length_Pentagon = float(input("Enter the length of pentagon: "))
        #Calculation for pentagon
        Pentagon_shape = [(int(length_sheet) + (round(length_Pentagon * cos((2 * pi) / 5), 2)) - (
            round((2 * length_Pentagon * cos((2 * pi) / 5)) + length_Pentagon, 2)), int(width_sheet), 0),
                          ((int(length_sheet) + (round((length_Pentagon * cos((2 * pi) / 5)), 2) + length_Pentagon)) - (
                              round((2 * length_Pentagon * cos((2 * pi) / 5)) + length_Pentagon, 2)), int(width_sheet),
                           0),
                          (int(length_sheet), round(length_Pentagon * sin((2 * pi) / 5), 2) + int(width_sheet), 0),
                          ((int(length_sheet) + round((length_Pentagon * cos((2 * pi) / 5)) + (length_Pentagon / 2),
                                                      2)) - (
                               round((2 * length_Pentagon * cos((2 * pi) / 5)) + length_Pentagon, 2)),
                           round((length_Pentagon * sin((2 * pi) / 5)) + (length_Pentagon * cos(pi / 3.33)), 2) + int(
                               width_sheet), 0),
                          (int(length_sheet) - (round((2 * length_Pentagon * cos((2 * pi) / 5)) + length_Pentagon, 2)),
                           round(length_Pentagon * sin((2 * pi) / 5), 2) + int(width_sheet), 0)]
        vertices_shapes.append(Pentagon_shape)
        no_shape = no_shape + 1
    elif type_sh == 6: #Developing a hexagon
        length_Hexagon = float(input("Enter the length of hexagon: "))  
        #Calculations for hexagon
        Hexagon_shape = [(int(length_sheet) + (round(length_Hexagon * cos(pi / 6), 2)) - (
            round(length_Hexagon * 2 * cos(pi / 6), 2)), int(width_sheet), 0),
                         (int(length_sheet), round(length_Hexagon * sin(pi / 6), 2) + int(width_sheet), 0),
                         (int(length_sheet),
                          round((length_Hexagon * sin(pi / 6)) + length_Hexagon, 2) + int(width_sheet), 0),
                         ((int(length_sheet) + round(length_Hexagon * cos(pi / 6), 2)) - (
                             round(length_Hexagon * 2 * cos(pi / 6), 2)),
                          round(((length_Hexagon * sin(pi / 6)) + length_Hexagon) + (length_Hexagon * sin(pi / 6)),
                                2) + int(width_sheet), 0),
                         (int(length_sheet) - (round(length_Hexagon * 2 * cos(pi / 6), 2)),
                          round(length_Hexagon * sin(pi / 6) + length_Hexagon, 2) + int(width_sheet), 0),
                         (int(length_sheet) - (round(length_Hexagon * 2 * cos(pi / 6), 2)),
                          round(length_Hexagon * sin(pi / 6), 2) + int(width_sheet), 0)]
        vertices_shapes.append(Hexagon_shape)
        no_shape = no_shape + 1
    else: #Developing a polygon with given amount of vertices
        Polygon_shape = []
        Polygon_shape_final = []
        no_polygon = 0
        polygon_vertices = input("enter the total vertices of polygon: ")
        #Calculations for polygon
        while (int(polygon_vertices) != no_polygon):
            X_co_ordinate = input("Enter the value of X-Co-ordinate: ")
            Y_co_ordinate = input("Enter the value of Y-Co-ordinate: ")
            Polygon_shape.insert(no_polygon, (float(X_co_ordinate), float(Y_co_ordinate), 0))
            no_polygon = no_polygon + 1

        minimum_x = minimum_x_coordinate(Polygon_shape)
        maximum_x = maximum_x_coordinate(Polygon_shape)
        minimum_y = minimum_y_coordinate(Polygon_shape)
        #Putting a polygon to the upper-right corner of the sheet
        for i in range(len(Polygon_shape)):
            origin = (int(length_sheet) + (Polygon_shape[i][0] - minimum_x)) - (maximum_x - minimum_x), \
                     Polygon_shape[i][1] - minimum_y + int(width_sheet), 0
            Polygon_shape_final.append(origin)

        vertices_shapes.append(Polygon_shape_final)
        no_shape = no_shape + 1

# ---------------------------------------------------------------------------------------------------------------#

#Sorting the shapes formed as well as making them ready for nesting
unsorted_shapes_area = []
sorted_shapes_area = []
index_area = []
vertices_in_decreasing_order = []
#Loop for sorting the shapes according to their areas in descending order
for i in range(len(vertices_shapes)):
    area = 0
    for j in range(len(vertices_shapes[i])):
        if j <= (len(vertices_shapes[i]) - 2):
            var_a = (vertices_shapes[i][j + 1][1] + vertices_shapes[i][j][1]) / 2
            var_b = vertices_shapes[i][j + 1][0] - vertices_shapes[i][j][0]
            area = area + (var_a * var_b)
        else:
            var_a = (vertices_shapes[i][j][1] + vertices_shapes[i][0][1]) / 2
            var_b = vertices_shapes[i][0][0] - vertices_shapes[i][j][0]
            area = area + (var_a * var_b)
            area = round(area, 2)
    sorted_shapes_area.append(abs(area))
    unsorted_shapes_area.append(abs(area))

#Finding the index of a shape to sort it by its area
for i in range(len(sorted_shapes_area)):
    for j in range(len(sorted_shapes_area)):
        if sorted_shapes_area[i] > sorted_shapes_area[j]:
            a = sorted_shapes_area[i]
            sorted_shapes_area[i] = sorted_shapes_area[j]
            sorted_shapes_area[j] = a

for i in range(len(sorted_shapes_area)):
    b = sorted_shapes_area[i]
    for j in range(len(unsorted_shapes_area)):
        c = unsorted_shapes_area[j]
        if b == c and j not in index_area:
            index_area.append(j)


#Arranging the vertices of the shapes in the descending order with the help of area and indices
for i in range(len(index_area)):
    index = index_area[i]
    vertices_in_decreasing_order.append(vertices_shapes[index])

print("-----------------------------------------------")

# ---------------------------------------------------------------------------------------------------------------#
#PART-2 NESTING THE SHAPES CREATED AS PER THEIR DIMENSIONS AND SIZES
# ---------------------------------------------------------------------------------------------------------------#

#Currently, all of the shapes are placed on the top-right corner outside and above the sheet
#It take some time for shapes to be nested due to extensive checking and proper placement
progress_for_shape = 0
new_vertices_shapes = []
invalid_shapes = []
#To take the shapes one-by-one and start nesting them
for i in range(len(vertices_in_decreasing_order)):
    shape_to_move_vertically = []
    shape_to_move_horizontally = []
    nested_shape = []
    intersection_with_previous_shapes = 0
    shape_to_move_vertically = vertices_in_decreasing_order[i]

    #For moving the shape in the vertical direction from its current position
    shape_to_move_vertically_clockwise = clockwise_list(shape_to_move_vertically)
    leftmost_xy, rightmost_xy = horizontal_checking(shape_to_move_vertically_clockwise)
    list_bottom = area_at_the_bottom_of_given_piece(shape_to_move_vertically_clockwise, leftmost_xy, rightmost_xy)
    shapes_at_the_bottom, list_shape3 = formation_of_set_S_vertical(list_bottom, new_vertices_shapes,
                                                                    shape_to_move_vertically_clockwise)
    
    #The shape with the vertical movememt requires to check other shapes present in its bottom. Hence, their maximum-y is calculated
    maximum_y = 0
    for j in range(len(shapes_at_the_bottom)):
        maximum_y_compare = maximum_y_coordinate(shapes_at_the_bottom[j])
        if maximum_y_compare > maximum_y:
            maximum_y = maximum_y_compare

    #The shape's vertices are moved vertically after above calculations
    vertical_movement = width_sheet - maximum_y
    for j in range(len(shape_to_move_vertically)):
        k = shape_to_move_vertically[j][0]
        l = shape_to_move_vertically[j][1] - vertical_movement + 1
        shape_to_move_horizontally.append((round(k, 2), round(l, 2), 0))

    # For moving the shape in the horizontal direction from its current position
    shape_to_move_horizontally_clockwise = clockwise_list(shape_to_move_horizontally)
    leftmin_x, leftmax_y = vertical_checking(shape_to_move_horizontally_clockwise)
    list_left = area_at_the_left_of_given_piece(shape_to_move_horizontally_clockwise, leftmin_x, leftmax_y)
    shapes_at_the_left, list_shape3 = formation_of_set_S_horizontal(list_left, new_vertices_shapes,
                                                                    shape_to_move_horizontally_clockwise)
    
    #The shape with the horizontal movememt requires to check other shapes present in its left. Hence, their maximum-x is calculated
    maximum_x = 0
    for j in range(len(shapes_at_the_left)):
        maximum_x_compare = maximum_x_coordinate(shapes_at_the_left[j])
        if maximum_x_compare > maximum_x:
            maximum_x = maximum_x_compare
    if maximum_x == 0:
        horizontal_movement = minimum_x_coordinate(shape_to_move_horizontally_clockwise)
    else:
        horizontal_movement = minimum_x_coordinate(shape_to_move_horizontally_clockwise) - maximum_x
    shape_to_move_vertically = []
    #The shape's vertices are moved horizontally after above calculations
    for j in range(len(shape_to_move_horizontally)):
        k = shape_to_move_horizontally[j][0] - horizontal_movement + 1
        l = shape_to_move_horizontally[j][1]
        shape_to_move_vertically.append((round(k, 2), round(l, 2), 0))

    # To ensure proper and complete nesting, the shapes are moved vertically, again
    
    #For moving the shape in the vertical direction from its current position
    shape_to_move_vertically_clockwise = clockwise_list(shape_to_move_vertically)
    leftmost_xy, rightmost_xy = horizontal_checking(shape_to_move_vertically_clockwise)
    list_bottom = area_at_the_bottom_of_given_piece(shape_to_move_vertically_clockwise, leftmost_xy, rightmost_xy)
    shapes_at_the_bottom, list_shape3 = formation_of_set_S_vertical(list_bottom, new_vertices_shapes,
                                                                    shape_to_move_vertically_clockwise)
    
    #The shape with the vertical movememt requires to check other shapes present in its bottom. Hence, their maximum-y is calculated
    maximum_y = 0
    for j in range(len(shapes_at_the_bottom)):
        maximum_y_compare = maximum_y_coordinate(shapes_at_the_bottom[j])
        if maximum_y_compare > maximum_y:
            maximum_y = maximum_y_compare

    #The shape's vertices are moved vertically after above calculations
    vertical_movement = minimum_y_coordinate(shape_to_move_vertically_clockwise) - maximum_y
    for j in range(len(shape_to_move_vertically)):
        k = shape_to_move_vertically[j][0]
        l = shape_to_move_vertically[j][1] - vertical_movement + 1
        nested_shape.append((round(k, 2), round(l, 2), 0))

    if i != 0:
        for j in range(len(new_vertices_shapes)):
            if intersection_of_shapes(new_vertices_shapes[j], nested_shape) == True:
                intersection_with_previous_shapes = 1
    if intersection_with_previous_shapes == 0:
        for j in range(len(nested_shape)):
            invalid = 0
            if (((nested_shape[j][0] > length_sheet) or (nested_shape[j][1] > width_sheet)) and invalid == 0):
                invalid = 1
                break
        if invalid == 0:
            new_vertices_shapes.append(nested_shape)
            time.sleep(0.1)
            progress_for_shape = progress_for_shape + 1
            update_progress(int(progress_for_shape) / int(number_shape))
        if invalid == 1:
            invalid_shapes.append(vertices_in_decreasing_order[i])
    if intersection_with_previous_shapes == 1:
        invalid_shapes.append(vertices_in_decreasing_order[i])

# ---------------------------------------------------------------------------------------------------------------#
        
#Repeating the above process for invalid shapes only
delete_list_index = []
for m in range(len(invalid_shapes)):
    shape_to_move_vertically = []
    shape_to_move_horizontally = []
    nested_shape = []
    shape_to_move_vertically = invalid_shapes[m]

    # For Vertical list
    shape_to_move_vertically_clockwise = clockwise_list(shape_to_move_vertically)
    leftmost_xy, rightmost_xy = horizontal_checking(shape_to_move_vertically_clockwise)
    list_bottom = area_at_the_bottom_of_given_piece(shape_to_move_vertically_clockwise, leftmost_xy, rightmost_xy)
    shapes_at_the_bottom, list_shape3 = formation_of_set_S_vertical(list_bottom, new_vertices_shapes,
                                                                    shape_to_move_vertically_clockwise)
    maximum_y = 0
    for j in range(len(shapes_at_the_bottom)):
        maximum_y_compare = maximum_y_coordinate(shapes_at_the_bottom[j])
        if maximum_y_compare > maximum_y:
            maximum_y = maximum_y_compare

    vertical_movement = width_sheet - maximum_y
    for j in range(len(shape_to_move_vertically)):
        k = shape_to_move_vertically[j][0]
        l = shape_to_move_vertically[j][1] - vertical_movement + 1
        shape_to_move_horizontally.append((round(k, 2), round(l, 2), 0))

    # For Horizontal list
    shape_to_move_horizontally_clockwise = clockwise_list(shape_to_move_horizontally)
    leftmin_x, leftmax_y = vertical_checking(shape_to_move_horizontally_clockwise)
    list_left = area_at_the_left_of_given_piece(shape_to_move_horizontally_clockwise, leftmin_x, leftmax_y)
    shapes_at_the_left, list_shape3 = formation_of_set_S_horizontal(list_left, new_vertices_shapes,
                                                                    shape_to_move_horizontally_clockwise)
    maximum_x = 0
    for j in range(len(shapes_at_the_left)):
        maximum_x_compare = maximum_x_coordinate(shapes_at_the_left[j])
        if maximum_x_compare > maximum_x:
            maximum_x = maximum_x_compare
    if maximum_x == 0:
        horizontal_movement = minimum_x_coordinate(shape_to_move_horizontally_clockwise)
    else:
        horizontal_movement = minimum_x_coordinate(shape_to_move_horizontally_clockwise) - maximum_x
    shape_to_move_vertically = []
    for j in range(len(shape_to_move_horizontally)):
        k = shape_to_move_horizontally[j][0] - horizontal_movement + 1
        l = shape_to_move_horizontally[j][1]
        shape_to_move_vertically.append((round(k, 2), round(l, 2), 0))

    # For Vertical movement again, for the same shape
    shape_to_move_vertically_clockwise = clockwise_list(shape_to_move_vertically)
    leftmost_xy, rightmost_xy = horizontal_checking(shape_to_move_vertically_clockwise)
    list_bottom = area_at_the_bottom_of_given_piece(shape_to_move_vertically_clockwise, leftmost_xy, rightmost_xy)
    shapes_at_the_bottom, list_shape3 = formation_of_set_S_vertical(list_bottom, new_vertices_shapes,
                                                                    shape_to_move_vertically_clockwise)
    maximum_y = 0
    for j in range(len(shapes_at_the_bottom)):
        maximum_y_compare = maximum_y_coordinate(shapes_at_the_bottom[j])
        if maximum_y_compare > maximum_y:
            maximum_y = maximum_y_compare

    vertical_movement = minimum_y_coordinate(shape_to_move_vertically_clockwise) - maximum_y
    for j in range(len(shape_to_move_vertically)):
        k = shape_to_move_vertically[j][0]
        l = shape_to_move_vertically[j][1] - vertical_movement + 1
        nested_shape.append((round(k, 2), round(l, 2), 0))

    if i != 0:
        for j in range(len(new_vertices_shapes)):
            if intersection_of_shapes(new_vertices_shapes[j], nested_shape) == True:
                intersection_with_previous_shapes = 1
    if intersection_with_previous_shapes == 0:
        for j in range(len(nested_shape)):
            invalid = 0
            if (((nested_shape[j][0] > length_sheet) or (nested_shape[j][1] > width_sheet)) and invalid == 0):
                invalid = 1
                break
        if invalid == 0:
            new_vertices_shapes.append(nested_shape)
            delete_list_index.append(m)
            time.sleep(0.1)
            progress_for_shape = progress_for_shape + 1
            update_progress(int(progress_for_shape) / int(number_shape))
        if invalid == 1:
            vertices_for_other_shapes.append(invalid_shapes[m])
            delete_list_index.append(m)
    if intersection_with_previous_shapes == 1:
        vertices_for_other_shapes.append(invalid_shapes[m])
        delete_list_index.append(m)

for n in sorted(delete_list_index,
                reverse=True):  # Remove the invalid vertices which gets added to the list of valid vertices
    del invalid_shapes[n]
# ---------------------------------------------------------------------------------------------------------------#

#Nesting the circles and the reamining invalid shapes using bottom-left approach
new_vertices_other_shapes = []
maximum_y_for_other_shape_for_new_column = 0
maximum_y_for_other_shape_for_current_column = 0
maximum_x_of_previous_column = 0
first_shape_placed = 0
for j in range(len(new_vertices_shapes)):
    maximum_y_compare = maximum_y_coordinate(new_vertices_shapes[j])
    if maximum_y_compare > maximum_y_for_other_shape_for_new_column:
        maximum_y_for_other_shape_for_new_column = maximum_y_compare
for p in range(len(vertices_for_other_shapes)):
    moved_other_shape = []
    intersection_with_previous_shapes = 0
    intersection_with_previous_other_shapes = 0
    if p == 0:
        # Use maximum y to place the circles and other shapes and check for intersection and sheet value
        other_shape_to_move = vertices_for_other_shapes[p]
        vertical_movement_other_shape = width_sheet - (maximum_y_for_other_shape_for_new_column + 1)
        minimum_x_of_other_shape = minimum_x_coordinate(other_shape_to_move)
        horizontal_movement_other_shape = minimum_x_of_other_shape - 1
        for j in range(len(other_shape_to_move)):
            k = other_shape_to_move[j][0] - horizontal_movement_other_shape
            l = other_shape_to_move[j][1] - vertical_movement_other_shape
            moved_other_shape.append((round(k, 2), round(l, 2), 0))

        #Checking the intersection of current shape with previously placed shapes
        for j in range(len(new_vertices_shapes)):
            if intersection_of_shapes(new_vertices_shapes[j], moved_other_shape) == True:
                intersection_with_previous_shapes = 1

        #Placing the shapes if no intersections exist
        if intersection_with_previous_shapes == 0:
            for j in range(len(moved_other_shape)):
                invalid = 0
                if (((moved_other_shape[j][0] > length_sheet) or (
                        moved_other_shape[j][1] > width_sheet)) and invalid == 0):
                    invalid = 1
                    break
            if invalid == 0:
                new_vertices_other_shapes.append(moved_other_shape)
                first_shape_placed = 1
                time.sleep(0.1)
                progress_for_shape = progress_for_shape + 1
                update_progress(int(progress_for_shape) / int(number_shape))
            if invalid == 1:
                invalid_shapes.append(vertices_for_other_shapes[p])
                time.sleep(0.1)
                progress_for_shape = progress_for_shape + 1
                update_progress(int(progress_for_shape) / int(number_shape))

    if p != 0:
        # Use maximum y to place the circles and other shapes and check for intersection and sheet value
        other_shape_to_move = vertices_for_other_shapes[p]
        if first_shape_placed == 1:
            maximum_y_for_other_shape_for_current_column = maximum_y_coordinate(
                new_vertices_other_shapes[len(new_vertices_other_shapes) - 1])
        else:
            maximum_y_for_other_shape_for_current_column = maximum_y_for_other_shape_for_new_column
        minimum_x_of_other_shape = minimum_x_coordinate(other_shape_to_move)
        horizontal_movement_other_shape = minimum_x_of_other_shape - (maximum_x_of_previous_column + 1)
        vertical_movement_other_shape = width_sheet - (maximum_y_for_other_shape_for_current_column + 1)
        for j in range(len(other_shape_to_move)):
            k = other_shape_to_move[j][0] - horizontal_movement_other_shape
            l = other_shape_to_move[j][1] - vertical_movement_other_shape
            moved_other_shape.append((round(k, 2), round(l, 2), 0))

        #Checking the intersection of current shape with previously placed shapes
        for j in range(len(new_vertices_shapes)):
            if intersection_of_shapes(new_vertices_shapes[j], moved_other_shape) == True:
                intersection_with_previous_shapes = 1

        for j in range(len(new_vertices_other_shapes)):
            if intersection_of_shapes(new_vertices_other_shapes[j], moved_other_shape) == True:
                intersection_with_previous_other_shapes = 1

        #Placing the shapes if no intersections exist
        if intersection_with_previous_shapes == 0 and intersection_with_previous_other_shapes == 0:
            for j in range(len(moved_other_shape)):
                invalid = 0
                if (((moved_other_shape[j][0] > length_sheet) or (
                        moved_other_shape[j][1] > width_sheet)) and invalid == 0):
                    invalid = 1
                    break
            if invalid == 0:
                new_vertices_other_shapes.append(moved_other_shape)
            #Trying to nest the shape with maximum values of previous shapes as the last option
            if invalid == 1:
                moved_other_shape = []
                for j in range(len(new_vertices_other_shapes)):
                    maximum_x_compare = maximum_x_coordinate(new_vertices_other_shapes[j])
                    if maximum_x_compare > maximum_x_of_previous_column:
                        maximum_x_of_previous_column = maximum_x_compare
                horizontal_movement_other_shape = minimum_x_of_other_shape - (maximum_x_of_previous_column + 1)
                vertical_movement_other_shape = width_sheet - (maximum_y_for_other_shape_for_new_column + 1)
                for j in range(len(other_shape_to_move)):
                    k = other_shape_to_move[j][0] - horizontal_movement_other_shape
                    l = other_shape_to_move[j][1] - vertical_movement_other_shape
                    moved_other_shape.append((round(k, 2), round(l, 2), 0))

                #Checking for intersection again with other shapes
                for j in range(len(new_vertices_shapes)):
                    if intersection_of_shapes(new_vertices_shapes[j], moved_other_shape) == True:
                        intersection_with_previous_shapes = 1

                #Final placement of invalid shapes (those which were not placed previously)
                if intersection_with_previous_shapes == 0:
                    for j in range(len(moved_other_shape)):
                        invalid = 0
                        if (((moved_other_shape[j][0] > length_sheet) or (
                                moved_other_shape[j][1] > width_sheet)) and invalid == 0):
                            invalid = 1
                            break
                    if invalid == 0:
                        new_vertices_other_shapes.append(moved_other_shape)
                        time.sleep(0.1)
                        progress_for_shape = progress_for_shape + 1
                        update_progress(int(progress_for_shape) / int(number_shape))
                    if invalid == 1:
                        invalid_shapes.append(moved_other_shape)
                        time.sleep(0.1)
                        progress_for_shape = progress_for_shape + 1
                        update_progress(int(progress_for_shape) / int(number_shape))

# ---------------------------------------------------------------------------------------------------------------#

#Appending the shapes from the other shapes' list to the main and final list of vertices of the shapes to be placed
for n in range(len(new_vertices_other_shapes)):
    new_vertices_shapes.append(new_vertices_other_shapes[n])

#To make a beep sound once the code gives its output to notify the user
beep_sound(5)

# ---------------------------------------------------------------------------------------------------------------#

#Printing all of the required outputs obtained from the given inputs
print("-----------------------------------------------")
if len(invalid_shapes) == 1 and len(new_vertices_shapes) != 1:
    print("There is an unplaced shape and", len(new_vertices_shapes),
          "shapes have been placed in the sheet successfully.")
if len(new_vertices_shapes) == 1 and len(invalid_shapes) != 1:
    print("There are", len(invalid_shapes), "unplaced shapes and one shape has been placed in the sheet successfully.")
if len(invalid_shapes) == 1 and len(new_vertices_shapes) == 1:
    print("There is an unplaced shape and one shape has been placed in the sheet successfully.")
if len(new_vertices_shapes) != 1 and len(invalid_shapes) != 1:
    print("There are", len(invalid_shapes), "unplaced shapes and", len(new_vertices_shapes),
          "shapes have been placed in the sheet successfully.")
print("-----------------------------------------------")
print("Vertices of invalid shapes:", invalid_shapes)
print("-----------------------------------------------")
print("Final vertices for shapes: ", new_vertices_shapes)

# ---------------------------------------------------------------------------------------------------------------#
