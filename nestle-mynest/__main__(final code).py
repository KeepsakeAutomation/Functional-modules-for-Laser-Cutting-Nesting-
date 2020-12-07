# used a customised library consisting nesting functions
# library name : nestle-mypack
from mynest import functions
import time
import cv2
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from math import sqrt, sin, cos, pi, asin
import ezdxf
from matplotlib.patches import Polygon



# --------------------------------------------------------------------------------------------------------------- #
# PART-1: CREATING THE SHAPES AND SHEET WITH THE HELP OF THEIR DIMENSIONS
# --------------------------------------------------------------------------------------------------------------- #
# Developing the sheet through its dimensions
length_sheet = int(input("Enter the length for sheet: "))
width_sheet = int(input("Enter the width for sheet: "))
l, w, area = functions.sheet(length_sheet, width_sheet)
print("area of sheet:", area)
vertices_shapes_1 = []
a = int(input("How do you want to give the input? \n 1 : File selection \n 2 : Shape creation\n 3 : DXF file \n"))
if a == 1:
    b = int(input("Enter the extension of image \n 1:.svg \n 2:Format of images(.png,.jpeg,.tiff) \n"))
    contour_type = int(input(" 1) unfilled shapes \n 2) filled shapes \n"))
    if b == 1:
        # CONVERSION
        drawing = svg2rlg(input("Enter path: "))
        renderPM.drawToFile(drawing, "nested_shape.png", fmt="PNG")
        print("conversion done")
        img = cv2.imread("nested_shape.png")
        vertices_shapes_1 = functions.image(img, contour_type)
    elif b == 2:
        img = cv2.imread(input('ENTER PATH : '))
        vertices_shapes_1 = functions.image(img, contour_type)
        print("vertices_shapes_1 = ", vertices_shapes_1)
    else:
        print("Please enter correct number")
        vertices_shapes_1 = []
elif a == 2:
    number_shape = input("Enter the number of shapes you want to form: ")
    no_shape = 0
    if number_shape.isnumeric() == False or int(number_shape) < 0:  # Checking whether the number is numeric or not
        print("Please enter only positive value")
    vertices_for_other_shapes = []
    while int(number_shape) != no_shape:
        type_shape = input(
            "Choose the shape: 1.Circle 2.Triangle 3.Square 4.Rectangle 5.Regular Pentagon 6.Regular Hexagon 7.Polygon: ")
        type_sh = int(type_shape)
        if type_shape.isnumeric() == False or int(type_shape) < 0:
            print("Please enter only positive value")
        if type_sh == 1:  # Developing a circle
            radius = float(input("Enter the radius: "))
            Circle_shape = functions.circle(radius, length_sheet, width_sheet)
            vertices_for_other_shapes.append(Circle_shape)
            no_shape = no_shape + 1
        elif type_sh == 2:  # Developing a triangle
            temp1_triangle = int(input("Enter length-1 of Triangle: "))
            temp2_triangle = int(input("Enter length-2 of Triangle: "))
            temp3_triangle = int(input("Enter length-3 of Triangle: "))
            var_d = temp1_triangle + temp2_triangle
            var_e = temp2_triangle + temp3_triangle
            var_f = temp3_triangle + temp1_triangle
            # To check whether the triangle is valid or not
            if var_d > temp3_triangle and var_e > temp1_triangle and var_f > temp2_triangle:
                # Calculations for triangle
                Triangle_shape = functions.triangle(temp1_triangle, temp2_triangle, temp3_triangle, length_sheet,
                                                    width_sheet)
                vertices_for_other_shapes.append(Triangle_shape)
                no_shape = no_shape + 1
            else:
                print("\nEnter the correct length for triangle")

        elif type_sh == 3:  # Developing a square
            Square = float(input("Enter length of square: "))
            Square_shape = functions.square(Square, length_sheet, width_sheet)  # Calculations for square
            vertices_for_other_shapes.append(Square_shape)
            no_shape = no_shape + 1

        elif type_sh == 4:  # Developing a rectangle
            Rect_length = int(input("Enter length of rectangle: "))
            Rect_width = int(input("Enter width of rectangle: "))
            Rectangle_shape = functions.rectangle(Rect_length, Rect_width, length_sheet,
                                                  width_sheet)  # Calculation for rectangle
            vertices_for_other_shapes.append(Rectangle_shape)
            no_shape = no_shape + 1

        elif type_sh == 5:  # Developing a pentagon
            length_Pentagon = int(input("Enter the length of pentagon: "))
            Pentagon_shape = functions.pentagon(length_Pentagon, length_sheet, width_sheet)
            vertices_for_other_shapes.append(Pentagon_shape)
            no_shape = no_shape + 1

        elif type_sh == 6:  # Developing a hexagon
            length_Hexagon = int(input("Enter the length of hexagon: "))
            # Calculations for hexagon
            Hexagon_shape = functions.hexagon(length_Hexagon, length_sheet, width_sheet)
            vertices_for_other_shapes.append(Hexagon_shape)
            no_shape = no_shape + 1

        else:  # Developing a polygon with given amount of vertices
            polygon_vertices = input("Enter the total vertices of polygon: ")
            no_polygon = 0
            Polygon_shape = []
            while (int(polygon_vertices) != no_polygon):
                X_co_ordinate = input("Enter the value of X-Co-ordinate: ")
                Y_co_ordinate = input("Enter the value of Y-Co-ordinate: ")
                Polygon_shape.insert(no_polygon, (float(X_co_ordinate), float(Y_co_ordinate), 0))
                no_polygon = no_polygon + 1
            Polygon_shape_final = functions.polygon(Polygon_shape, length_sheet, width_sheet)  # Calculations for polygon
            vertices_for_other_shapes.append(Polygon_shape_final)
            no_shape = no_shape + 1

elif a == 3:
    list_for_start_end_points = []
    file_path = input("Enter the path of .DXF File: ")
    dwg = ezdxf.readfile(file_path)
    msp = dwg.modelspace()
    shapes_from_dxf_calc = functions.dxf_calculations(msp, length_sheet, width_sheet)
    vertices_shapes_1 = shapes_from_dxf_calc


else:
    print("/\_Please enter correct number/\_")
    vertices_shapes = []

# Developing the shapes through their dimensions
if a != 2:
    vertices_shapes = []
    vertices_shapes = functions.arg_shapes(vertices_shapes_1, length_sheet, width_sheet)
    vertices_for_other_shapes = vertices_shapes
    number_shape = len(vertices_shapes)
# ---------------------------------------------------------------------------------------------------------------#
# Functionality to add grouping of shapes
if (a == 1 and (b == 1 or b == 2)) or a == 3:
    c = int(input("Do you want to group the shapes?: \n"
                  "1. Yes, I want to group the shapes \n"
                  "2. No, I want to nest the shapes directly \n"))

    if c == 1:
        print("Opening the grouping section for you...")
        # Grouping the shapes and preparing those groups for nesting
        no_of_group = int(input("Enter the Number of groups to be formed: "))
        no_of_shapes_in_grp = []
        for i in range(no_of_group):
            a = i + 1
            no_of_shapes_in_grp.append(int(input("Enter the Number of shapes in group-" + str(a) + ": ")))
        grouped_list = []
        print("no_of_shapes_in_grp = ",no_of_shapes_in_grp)
        shape_choice = int(input("How do you want to create the groups?: \n"
                                 "1: Scattered - By entering specific position of shapes\n"
                                 "2: Consecutive - By entering the starting and ending position of shapes \n"))
        if shape_choice == 1:
            for i in range(len(no_of_shapes_in_grp)):
                a = i + 1
                shapes_in_group = []
                for j in range(no_of_shapes_in_grp[i]):
                    b = j + 1
                    c = (input(
                        "Enter the position (in numbers) for the group-" + str(a) + " and shape-" + str(b) + ": "))
                    shapes_in_group.append(int(c))
                grouped_list.append(shapes_in_group)
                print("grouped_list = ", grouped_list)
        elif shape_choice == 2:
            for i in range(len(no_of_shapes_in_grp)):
                a = i + 1
                b = 0
                shapes_in_group = []
                range_start_group = int(input("Enter the number for starting shape for group-" + str(a) + ": "))
                range_end_group = int(input("Enter the number for ending shape for group-" + str(a) + ": "))
                for j in range(no_of_shapes_in_grp[i]):
                    if j == 0:
                        b = range_start_group
                        shapes_in_group.append(int(b))
                        b = b + 1
                    else:
                        shapes_in_group.append(int(b))
                        b = b + 1
                grouped_list.append(shapes_in_group)

        else:
            print("You have entered an invalid choice.")

        groups_list = []
        all_shapes_length = []
        for i in range(len(grouped_list)):
            grouped_shapes = []
            shapes_length = []
            for j in range(len(grouped_list[i])):
                a = len(vertices_shapes_1[(grouped_list[i][j]) - 1])
                shapes_length.append(int(a))
                print("shapes_length = ",shapes_length)
                for k in range(a):
                    grouped_shapes.append(vertices_shapes_1[(grouped_list[i][j]) - 1][k])
            groups_list.append(grouped_shapes)
            print("groups_list = ", groups_list)
            all_shapes_length.append(shapes_length)
            print("all_shapes_length = ",all_shapes_length)

        print("-----------------------------------------------")
        arranged_groups = []
        arranged_groups = functions.arg_shapes(groups_list, length_sheet, width_sheet)
        progress_for_shape = 0
        new_vertices_shapes = []
        invalid_shapes = []
        # Nesting the shapes using bottom-left approach
        new_vertices_other_shapes = functions.gravity_approach(length_sheet, width_sheet, new_vertices_shapes,
                                                               arranged_groups, invalid_shapes)
        new_vertices_other_shapes = functions.nested_shapes_coordinates_eff(new_vertices_other_shapes)
        # ---------------------------------------------------------------------------------------------------------------#
        # Appending the shapes from the other shapes' list to the main and final list of vertices of the shapes to be placed


        for n in range(len(new_vertices_other_shapes)):
            new_vertices_shapes.append(new_vertices_other_shapes[n])

        for i in range(len(all_shapes_length)):
            print(len(all_shapes_length[i]))
        # Ungrouping the groups back to the form of shapes
        # all_shapes_length
        grouped_nested_shapes = []
        for i in range(len(all_shapes_length)):
            c = []
            for j in range(len(all_shapes_length[i])):
                b = all_shapes_length[i][j]
                print("b=", b)
                c = new_vertices_shapes[i][:b]
                print("c", c)
                grouped_nested_shapes.append(c)
                d = len(new_vertices_shapes[i])
                e = d - b
                f = new_vertices_shapes[i][-e:]
                new_vertices_shapes[i] = f
        # ---------------------------------------------------------------------------------------------------------------#
        # Printing all of the required outputs obtained from the given inputs
        print("-----------------------------------------------")
        functions.print_func_1(new_vertices_shapes, invalid_shapes, grouped_nested_shapes)
        freecad_file_address = input("Please enter the freecad file path: ")
        code_for_freecad = functions.freecad_nesting(grouped_nested_shapes, length_sheet, width_sheet,
                                                     freecad_file_address)

    if c == 2:
        print("Wait for sometime, nesting is happening in the background...")
        print("-----------------------------------------------")
        progress_for_shape = 0
        new_vertices_shapes = []
        invalid_shapes = []
        # Nesting the circles and the remaining invalid shapes using bottom-left approach
        new_vertices_other_shapes = []
        maximum_y_for_other_shape_for_new_column = 0
        maximum_y_for_other_shape_for_current_column = 0
        maximum_x_of_previous_column = 0
        first_shape_placed = 0
        new_vertices_other_shapes = functions.gravity_approach(length_sheet, width_sheet, new_vertices_shapes,
                                                               vertices_for_other_shapes, invalid_shapes)
        new_vertices_other_shapes_final = functions.nested_shapes_coordinates_eff(new_vertices_other_shapes)
        # ---------------------------------------------------------------------------------------------------------------#
        # Appending the shapes from the other shapes' list to the main and final list of vertices of the shapes to be placed
        for n in range(len(new_vertices_other_shapes_final)):
            new_vertices_shapes.append(new_vertices_other_shapes_final[n])
        # ---------------------------------------------------------------------------------------------------------------#
        # Printing all of the required outputs obtained from the given inputs
        print("-----------------------------------------------")
        functions.print_func_2(new_vertices_shapes, invalid_shapes)
        freecad_file_address = input("Please enter the freecad file path: ")
        code_for_freecad = functions.freecad_nesting(new_vertices_shapes, length_sheet, width_sheet,
                                                     freecad_file_address)
    # ---------------------------------------------------------------------------------------------------------------#

if a == 2:
    print("Wait for sometime, nesting is happening in the background...")
    print("-----------------------------------------------")
    progress_for_shape = 0
    new_vertices_shapes = []
    invalid_shapes = []
    # Nesting the circles and the remaining invalid shapes using bottom-left approach
    new_vertices_other_shapes = []
    maximum_y_for_other_shape_for_new_column = 0
    maximum_y_for_other_shape_for_current_column = 0
    maximum_x_of_previous_column = 0
    first_shape_placed = 0
    new_vertices_other_shapes = functions.gravity_approach(length_sheet, width_sheet, new_vertices_shapes,
                                                           vertices_for_other_shapes, invalid_shapes)
    new_vertices_other_shapes_final = functions.nested_shapes_coordinates_eff(new_vertices_other_shapes)
    # ---------------------------------------------------------------------------------------------------------------#
    # Appending the shapes from the other shapes' list to the main and final list of vertices of the shapes to be placed
    for n in range(len(new_vertices_other_shapes_final)):
        new_vertices_shapes.append(new_vertices_other_shapes_final[n])
    # ---------------------------------------------------------------------------------------------------------------#
    # Printing all of the required outputs obtained from the given inputs
    print("-----------------------------------------------")
    functions.print_func_2(new_vertices_shapes, invalid_shapes)
    freecad_file_address = input("Please enter the freecad file path: ")
    code_for_freecad = functions.freecad_nesting(new_vertices_shapes, length_sheet, width_sheet, freecad_file_address)
# ---------------------------------------------------------------------------------------------------------------#
