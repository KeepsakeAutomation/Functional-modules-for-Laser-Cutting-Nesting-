# Importing the required libraries

import cv2
import matplotlib.pyplot as plt
import time
import math
import ezdxf
import numpy as np
from matplotlib.patches import Polygon
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from math import sqrt, sin, cos, pi, asin




# ---------------------------------------------------------------------------------------------------------------#

# All of the required functions at one place


def sheet(length_sheet, width_sheet):
    vertices_sheet = [(0, 0, 0), (int(length_sheet), 0, 0), (int(length_sheet), (int(width_sheet)), 0), (0, (int(width_sheet)), 0)]
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
    return length_sheet, width_sheet, area_of_sheet


def horizontal_checking(list_shape1):
    right_x1 = 0
    left_x1 = 0
    for x1 in range(len(list_shape1)):  # Get the lowest y-coordinate of shape-1
        if x1 == 0:  # Get the highest y-coordinate of shape-1
            right_x1 = list_shape1[x1][0]
            a = list_shape1[0 + int(x1)]
            left_x1 = list_shape1[x1][0]
            b = list_shape1[0 + int(x1)]
        else:
            if list_shape1[x1][0] == right_x1:
                if list_shape1[x1][1] < a[1]:
                    a = list_shape1[0 + int(x1)]
            if list_shape1[x1][0] > right_x1:
                right_x1 = list_shape1[x1][0]
                a = list_shape1[0 + int(x1)]
            if list_shape1[x1][0] == left_x1:
                if list_shape1[x1][1] < b[1]:
                    b = list_shape1[0 + int(x1)]
            if list_shape1[x1][0] < left_x1:
                left_x1 = list_shape1[x1][0]
                b = list_shape1[0 + int(x1)]
    return b, a


def clockwise_list(list_shape2):
    j = 0
    list_shape1 = []
    for i in range(len(list_shape2)):  # Check => shape co-ordinates are clockwise or anti-clockwise
        if i != len(list_shape2) - 1:
            j = j + ((list_shape2[i + 1][0] - list_shape2[i][0]) * (list_shape2[i + 1][1] + list_shape2[i][1]))
        else:
            j = j + ((list_shape2[0][0] - list_shape2[i][0]) * (list_shape2[0][1] + list_shape2[i][1]))
    if j > 0:  # If shape co-ordinates are anti-clockwise then arrange it in clockwise
        list_shape1 = list_shape2
    else:
        for i in range(len(list_shape2)):
            list_shape1.append(
                list_shape2[len(list_shape2) - 1 - i])  # list_shape1 = clockwise arrangement of co-ordinates
    return list_shape1

def area_at_the_left_of_given_piece(list_shape1, x, y):
    list = []
    list1 = [y]
    for i in range(len(list_shape1)):  # Fatching co_ordinates between leftmost high and leftmost low co-ordinates
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

def vertical_checking(list_shape1):
    high_y1 = 0
    low_y1 = 0
    for y1 in range(len(list_shape1)):  # Get the lowest y-coordinate of shape-1
        if y1 == 0:  # Get the highest y-coordinate of shape-1
            high_y1 = list_shape1[y1][1]
            a = list_shape1[0 + int(y1)]
            low_y1 = list_shape1[y1][1]
            b = list_shape1[0 + int(y1)]
        else:
            if list_shape1[y1][1] == high_y1:
                if list_shape1[y1][0] < a[0]:
                    a = list_shape1[0 + int(y1)]
            if list_shape1[y1][1] > high_y1:
                high_y1 = list_shape1[y1][1]
                a = list_shape1[0 + int(y1)]
            if list_shape1[y1][1] == low_y1:
                if list_shape1[y1][0] < b[0]:
                    b = list_shape1[0 + int(y1)]
            if list_shape1[y1][1] < low_y1:
                low_y1 = list_shape1[y1][1]
                b = list_shape1[0 + int(y1)]
    return b, a

def side(a, b, c):
    """ Returns a position of the point c relative to the line going through a and b
        Points a, b are expected to be different
    """
    d = (c[1] - a[1]) * (b[0] - a[0]) - (b[1] - a[1]) * (c[0] - a[0])
    return 1 if d > 0 else (-1 if d < 0 else 0)


def is_point_in_closed_segment(a, b, c):
    """ Returns True if c is inside closed segment, False otherwise.
        a, b, c are expected to be collinear
    """
    if a[0] < b[0]:
        return a[0] <= c[0] and c[0] <= b[0]
    if b[0] < a[0]:
        return b[0] <= c[0] and c[0] <= a[0]

    if a[1] < b[1]:
        return a[1] <= c[1] and c[1] <= b[1]
    if b[1] < a[1]:
        return b[1] <= c[1] and c[1] <= a[1]

    return a[0] == c[0] and a[1] == c[1]


def closed_segment_intersect(a, b, c, d):
    """ Verifies if closed segments a, b, c, d do intersect.
    """
    if a == b:
        return a == c or a == d
    if c == d:
        return c == a or c == b

    s1 = side(a, b, c)
    s2 = side(a, b, d)

    # All points are collinear
    if s1 == 0 and s2 == 0:
        return \
            is_point_in_closed_segment(a, b, c) or is_point_in_closed_segment(a, b, d) or \
            is_point_in_closed_segment(c, d, a) or is_point_in_closed_segment(c, d, b)

    # No touching and on the same side
    if s1 and s1 == s2:
        return False

    s1 = side(c, d, a)
    s2 = side(c, d, b)

    # No touching and on the same side
    if s1 and s1 == s2:
        return False
    return True


def is_point_in_closed_segment_vertical(a, b, c):
    """ Returns True if c is inside closed segment, False otherwise.
        a, b, c are expected to be collinear
    """
    if a[0] < b[0]:
        return a[0] < c[0] and c[0] < b[0]
    if b[0] < a[0]:
        return b[0] < c[0] and c[0] < a[0]

    if a[1] < b[1]:
        return a[1] < c[1] and c[1] < b[1]
    if b[1] < a[1]:
        return b[1] < c[1] and c[1] < a[1]

    return a[0] == c[0] and a[1] == c[1]


def minimum_x_coordinate(list_shape1):
    for i in range(len(list_shape1)):
        if i == 0:
            min_x = list_shape1[0][0]
        else:
            if min_x >= list_shape1[i][0]:
                min_x = list_shape1[i][0]
    return min_x


def maximum_x_coordinate(list_1):
    for i in range(len(list_1)):
        if i == 0:
            max_x = list_1[0][0]
        else:
            if max_x <= list_1[i][0]:
                max_x = list_1[i][0]
    return max_x


def minimum_y_coordinate(list_2):
    for i in range(len(list_2)):
        if i == 0:
            min_y = list_2[0][1]
        else:
            if min_y >= list_2[i][1]:
                min_y = list_2[i][1]
    return min_y


def maximum_y_coordinate(list_2):
    for i in range(len(list_2)):
        if i == 0:
            max_y = list_2[0][1]
        else:
            if max_y <= list_2[i][1]:
                max_y = list_2[i][1]
    return max_y

def intersection_of_shapes(list_shape1, list_shape2):
    if (list_shape1 == list_shape2):
        return True
    for y1 in range(len(list_shape1)):  # Get the lowest y-coordinate of shape-1
        if y1 == 0:  # Get the highest y-coordinate of shape-1
            high_y1 = list_shape1[y1][1]
            low_y1 = list_shape1[y1][1]
        else:
            if list_shape1[y1][1] > high_y1:
                high_y1 = list_shape1[y1][1]
            if list_shape1[y1][1] < low_y1:
                low_y1 = list_shape1[y1][1]

    for y2 in range(len(list_shape2)):  # Get the lowest y-coordinate of shape-2
        if y2 == 0:  # Get the highest y-coordinate of shape-2
            high_y2 = list_shape2[y2][1]
            low_y2 = list_shape2[y2][1]
        else:
            if list_shape2[y2][1] > high_y2:
                high_y2 = list_shape2[y2][1]
            if list_shape2[y2][1] < low_y2:
                low_y2 = list_shape2[y2][1]

    if low_y1 > high_y2 or low_y2 > high_y1:  # Checks the condition for intersection
        return False

    for x1 in range(len(list_shape1)):  # Get the leftmost x-coordinate of shape-1
        if x1 == 0:  # Get the rightmost x-coordinate of shape-1
            right_x1 = list_shape1[x1][0]
            left_x1 = list_shape1[x1][0]
        else:
            if list_shape1[x1][0] > right_x1:
                right_x1 = list_shape1[x1][0]
            if list_shape1[x1][0] < left_x1:
                left_x1 = list_shape1[x1][0]

    for x2 in range(len(list_shape2)):  # Get the leftmost x-coordinate of shape-2
        if x2 == 0:  # Get the rightmost x-coordinate of shape-2
            right_x2 = list_shape2[x2][0]
            left_x2 = list_shape2[x2][0]
        else:
            if list_shape2[x2][0] > right_x2:
                right_x2 = list_shape2[x2][0]
            if list_shape2[x2][0] < left_x2:
                left_x2 = list_shape2[x2][0]

    if left_x1 > right_x2 or left_x2 > right_x1:  # Checks the condition for intersection
        return False

    for e1 in range(len(list_shape1)):  # Creates the edges from co-ordinates of shape-1
        if e1 == len(list_shape1) - 1:
            a = list_shape1[0 + int(e1)]
            b = list_shape1[0]
        else:
            a = list_shape1[0 + int(e1)]
            b = list_shape1[1 + int(e1)]
        for e2 in range(len(list_shape2)):  # Creates the edges from co-ordinates of shape-2
            if e2 == len(list_shape2) - 1:
                c = list_shape2[0 + int(e2)]
                d = list_shape2[0]
            else:
                c = list_shape2[0 + int(e2)]
                d = list_shape2[1 + int(e2)]
            if (closed_segment_intersect(a, b, c, d) == True):
                return True
                break
    if (closed_segment_intersect(a, b, c, d) == True):  # Checks the condition for intersection
        return True
    else:
        return False


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


def image(img, contour_type):
    # convert to RGB
    scale_percent = 26.46  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    image = cv2.flip(image,0)
    # convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # create a binary thresholded image
    _, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
    list_of_contours = []
    list_of_hierarchy = []
    list_of_contours_final = []
    number_of_contour = []
    list_of_contours_not_used = []

    if contour_type == 1:
        # find the contours from the thresholded image
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # cv2.RETR_CCOMP cv2.RETR_TREE cv2.RETR_EXTERNAL

        for i in range(len(hierarchy)):
            list_of_hierarchy = []
            for j in range(len(hierarchy[i])):
                a = hierarchy[i][j][0]
                b = hierarchy[i][j][1]
                c = hierarchy[i][j][2]
                d = hierarchy[i][j][3]
                e = a,b,c,d
                list_of_hierarchy.append(e)

        for i in range(len(contours)):
            list_used_to_find_contours = []
            for j in range(len(contours[i])):
                for k in range(len(contours[i][j])):
                    a = contours[i][j][k][0]
                    b = contours[i][j][k][1]
                    c = a,b,0
                    list_used_to_find_contours.append(c)
            if len(list_used_to_find_contours) != 1 :
                list_of_contours.append(list_used_to_find_contours)

        for i in range(len(list_of_hierarchy)) :
            for j in range(len(list_of_hierarchy)) :
                if i == list_of_hierarchy[j][2] :
                    for k in range(len(list_of_hierarchy)) :
                        if i == list_of_hierarchy[k][3] :
                            n = list_of_hierarchy[i][3]
                            if list_of_hierarchy[n][3] == -1:
                                number_of_contour.append(n)
            if list_of_hierarchy[i][2] == -1 :
                n = list_of_hierarchy[i][3]
                number_of_contour.append(n)

        for i in range(len(list_of_contours)) :
            if (i in number_of_contour) == True :
                list_of_contours_final.append(list_of_contours[i])
            else :
                list_of_contours_not_used.append(list_of_contours[i])

        if len(list_of_contours_final) == 0 :
            index = 0
            for i in range(len(list_of_hierarchy)):
                if (list_of_hierarchy[i][2],list_of_hierarchy[i][3]) == (-1,-1):
                    index = index + 1
            if index == len(list_of_hierarchy):
                list_of_contours_final =  list_of_contours

        # font
        font = cv2.FONT_HERSHEY_SIMPLEX
        for i in range(len(list_of_contours_final)):
            text = str(i)
            org = list_of_contours_final[i][0][0], list_of_contours_final[i][0][1] - 3
            image = cv2.putText(image, text, org, font, fontScale=0.5, color=(0, 0, 255), thickness=1)

        # draw all contours
        image = cv2.drawContours(image, contours, -1, (0, 255, 0), 1)

        # show the image with the drawn contours
        plt.imshow(image)
        plt.show()
        return list_of_contours_final

    elif contour_type == 2:
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_SIMPLE)  # cv2.RETR_CCOMP cv2.RETR_TREE cv2.RETR_EXTERNAL

        for i in range(len(contours)):
            list_used_to_find_contours = []
            for j in range(len(contours[i])):
                for k in range(len(contours[i][j])):
                    a = contours[i][j][k][0]
                    b = contours[i][j][k][1]
                    c = a, b, 0
                    list_used_to_find_contours.append(c)
            if len(list_used_to_find_contours) != 1:
                list_of_contours_final.append(list_used_to_find_contours)

        # font
        font = cv2.FONT_HERSHEY_SIMPLEX
        for i in range(len(list_of_contours_final)):
            text = str(i)
            org = list_of_contours_final[i][0][0], list_of_contours_final[i][0][1] - 3
            image = cv2.putText(image, text, org, font , fontScale = 0.5, color = (0, 0, 255), thickness = 1)

        # draw all contours
        image = cv2.drawContours(image, contours, -1, (0, 255, 0), 1)

        # show the image with the drawn contours
        plt.imshow(image)
        plt.show()
        return list_of_contours_final

    else :
        return print(" You have entered an invalid choice ")


def nested_shapes_coordinates(new_vertices_other_shapes):
    left_shape = []
    right_shape = []
    new_vertices_other_shapes_clockwise = []

    for i in range(len(new_vertices_other_shapes)):
        new_vertices_other_shapes_clockwise.append(clockwise_list(new_vertices_other_shapes[i]))
    new_vertices_other_shapes = new_vertices_other_shapes_clockwise

    vertices_nested_again_shapes = []
    for i in range(len(new_vertices_other_shapes)):
        right_shape = new_vertices_other_shapes[i]
        max_y = maximum_y_coordinate(right_shape)
        min_y = minimum_y_coordinate(right_shape)
        min_x = minimum_x_coordinate(right_shape)
        max_x = maximum_x_coordinate(right_shape)
        left_side_coordinates = []
        for i in range(len(vertices_nested_again_shapes)):
            points_of_left_shape = []
            if right_shape == vertices_nested_again_shapes[i]:
                continue
            for j in range(len(vertices_nested_again_shapes[i])):
                if vertices_nested_again_shapes[i][j][0] <= min_x and vertices_nested_again_shapes[i][j][1] <= max_y and \
                        vertices_nested_again_shapes[i][j][1] >= min_y:
                    points_of_left_shape.append(vertices_nested_again_shapes[i][j])
            if len(points_of_left_shape) != 0:
                left_side_coordinates.append(vertices_nested_again_shapes[i])

        if len(left_side_coordinates) == 0 or len(left_side_coordinates) != 0:
            var_1 = 0
            var_3 = (-1, -1, -1)
            var_6 = (-1, -1, -1)
            var_4 = 10000
            for i in range(len(vertices_nested_again_shapes)):
                for j in range(len(vertices_nested_again_shapes[i])):
                    if vertices_nested_again_shapes[i][j][1] <= min_y and vertices_nested_again_shapes[i][j][0] <= min_x:
                        var_2 = vertices_nested_again_shapes[i][j]
                        if var_2[1] > var_1:
                            var_1 = var_2[1]
                            var_3 = var_2
                    if vertices_nested_again_shapes[i][j][1] >= max_y and vertices_nested_again_shapes[i][j][0] <= min_x:
                        var_5 = vertices_nested_again_shapes[i][j]
                        if var_5[1] < var_4:
                            var_4 = var_5[1]
                            var_6 = var_5
            if var_3 == (-1, -1, -1) :
                left_side_coordinates = []
            else:
                for i in range(len(vertices_nested_again_shapes)):
                    for j in range(len(vertices_nested_again_shapes[i])):
                        if var_3 == vertices_nested_again_shapes[i][j] or var_6 == vertices_nested_again_shapes[i][j]:
                            left_side_coordinates.append(vertices_nested_again_shapes[i])
                            break

        slope_points = []
        for j in range(len(left_side_coordinates)):
            for i in range(len(left_side_coordinates[j])):
                if i != len(left_side_coordinates[j]) - 1:
                    ax1 = round(left_side_coordinates[j][i][0], 1)
                    ay1 = round(left_side_coordinates[j][i][1], 1)
                    ax2 = round(left_side_coordinates[j][i + 1][0], 1)
                    ay2 = round(left_side_coordinates[j][i + 1][1], 1)
                else:
                    ax1 = round(left_side_coordinates[j][i][0], 1)
                    ay1 = round(left_side_coordinates[j][i][1], 1)
                    ax2 = round(left_side_coordinates[j][0][0], 1)
                    ay2 = round(left_side_coordinates[j][0][1], 1)
                if ax1 == ax2 and ay1 == ay2:
                    continue
                elif ay1 == ay2:
                    if ax1 < ax2:
                        inc_value = ax1
                        while inc_value != ax2:
                            inc_value = round(inc_value + 0.1, 1)
                            slope_points.append((inc_value, ay1, 0))
                    else:
                        inc_value = ax1
                        while inc_value != ax2:
                            inc_value = round(inc_value - 0.1, 1)
                            slope_points.append((inc_value, ay1, 0))
                elif ax1 == ax2:
                    if ay1 < ay2:
                        inc_value = ay1
                        while inc_value != ay2:
                            inc_value = round(inc_value + 0.1, 1)
                            slope_points.append((ax1, inc_value, 0))
                    else:
                        inc_value = ay1
                        while inc_value != ay2:
                            inc_value = round(inc_value - 0.1, 1)
                            slope_points.append((ax1, inc_value, 0))
                elif ax1 != ax2 or ay1 != ay2:
                    slope = (ay2 - ay1) / (ax2 - ax1)
                    inc_value = ay1
                    if ay2 > ay1:
                        while (round(float(inc_value), 1) != ay2):
                            inc_value = round(inc_value + 0.1, 1)
                            obt_value = round(float((inc_value - ay1 + (slope * ax1)) / slope), 1)
                            slope_points.append((obt_value, inc_value, 0))
                    else:
                        while (round(float(inc_value), 1) != ay2):
                            inc_value = round(inc_value - 0.1, 1)
                            obt_value = round(float((inc_value - ay1 + (slope * ax1)) / slope), 1)
                            slope_points.append((obt_value, inc_value, 0))

        x_for_right_shape ,y_for_right_shape= vertical_checking(right_shape)
        min_points = area_at_the_left_of_given_piece(right_shape,x_for_right_shape,y_for_right_shape)

        left_side_coordinates = []
        for i in range(len(min_points) - 1):
            ax1 = round(min_points[i][0], 1)
            ay1 = round(min_points[i][1], 1)
            ax2 = round(min_points[i + 1][0], 1)
            ay2 = round(min_points[i + 1][1], 1)
            if ax1 == ax2 and ay1 == ay2:
                continue
            elif ay1 == ay2:
                if ax1 < ax2:
                    inc_value = ax1
                    while inc_value != ax2:
                        left_side_coordinates.append((inc_value, ay1, 0))
                        inc_value = round(inc_value + 0.1, 1)
                    left_side_coordinates.append((ax2,ay1,0))
                else:
                    inc_value = ax1
                    while inc_value != ax2:
                        left_side_coordinates.append((inc_value, ay1, 0))
                        inc_value = round(inc_value - 0.1, 1)
                    left_side_coordinates.append((ax2, ay1, 0))
            elif ax1 == ax2:
                if ay1 < ay2:
                    inc_value = ay1
                    left_side_coordinates.append((ax1,ay1,0))
                    while inc_value != ay2:
                        inc_value = round(inc_value + 0.1, 1)
                        left_side_coordinates.append((ax1, inc_value, 0))
                else:
                    inc_value = ay1
                    left_side_coordinates.append((ax1,ay1,0))
                    while inc_value != ay2:
                        inc_value = round(inc_value - 0.1, 1)
                        left_side_coordinates.append((ax1, inc_value, 0))
            elif ax1 != ax2 or ay1 != ay2:
                slope = (ay2 - ay1) / (ax2 - ax1)
                inc_value = ax1
                if ax2 > ax1:
                    left_side_coordinates.append((ax1,ay1,0))
                    while (round(float(inc_value), 1) != ax2):
                        inc_value = round(inc_value + 0.1, 1)
                        obt_value = round(float((slope * (inc_value - ax1)) + ay1), 1)
                        left_side_coordinates.append((inc_value, obt_value, 0))
                else:
                    left_side_coordinates.append((ax1,ay1,0))
                    while (round(float(inc_value), 1) != ax2):
                        inc_value = round(inc_value - 0.1, 1)
                        obt_value = round(float((slope * (inc_value - ax1)) + ay1), 1)
                        left_side_coordinates.append((inc_value, obt_value, 0))


        short_distances = []
        for i in range(len(slope_points)):
            y_slope_point = round(slope_points[i][1], 1)
            x_slope_point = round(slope_points[i][0], 1)
            for j in range(len(left_side_coordinates)):
                y_min_point = round(left_side_coordinates[j][1], 1)
                x_min_point = round(left_side_coordinates[j][0], 1)
                if y_min_point == y_slope_point:
                    short_distance = round(x_min_point - x_slope_point,1)
                    short_distances.append(short_distance)

        shortest_distance_x = min_x
        for i in range(len(short_distances)):
            if i == 0:
                shortest_distance_x = short_distances[i]
            if short_distances[i] < shortest_distance_x:
                shortest_distance_x = short_distances[i]
        right_shape_nested = []
        for i in range(len(right_shape)):
            if shortest_distance_x == 0:
                a = right_shape[i][0] + 1
            else:
                a = right_shape[i][0] - (shortest_distance_x - 1)
            right_shape_nested.append((a, right_shape[i][1], 0))
        vertices_nested_again_shapes.append(right_shape_nested)
    return vertices_nested_again_shapes


def circle(radius, length_sheet, width_sheet):
    Circle_shape = []
    angle = 1
    times = 360 / angle
    x = radius
    y = radius
    theta = 0
    # Developing a polygon which contains 360 sides and also resembles circle completely
    for i in range(int(times)):
        point_circle = (round(int(length_sheet) + (x + ((radius) * sin(theta * (pi / 180)))) - (2 * radius), 6),
                        round(int(width_sheet) + (y + ((radius) * cos(theta * (pi / 180)))), 6), 0)
        Circle_shape.append(point_circle)
        theta = theta + angle
    return Circle_shape


def triangle(temp1_triangle, temp2_triangle, temp3_triangle, length_sheet, width_sheet):
    # Equilateral Triangle
    if temp1_triangle == temp2_triangle == temp3_triangle:
        Triangle_shape = [(int(length_sheet) - temp2_triangle, int(width_sheet), 0),
                          (int(length_sheet), int(width_sheet), 0), (
                          (int(length_sheet) + round((temp1_triangle / 2), 2)) - temp2_triangle,
                          round(sqrt((temp1_triangle * 2) - ((temp1_triangle / 2) * 2)), 2) + int(width_sheet), 0)]
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
                          (int(length_sheet), int(width_sheet), 0), ((int(length_sheet) + (var_t2 / 2)) - var_t2, round(
                sqrt((var_t1 * var_t1) - ((var_t2 / 2) * (var_t2 / 2))), 2) + int(width_sheet), 0)]
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
        Triangle_shape = [(int(length_sheet) - var_t2, int(width_sheet), 0), (int(length_sheet), int(width_sheet), 0),
                          ((int(length_sheet) + (F - W)) - var_t2, int(width_sheet) + (H + T), 0)]
    return Triangle_shape



def square(Square, length_sheet, width_sheet):
    Square_shape = [(int(length_sheet) - Square, int(width_sheet), 0),
                    (int(length_sheet) - Square, Square + int(width_sheet), 0),
                    (int(length_sheet), Square + int(width_sheet), 0), (int(length_sheet), int(width_sheet), 0)]
    return Square_shape


def rectangle(Rect_length, Rect_width, length_sheet, width_sheet):
    Rectangle_shape = [(int(length_sheet) - Rect_length, int(width_sheet), 0),
                       (int(length_sheet) - Rect_length, Rect_width + int(width_sheet), 0),
                       (int(length_sheet), Rect_width + int(width_sheet), 0), (int(length_sheet), int(width_sheet), 0)]
    return Rectangle_shape


def pentagon(length_Pentagon, length_sheet, width_sheet):
    # Calculation for pentagon
    Pentagon_shape = [(int(length_sheet) + (round(length_Pentagon * cos((2 * pi) / 5), 2)) - (
        round((2 * length_Pentagon * cos((2 * pi) / 5)) + length_Pentagon, 2)), int(width_sheet), 0),
                      ((int(length_sheet) + (
                              round((length_Pentagon * cos((2 * pi) / 5)), 2) + length_Pentagon)) - (
                           round((2 * length_Pentagon * cos((2 * pi) / 5)) + length_Pentagon, 2)),
                       int(width_sheet),
                       0),
                      (int(length_sheet), round(length_Pentagon * sin((2 * pi) / 5), 2) + int(width_sheet), 0),
                      ((int(length_sheet) + round((length_Pentagon * cos((2 * pi) / 5)) + (length_Pentagon / 2),
                                                  2)) - (
                           round((2 * length_Pentagon * cos((2 * pi) / 5)) + length_Pentagon, 2)),
                       round((length_Pentagon * sin((2 * pi) / 5)) + (length_Pentagon * cos(pi / 3.33)),
                             2) + int(
                           width_sheet), 0),
                      (int(length_sheet) - (
                          round((2 * length_Pentagon * cos((2 * pi) / 5)) + length_Pentagon, 2)),
                       round(length_Pentagon * sin((2 * pi) / 5), 2) + int(width_sheet), 0)]
    return Pentagon_shape


def hexagon(length_Hexagon, length_sheet, width_sheet):
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
    return Hexagon_shape


def polygon(Polygon_shape, length_sheet, width_sheet):
    Polygon_shape_final = []
    minimum_x = minimum_x_coordinate(Polygon_shape)
    maximum_x = maximum_x_coordinate(Polygon_shape)
    minimum_y = minimum_y_coordinate(Polygon_shape)
    # Putting a polygon to the upper-right corner of the sheet
    for i in range(len(Polygon_shape)):
        origin = (int(length_sheet) + (Polygon_shape[i][0] - minimum_x)) - (maximum_x - minimum_x), \
                 Polygon_shape[i][1] - minimum_y + int(width_sheet), 0
        Polygon_shape_final.append(origin)
    return Polygon_shape_final




def freecad_nesting(new_vertices_shapes,length_sheet,width_sheet, freecad_file_address) :
    # Adding the requisite data to the macro file of FreeCAD
    file_object = open(freecad_file_address, "w+")
    file_object.write("#Import the library files \n"
                      "import FreeCAD,Draft \n"
                      "import PartDesign \n"
                      "import PartDesignGui \n"
                      "import Spreadsheet \n"
                      "from math import sin,cos,degrees,radians,pi,sqrt,asin \n \n"
                      "#Create a new document and activate PartDesign Workbench \n"
                      "App.newDocument(\"Shape\") \n"
                      "Gui.activateWorkbench(\"PartDesignWorkbench\") \n"
                      "App.activeDocument().addObject('PartDesign::Body','Body') \n"
                      "Gui.activeView().setActiveObject('pdbody', App.activeDocument().Body) \n"
                      "Gui.Selection.clearSelection() \n"
                      "Gui.Selection.addSelection(App.ActiveDocument.Body) \n"
                      "App.ActiveDocument.recompute() \n")

    file_object.write("sheet = [(0.0, 0.0, 0), (" + str(length_sheet) + ", 0.0, 0), (" + str(length_sheet) + ", " + str(width_sheet) + ", 0), (0.0, " + str(width_sheet) + ", 0)] \n")
    file_object.write("wire = Draft.makeWire(sheet, closed=True) \n")

    c = ["a%d" % x for x in range(1, len(new_vertices_shapes) + 1)]
    for x in range(len(c)):  # you can loop over them
        file_object.write(str(c[x]) + "=" + str(new_vertices_shapes[x]) + "\n")
        file_object.write("wire = Draft.makeWire(" + str(c[x]) + ", closed=True) \n")
    file_object.close()
    return print("Macro file has been updated/created")

def nested_shapes_coordinates_eff(new_vertices_other_shapes):
    left_shape = []
    right_shape = []
    bottom_shape = []
    top_shape = []
    new_vertices_other_shapes_clockwise = []

    for i in range(len(new_vertices_other_shapes)):
        new_vertices_other_shapes_clockwise.append(clockwise_list(new_vertices_other_shapes[i]))
    new_vertices_other_shapes = new_vertices_other_shapes_clockwise

    vertices_nested_again_shapes = []
    for i in range(len(new_vertices_other_shapes)):
        right_shape = new_vertices_other_shapes[i]
        max_y = maximum_y_coordinate(right_shape)
        min_y = minimum_y_coordinate(right_shape)
        min_x = minimum_x_coordinate(right_shape)
        max_x = maximum_x_coordinate(right_shape)
        left_side_coordinates = []
        for i in range(len(vertices_nested_again_shapes)):
            points_of_left_shape = []
            if right_shape == vertices_nested_again_shapes[i]:
                continue
            for j in range(len(vertices_nested_again_shapes[i])):
                if vertices_nested_again_shapes[i][j][0] <= min_x and vertices_nested_again_shapes[i][j][1] <= max_y and \
                        vertices_nested_again_shapes[i][j][1] >= min_y:
                    points_of_left_shape.append(vertices_nested_again_shapes[i][j])
            if len(points_of_left_shape) != 0:
                left_side_coordinates.append(vertices_nested_again_shapes[i])

        if len(left_side_coordinates) == 0 or len(left_side_coordinates) != 0:
            var_1 = 0
            var_3 = (-1, -1, -1)
            var_6 = (-1, -1, -1)
            var_4 = 10000
            for i in range(len(vertices_nested_again_shapes)):
                for j in range(len(vertices_nested_again_shapes[i])):
                    if vertices_nested_again_shapes[i][j][1] <= min_y and vertices_nested_again_shapes[i][j][0] <= min_x:
                        var_2 = vertices_nested_again_shapes[i][j]
                        if var_2[1] > var_1:
                            var_1 = var_2[1]
                            var_3 = var_2
                    if vertices_nested_again_shapes[i][j][1] >= max_y and vertices_nested_again_shapes[i][j][0] <= min_x:
                        var_5 = vertices_nested_again_shapes[i][j]
                        if var_5[1] < var_4:
                            var_4 = var_5[1]
                            var_6 = var_5
            if var_3 == (-1, -1, -1):
                left_side_coordinates = []
            else:
                for i in range(len(vertices_nested_again_shapes)):
                    for j in range(len(vertices_nested_again_shapes[i])):
                        if var_3 == vertices_nested_again_shapes[i][j] or var_6 == vertices_nested_again_shapes[i][j]:
                            left_side_coordinates.append(vertices_nested_again_shapes[i])
                            break

        # print("left_side_coordinates = ", left_side_coordinates)
        shortest_distance_x = 0
        for i in range(len(left_side_coordinates)):
            if maximum_y_coordinate(left_side_coordinates[i]) < min_y:
                continue
            if maximum_x_coordinate(left_side_coordinates[i]) > shortest_distance_x :
                shortest_distance_x = maximum_x_coordinate(left_side_coordinates[i])
        # print("shortest_distance_x = ",shortest_distance_x)

        right_shape_nested = []
        for i in range(len(right_shape)):
            if shortest_distance_x == 0:
                a = right_shape[i][0] + 1
            else:
                a = right_shape[i][0] - ((min_x - shortest_distance_x) - 1)
            right_shape_nested.append((a, right_shape[i][1], 0))
        vertices_nested_again_shapes.append(right_shape_nested)
    return vertices_nested_again_shapes

# def nested_shapes_coordinates_eff(new_vertices_other_shapes):
#     left_shape = []
#     right_shape = []
#     bottom_shape = []
#     top_shape = []
#     new_vertices_other_shapes_clockwise = []
#
#     for i in range(len(new_vertices_other_shapes)):
#         new_vertices_other_shapes_clockwise.append(clockwise_list(new_vertices_other_shapes[i]))
#     new_vertices_other_shapes = new_vertices_other_shapes_clockwise
#
#     vertices_nested_again_shapes = []
#     for i in range(len(new_vertices_other_shapes)):
#         right_shape = new_vertices_other_shapes[i]
#         max_y = maximum_y_coordinate(right_shape)
#         min_y = minimum_y_coordinate(right_shape)
#         min_x = minimum_x_coordinate(right_shape)
#         max_x = maximum_x_coordinate(right_shape)
#         left_side_coordinates = []
#         for i in range(len(vertices_nested_again_shapes)):
#             points_of_left_shape = []
#             if right_shape == vertices_nested_again_shapes[i]:
#                 continue
#             for j in range(len(vertices_nested_again_shapes[i])):
#                 if vertices_nested_again_shapes[i][j][0] <= min_x and vertices_nested_again_shapes[i][j][1] <= max_y and \
#                         vertices_nested_again_shapes[i][j][1] >= min_y:
#                     points_of_left_shape.append(vertices_nested_again_shapes[i][j])
#             if len(points_of_left_shape) != 0:
#                 left_side_coordinates.append(vertices_nested_again_shapes[i])
#
#         if len(left_side_coordinates) == 0 or len(left_side_coordinates) != 0:
#             var_1 = 0
#             var_3 = (-1, -1, -1)
#             var_6 = (-1, -1, -1)
#             var_4 = 10000
#             for i in range(len(vertices_nested_again_shapes)):
#                 for j in range(len(vertices_nested_again_shapes[i])):
#                     if vertices_nested_again_shapes[i][j][1] <= min_y and vertices_nested_again_shapes[i][j][0] <= min_x:
#                         var_2 = vertices_nested_again_shapes[i][j]
#                         if var_2[1] > var_1:
#                             var_1 = var_2[1]
#                             var_3 = var_2
#                     if vertices_nested_again_shapes[i][j][1] >= max_y and vertices_nested_again_shapes[i][j][0] <= min_x:
#                         var_5 = vertices_nested_again_shapes[i][j]
#                         if var_5[1] < var_4:
#                             var_4 = var_5[1]
#                             var_6 = var_5
#             if var_3 == (-1, -1, -1) :
#                 left_side_coordinates = []
#             else:
#                 for i in range(len(vertices_nested_again_shapes)):
#                     for j in range(len(vertices_nested_again_shapes[i])):
#                         if var_3 == vertices_nested_again_shapes[i][j] or var_6 == vertices_nested_again_shapes[i][j]:
#                             left_side_coordinates.append(vertices_nested_again_shapes[i])
#                             break
#
#         slope_points = []
#         for j in range(len(left_side_coordinates)):
#             for i in range(len(left_side_coordinates[j])):
#                 if i != len(left_side_coordinates[j]) - 1:
#                     ax1 = round(left_side_coordinates[j][i][0], 1)
#                     ay1 = round(left_side_coordinates[j][i][1], 1)
#                     ax2 = round(left_side_coordinates[j][i + 1][0], 1)
#                     ay2 = round(left_side_coordinates[j][i + 1][1], 1)
#                 else:
#                     ax1 = round(left_side_coordinates[j][i][0], 1)
#                     ay1 = round(left_side_coordinates[j][i][1], 1)
#                     ax2 = round(left_side_coordinates[j][0][0], 1)
#                     ay2 = round(left_side_coordinates[j][0][1], 1)
#                 if ax1 == ax2 and ay1 == ay2:
#                     continue
#                 elif ay1 == ay2:
#                     if ax1 < ax2:
#                         inc_value = ax1
#                         while inc_value != ax2:
#                             inc_value = round(inc_value + 0.1, 1)
#                             slope_points.append((inc_value, ay1, 0))
#                     else:
#                         inc_value = ax1
#                         while inc_value != ax2:
#                             inc_value = round(inc_value - 0.1, 1)
#                             slope_points.append((inc_value, ay1, 0))
#                 elif ax1 == ax2:
#                     if ay1 < ay2:
#                         inc_value = ay1
#                         while inc_value != ay2:
#                             inc_value = round(inc_value + 0.1, 1)
#                             slope_points.append((ax1, inc_value, 0))
#                     else:
#                         inc_value = ay1
#                         while inc_value != ay2:
#                             inc_value = round(inc_value - 0.1, 1)
#                             slope_points.append((ax1, inc_value, 0))
#                 elif ax1 != ax2 or ay1 != ay2:
#                     slope = (ay2 - ay1) / (ax2 - ax1)
#                     inc_value = ay1
#                     if ay2 > ay1:
#                         while (round(float(inc_value), 1) != ay2):
#                             inc_value = round(inc_value + 0.1, 1)
#                             obt_value = round(float((inc_value - ay1 + (slope * ax1)) / slope), 1)
#                             slope_points.append((obt_value, inc_value, 0))
#                     else:
#                         while (round(float(inc_value), 1) != ay2):
#                             inc_value = round(inc_value - 0.1, 1)
#                             obt_value = round(float((inc_value - ay1 + (slope * ax1)) / slope), 1)
#                             slope_points.append((obt_value, inc_value, 0))
#
#         x_for_right_shape ,y_for_right_shape= vertical_checking(right_shape)
#         min_points = area_at_the_left_of_given_piece(right_shape,x_for_right_shape,y_for_right_shape)
#
#         left_side_coordinates = []
#         for i in range(len(min_points) - 1):
#             ax1 = round(min_points[i][0], 1)
#             ay1 = round(min_points[i][1], 1)
#             ax2 = round(min_points[i + 1][0], 1)
#             ay2 = round(min_points[i + 1][1], 1)
#             if ax1 == ax2 and ay1 == ay2:
#                 continue
#             elif ay1 == ay2:
#                 if ax1 < ax2:
#                     inc_value = ax1
#                     while inc_value != ax2:
#                         left_side_coordinates.append((inc_value, ay1, 0))
#                         inc_value = round(inc_value + 0.1, 1)
#                     left_side_coordinates.append((ax2,ay1,0))
#                 else:
#                     inc_value = ax1
#                     while inc_value != ax2:
#                         left_side_coordinates.append((inc_value, ay1, 0))
#                         inc_value = round(inc_value - 0.1, 1)
#                     left_side_coordinates.append((ax2, ay1, 0))
#             elif ax1 == ax2:
#                 if ay1 < ay2:
#                     inc_value = ay1
#                     left_side_coordinates.append((ax1,ay1,0))
#                     while inc_value != ay2:
#                         inc_value = round(inc_value + 0.1, 1)
#                         left_side_coordinates.append((ax1, inc_value, 0))
#                 else:
#                     inc_value = ay1
#                     left_side_coordinates.append((ax1,ay1,0))
#                     while inc_value != ay2:
#                         inc_value = round(inc_value - 0.1, 1)
#                         left_side_coordinates.append((ax1, inc_value, 0))
#             elif ax1 != ax2 or ay1 != ay2:
#                 slope = (ay2 - ay1) / (ax2 - ax1)
#                 inc_value = ax1
#                 if ax2 > ax1:
#                     left_side_coordinates.append((ax1,ay1,0))
#                     while (round(float(inc_value), 1) != ax2):
#                         inc_value = round(inc_value + 0.1, 1)
#                         obt_value = round(float((slope * (inc_value - ax1)) + ay1), 1)
#                         left_side_coordinates.append((inc_value, obt_value, 0))
#                 else:
#                     left_side_coordinates.append((ax1,ay1,0))
#                     while (round(float(inc_value), 1) != ax2):
#                         inc_value = round(inc_value - 0.1, 1)
#                         obt_value = round(float((slope * (inc_value - ax1)) + ay1), 1)
#                         left_side_coordinates.append((inc_value, obt_value, 0))
#
#
#         short_distances = []
#         for i in range(len(slope_points)):
#             y_slope_point = round(slope_points[i][1], 1)
#             x_slope_point = round(slope_points[i][0], 1)
#             for j in range(len(left_side_coordinates)):
#                 y_min_point = round(left_side_coordinates[j][1], 1)
#                 x_min_point = round(left_side_coordinates[j][0], 1)
#                 if y_min_point == y_slope_point:
#                     short_distance = round(x_min_point - x_slope_point,1)
#                     short_distances.append(short_distance)
#
#         shortest_distance_x = min_x
#         for i in range(len(short_distances)):
#             if i == 0:
#                 shortest_distance_x = short_distances[i]
#             if short_distances[i] < shortest_distance_x:
#                 shortest_distance_x = short_distances[i]
#
#         right_shape_nested = []
#         for i in range(len(right_shape)):
#             if shortest_distance_x == 0:
#                 a = right_shape[i][0] + 1
#             else:
#                 a = right_shape[i][0] - (shortest_distance_x - 1)
#             right_shape_nested.append((a, right_shape[i][1], 0))
#         vertices_nested_again_shapes.append(right_shape_nested)
#     return vertices_nested_again_shapes

def gravity_approach(length_sheet, width_sheet, new_vertices_shapes, arranged_groups, invalid_shapes):
    new_vertices_other_shapes = []
    maximum_y_for_other_shape_for_new_column = 0
    maximum_y_for_other_shape_for_current_column = 0
    maximum_x_of_previous_column = 0
    first_shape_placed = 0
    for j in range(len(new_vertices_shapes)):
        maximum_y_compare = maximum_y_coordinate(new_vertices_shapes[j])
        if maximum_y_compare > maximum_y_for_other_shape_for_new_column:
            maximum_y_for_other_shape_for_new_column = maximum_y_compare
    for p in range(len(arranged_groups)):
        moved_other_shape = []
        intersection_with_previous_shapes = 0
        intersection_with_previous_other_shapes = 0
        if p == 0:
            # Use maximum y to place the circles and other shapes and check for intersection and sheet value
            other_shape_to_move = arranged_groups[p]
            vertical_movement_other_shape = width_sheet - (maximum_y_for_other_shape_for_new_column + 1)
            minimum_x_of_other_shape = minimum_x_coordinate(other_shape_to_move)
            horizontal_movement_other_shape = minimum_x_of_other_shape - 1
            for j in range(len(other_shape_to_move)):
                k = other_shape_to_move[j][0] - horizontal_movement_other_shape
                l = other_shape_to_move[j][1] - vertical_movement_other_shape
                moved_other_shape.append((round(k, 2), round(l, 2), 0))

            # Checking the intersection of current shape with previously placed shapes
            for j in range(len(new_vertices_shapes)):
                if intersection_of_shapes(new_vertices_shapes[j],moved_other_shape) == True:
                    intersection_with_previous_shapes = 1

            # Placing the shapes if no intersections exist
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

                if invalid == 1:
                    invalid_shapes.append(arranged_groups[p])

        if p != 0:
            # Use maximum y to place the circles and other shapes and check for intersection and sheet value
            other_shape_to_move = arranged_groups[p]
            if first_shape_placed == 1:
                maximum_y_for_other_shape_for_current_column = maximum_y_coordinate(new_vertices_other_shapes[len(new_vertices_other_shapes)-1])
            else:
                maximum_y_for_other_shape_for_current_column = maximum_y_for_other_shape_for_new_column
            minimum_x_of_other_shape = minimum_x_coordinate(other_shape_to_move)
            horizontal_movement_other_shape = minimum_x_of_other_shape - (maximum_x_of_previous_column + 1)
            vertical_movement_other_shape = width_sheet - (maximum_y_for_other_shape_for_current_column + 1)
            for j in range(len(other_shape_to_move)):
                k = other_shape_to_move[j][0] - horizontal_movement_other_shape
                l = other_shape_to_move[j][1] - vertical_movement_other_shape
                moved_other_shape.append((round(k, 2), round(l, 2), 0))

            # Checking the intersection of current shape with previously placed shapes
            for j in range(len(new_vertices_shapes)):
                if intersection_of_shapes(new_vertices_shapes[j], moved_other_shape) == True:
                    intersection_with_previous_shapes = 1

            for j in range(len(new_vertices_other_shapes)):
                if intersection_of_shapes(new_vertices_other_shapes[j], moved_other_shape) == True:
                    intersection_with_previous_other_shapes = 1

            # Placing the shapes if no intersections exist
            if intersection_with_previous_shapes == 0 and intersection_with_previous_other_shapes == 0:
                for j in range(len(moved_other_shape)):
                    invalid = 0
                    if (((moved_other_shape[j][0] > length_sheet) or (
                            moved_other_shape[j][1] > width_sheet)) and invalid == 0):
                        invalid = 1
                        break
                if invalid == 0:
                    new_vertices_other_shapes.append(moved_other_shape)
                # Trying to nest the shape with maximum values of previous shapes as the last option
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

                    # Checking for intersection again with other shapes
                    for j in range(len(new_vertices_shapes)):
                        if intersection_of_shapes(new_vertices_shapes[j], moved_other_shape) == True:
                            intersection_with_previous_shapes = 1

                    # Final placement of invalid shapes (those which were not placed previously)
                    if intersection_with_previous_shapes == 0:
                        for j in range(len(moved_other_shape)):
                            invalid = 0
                            if (((moved_other_shape[j][0] > length_sheet) or (
                                    moved_other_shape[j][1] > width_sheet)) and invalid == 0):
                                invalid = 1
                                break
                        if invalid == 0:
                            new_vertices_other_shapes.append(moved_other_shape)
                        if invalid == 1:
                            invalid_shapes.append(moved_other_shape)
    return new_vertices_other_shapes


def print_func_1(new_vertices_shapes, invalid_shapes, grouped_nested_shapes):
    if len(invalid_shapes) == 1 and len(new_vertices_shapes) != 1:
        print("There is an unplaced shape and", len(new_vertices_shapes),
              "shapes have been placed in the sheet successfully.")
    if len(new_vertices_shapes) == 1 and len(invalid_shapes) != 1:
        print("There are", len(invalid_shapes),
              "unplaced shapes and one shape has been placed in the sheet successfully.")
    if len(invalid_shapes) == 1 and len(new_vertices_shapes) == 1:
        print("There is an unplaced shape and one shape has been placed in the sheet successfully.")
    if len(new_vertices_shapes) != 1 and len(invalid_shapes) != 1:
        print("There are", len(invalid_shapes), "unplaced shapes and", len(new_vertices_shapes),
              "shapes have been placed in the sheet successfully.")
    print("-----------------------------------------------")
    print("Vertices of invalid shapes:", invalid_shapes)
    print("-----------------------------------------------")
    print("Final vertices for shapes: ", grouped_nested_shapes)
    print("-----------------------------------------------")


def print_func_2(new_vertices_shapes, invalid_shapes):
    if len(invalid_shapes) == 1 and len(new_vertices_shapes) != 1:
        print("There is an unplaced shape and", len(new_vertices_shapes),
              "shapes have been placed in the sheet successfully.")
    if len(new_vertices_shapes) == 1 and len(invalid_shapes) != 1:
        print("There are", len(invalid_shapes),
              "unplaced shapes and one shape has been placed in the sheet successfully.")
    if len(invalid_shapes) == 1 and len(new_vertices_shapes) == 1:
        print("There is an unplaced shape and one shape has been placed in the sheet successfully.")
    if len(new_vertices_shapes) != 1 and len(invalid_shapes) != 1:
        print("There are", len(invalid_shapes), "unplaced shapes and", len(new_vertices_shapes),
              "shapes have been placed in the sheet successfully.")
    print("-----------------------------------------------")
    print("Vertices of invalid shapes:", invalid_shapes)
    print("-----------------------------------------------")
    print("Final vertices for shapes: ", new_vertices_shapes)
    print("-----------------------------------------------")


def dxf_calculations(msp, length_sheet, width_sheet):
    list_for_start_end_points = []
    vertices_shapes_circle = []
    polyline = 0
    vertices_shapes_1 = []
    for e in msp:
        if e.dxftype() == "LWPOLYLINE":
            lines = msp.query('LWPOLYLINE')
            points = polyline
            first_point = lines[points]
            list_polyline = []
            for i in range(len(first_point)):
                x = round(first_point[i][0], 2)
                y = round(first_point[i][1], 2)
                list_polyline.append((x, y, 0))
            polyline = polyline + 1
            list_for_start_end_points.append([list_polyline[0], list_polyline[len(list_polyline) - 1]])
            vertices_shapes_1.append(clockwise_list(list_polyline))

        elif (e.dxftype() == "LINE"):
            list_line = []
            list_line.append((round(e.dxf.start[0], 2), round(e.dxf.start[1], 2), round(e.dxf.start[2], 2)))
            list_line.append((round(e.dxf.end[0], 2), round(e.dxf.end[1], 2), round(e.dxf.end[2], 2)))
            list_for_start_end_points.append([list_line[0], list_line[1]])
            vertices_shapes_1.append(clockwise_list(list_line))

        elif (e.dxftype() == "CIRCLE"):
            radius = e.dxf.radius
            area_through_radius = (pi * radius * radius)
            angle = 1
            times = 360 / angle
            x = e.dxf.center[0]
            y = e.dxf.center[1]
            theta = 0
            circle_area = 0
            # Developing a polygon which contains 360 sides and also resembles circle completely
            Circle_shape = []
            for i in range(int(times)):
                point_circle = (round(x + ((radius) * sin(theta * (pi / 180))), 2),
                                round(y + ((radius) * cos(theta * (pi / 180))), 2), 0)
                Circle_shape.append(point_circle)
                theta = theta + angle
            vertices_shapes_circle.append(clockwise_list(Circle_shape))

        elif (e.dxftype() == "ARC"):
            x = e.dxf.center[0]
            y = e.dxf.center[1]
            radius_arc = e.dxf.radius
            start_angle = e.dxf.start_angle
            end_angle = e.dxf.end_angle
            if end_angle > start_angle:
                if round(end_angle - start_angle, 5) <= 90:
                    times = 5
                    theta_arc = start_angle
                    angle_arc = (end_angle - start_angle) / 5
                if end_angle - start_angle >= 90 or end_angle - start_angle <= 180:
                    times = 20
                    theta_arc = start_angle
                    angle_arc = (end_angle - start_angle) / 20
                if end_angle - start_angle >= 180 or end_angle - start_angle <= 270:
                    times = 30
                    theta_arc = start_angle
                    angle_arc = (end_angle - start_angle) / 30
                if end_angle - start_angle > 270:
                    times = 40
                    theta_arc = start_angle
                    angle_arc = (end_angle - start_angle) / 40

            else:
                times = 25
                theta_arc = end_angle
                angle_arc = -((360 - start_angle) + end_angle) / 25
            arc_shape = []

            for i in range(int(times + 1)):
                F = round(x + (radius_arc * cos(theta_arc * (pi / 180))), 2)
                E = round(y + (radius_arc * sin(theta_arc * (pi / 180))), 2)
                theta_arc = theta_arc + angle_arc
                arc_shape.append((F, E, 0))
            arc_shape = clockwise_list(arc_shape)
            list_for_start_end_points.append([arc_shape[0], arc_shape[len(arc_shape) - 1]])
            vertices_shapes_1.append(clockwise_list(arc_shape))

    shape_1 = []
    pre_grp_indices = []
    main_shp_indices = []
    for i in range(len(list_for_start_end_points)):
        sp_1_x = truncate(list_for_start_end_points[i][0][0], 1)
        sp_1_y = truncate(list_for_start_end_points[i][0][1], 1)
        ep_1_x = truncate(list_for_start_end_points[i][1][0], 1)
        ep_1_y = truncate(list_for_start_end_points[i][1][1], 1)
        sp_1 = (sp_1_x, sp_1_y)
        ep_1 = (ep_1_x, ep_1_y)
        if i not in main_shp_indices:
            shape_1.append(i)
            main_shp_indices.append(i)
        for j in range(len(list_for_start_end_points)):
            sp_2_x = truncate(list_for_start_end_points[j][0][0], 1)
            sp_2_y = truncate(list_for_start_end_points[j][0][1], 1)
            ep_2_x = truncate(list_for_start_end_points[j][1][0], 1)
            ep_2_y = truncate(list_for_start_end_points[j][1][1], 1)
            sp_2 = (sp_2_x, sp_2_y)
            ep_2 = (ep_2_x, ep_2_y)
            if i != j:
                if sp_1 == sp_2 or sp_1 == ep_2 or ep_1 == sp_2 or ep_1 == ep_2:  # or (ep_1_x- ep_2_x <= 0.1) or (ep_1_x- ep_2_x <= -0.1) or (ep_1_y- ep_2_y <= 0.1) or (ep_1_y- ep_2_y <= -0.1) or (sp_1_x - sp_2_x <= 0.1) or (sp_1_x - sp_2_x <= -0.1) or (sp_1_y - sp_2_y <= 0.1) or (sp_1_y - sp_2_y <= -0.1) or (ep_1_x - sp_2_x <= 0.1) or (ep_1_x - sp_2_x <= -0.1) or (ep_1_y - sp_2_y <= 0.1) or (ep_1_y - sp_2_y <= -0.1):
                    shape_1.append(j)
        pre_grp_indices.append(sorted(shape_1))
        shape_1 = []

    temp_union_ind_list = []
    temp_union_ind_list_again = []
    for i in range(len(pre_grp_indices)):
        temp_shape1 = set(pre_grp_indices[i])
        temp_shape3 = pre_grp_indices[i]
        for j in range(len(pre_grp_indices)):
            temp_shape2 = set(pre_grp_indices[j])
            temp_shape4 = pre_grp_indices[j]
            if len(temp_shape1.intersection(temp_shape2)) > 0:
                temp_shape3 = list(set().union(temp_shape3, temp_shape4))
                temp_shape1 = set(temp_shape3)
        for k in range(len(pre_grp_indices)):
            temp_shape2 = set(pre_grp_indices[k])
            temp_shape4 = pre_grp_indices[k]
            if len(temp_shape1.intersection(temp_shape2)) > 0:
                temp_shape3 = list(set().union(temp_shape3, temp_shape4))
                temp_shape1 = set(temp_shape3)
        if temp_shape3 not in temp_union_ind_list:
            temp_union_ind_list.append(temp_shape3)

    for i in range(len(temp_union_ind_list)):
        temp_shape1 = set(temp_union_ind_list[i])
        temp_shape3 = temp_union_ind_list[i]
        for j in range(len(temp_union_ind_list)):
            temp_shape2 = set(temp_union_ind_list[j])
            temp_shape4 = temp_union_ind_list[j]
            if len(temp_shape1.intersection(temp_shape2)) > 0:
                temp_shape3 = list(set().union(temp_shape3, temp_shape4))
                temp_shape1 = set(temp_shape3)
        for k in range(len(temp_union_ind_list)):
            temp_shape2 = set(temp_union_ind_list[k])
            temp_shape4 = temp_union_ind_list[k]
            if len(temp_shape1.intersection(temp_shape2)) > 0:
                temp_shape3 = list(set().union(temp_shape3, temp_shape4))
                temp_shape1 = set(temp_shape3)
        if temp_shape3 not in temp_union_ind_list_again:
            temp_union_ind_list_again.append(temp_shape3)

    union_ind_list = []
    for i in range(len(temp_union_ind_list_again)):
        if i == 0:
            union_ind_list.append(temp_union_ind_list_again[i])
            continue
        temp_var = 0
        for k in range(len(union_ind_list)):
            if temp_union_ind_list_again[i][0] in union_ind_list[k]:
                temp_var = 1
        if temp_var == 0 and (temp_union_ind_list_again[i] not in union_ind_list):
            union_ind_list.append(temp_union_ind_list_again[i])

    start_end_points = []
    ind_ver_list = []
    union_ver_list = []
    for i in range(len(union_ind_list)):
        temp_start_end_points = []
        for j in range(len(union_ind_list[i])):
            index_value = union_ind_list[i][j]
            random_list = vertices_shapes_1[int(index_value)]
            temp_start_end_points.append([random_list[0], random_list[len(random_list) - 1]])
            for k in range(len(random_list)):
                ind_ver_list.append(random_list[k])
        union_ver_list.append(clockwise_list(ind_ver_list))
        start_end_points.append(temp_start_end_points)
        ind_ver_list = []

    appending_indices = []
    seq_ind = []
    for i in range(len(start_end_points)):
        appending_indices = []
        for j in range(len(start_end_points[i])):
            if j == 0:
                appending_indices.append(union_ind_list[i][0])
                appending_st_en_pts = start_end_points[i][0]
                st_pt_1 = (truncate(appending_st_en_pts[0][0], 1), truncate(appending_st_en_pts[0][1], 1))
                en_pt_1 = (truncate(appending_st_en_pts[1][0], 1), truncate(appending_st_en_pts[1][1], 1))
            if j != 0:
                last_index = appending_indices[len(appending_indices) - 1]
                real_index_value = union_ind_list[i].index(last_index)
                appending_st_en_pts = start_end_points[i][real_index_value]
                st_pt_1 = (truncate(appending_st_en_pts[0][0], 1), truncate(appending_st_en_pts[0][1], 1))
                en_pt_1 = (truncate(appending_st_en_pts[1][0], 1), truncate(appending_st_en_pts[1][1], 1))
            for k in range(len(start_end_points[i])):
                if (union_ind_list[i][k] in appending_indices) == True:
                    continue
                st_pt_2 = (truncate(start_end_points[i][k][0][0], 1), truncate(start_end_points[i][k][0][1], 1))
                en_pt_2 = (truncate(start_end_points[i][k][1][0], 1), truncate(start_end_points[i][k][1][1], 1))
                if en_pt_1 == st_pt_2:  # or (en_pt_1[0] - st_pt_2[0] <= 0.1) or (en_pt_1[0] - st_pt_2[0] <= -0.1) or (en_pt_1[1] - st_pt_2[1] <= 0.1) or (en_pt_1[1] - st_pt_2[1] <= -0.1):
                    appending_indices.append(union_ind_list[i][k])
                    break
                if en_pt_1 == en_pt_2 or st_pt_1 == st_pt_2:  # or (en_pt_1[0]- en_pt_2[0] <= 0.1) or (en_pt_1[0]- en_pt_2[0] <= -0.1) or (en_pt_1[1]- en_pt_2[1] <= 0.1) or (en_pt_1[1]- en_pt_2[1] <= -0.1) or st_pt_1 == st_pt_2 or (st_pt_1[0] - st_pt_2[0] <= 0.1) or (st_pt_1[0] - st_pt_2[0] <= -0.1) or (st_pt_1[1] - st_pt_2[1] <= 0.1) or (st_pt_1[1] - st_pt_2[1] <= -0.1):
                    start_end_points[i][k] = anticlockwise_list(start_end_points[i][k])
                    vertices_shapes_1[union_ind_list[i][k]] = anticlockwise_list(
                        vertices_shapes_1[union_ind_list[i][k]])
                    st_pt_2 = (truncate(start_end_points[i][k][0][0], 1), truncate(start_end_points[i][k][0][1], 1))
                    en_pt_2 = (truncate(start_end_points[i][k][1][0], 1), truncate(start_end_points[i][k][1][1], 1))
                    if en_pt_1 == st_pt_2:  # or (en_pt_1[0] - st_pt_2[0] <= 0.1) or (en_pt_1[0] - st_pt_2[0] <= -0.1) or (en_pt_1[1] - st_pt_2[1] <= 0.1) or (en_pt_1[1] - st_pt_2[1] <= -0.1):
                        appending_indices.append(union_ind_list[i][k])
                        break
                    else:
                        start_end_points[i][k] = anticlockwise_list(start_end_points[i][k])
                        vertices_shapes_1[union_ind_list[i][k]] = anticlockwise_list(
                            vertices_shapes_1[union_ind_list[i][k]])
                        st_pt_2 = (truncate(start_end_points[i][k][0][0], 1), truncate(start_end_points[i][k][0][1], 1))
                        en_pt_2 = (truncate(start_end_points[i][k][1][0], 1), truncate(start_end_points[i][k][1][1], 1))

        seq_ind.append(appending_indices)
        appending_indices = []
    vertices_shapes = []
    for k in range(len(seq_ind)):
        temp_list_shape = []
        for m in range(len(seq_ind[k])):
            list_shape = vertices_shapes_1[seq_ind[k][m]]
            for n in range(len(list_shape)):
                if list_shape[n] not in temp_list_shape:
                    temp_list_shape.append(list_shape[n])
            list_shape = []
        vertices_shapes.append(temp_list_shape)

    vertices_shapes_1 = vertices_shapes
    for j in range(len(vertices_shapes_circle)):
        vertices_shapes_1.append(vertices_shapes_circle[j])
    vertices_shapes_2 = []
    for i in range(len(vertices_shapes_1)):
        temp_shape = []
        for j in range(len(vertices_shapes_1[i])):
            temp_shape.append([vertices_shapes_1[i][j][0], vertices_shapes_1[i][j][1]])
        vertices_shapes_2.append(temp_shape)

    shape = []
    c = ["a%d" % x for x in range(1, len(vertices_shapes_2) + 1)]
    for x in range(len(c)):  # you can loop over them
        c[x] = np.array(vertices_shapes_2[x])
        y = c[x]
        p = Polygon(y, facecolor='none', edgecolor='b')
        shape.append(p)
    fig, ax = plt.subplots()
    c = ["%d" % x for x in range(1, len(shape) + 1)]
    for x in range(len(c)):
        ax.text(vertices_shapes_2[x][0][0], vertices_shapes_2[x][0][1], str(c[x]), style='italic')
        ax.add_patch(shape[x])
    ax.set_xlim([0, width_sheet])
    ax.set_ylim([0, length_sheet])
    plt.show()
    return vertices_shapes

def anticlockwise_list(list_shape2):
    list_shape1 = []
    for i in range(len(list_shape2)):
        list_shape1.append(list_shape2[len(list_shape2) - 1 - i])  # list_shape1 = clockwise arrangement of co-ordinates
    return list_shape1


def truncate(number, decimals=0):
    """
    Returns a value truncated to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor
