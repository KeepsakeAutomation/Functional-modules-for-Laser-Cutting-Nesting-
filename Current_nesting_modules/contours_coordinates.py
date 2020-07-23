import cv2
import matplotlib.pyplot as plt
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from math import sqrt, sin, cos, pi, asin



def image(img):
    # convert to RGB
    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    image = cv2.flip(image, 0)
    # convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # create a binary thresholded image
    _, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
    list1 = []
    list2 = []
    plt.imshow(gray)
    plt.show()
    # find the contours from the thresholded image
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
        list1 = []
        for j in range(len(contours[i])):
            for k in range(len(contours[i][j])):
                a = contours[i][j][k][0]
                b = contours[i][j][k][1]
                c = a, b, 0
                list1.append(c)
        list2.append(list1)
    # font
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Using cv2.putText() method
    for i in range(len(list2)):
        text = str(i + 1)
        org = list2[i][0][0], list2[i][0][1] - 3
        image = cv2.putText(image, text, org, font, fontScale=0.8, color=(0, 0, 255), thickness=1)
    image = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
        # show the image with the drawn contours
    plt.imshow(image)
    plt.show()
    return list2
