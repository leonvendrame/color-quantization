#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools
import numpy as np
import cv2 as ocv
import random

def minor_distance(pixel, sets):
    minor_distance_set = sets[0]
    minor_distance = 9999999
    for _set in sets:
        distance = np.linalg.norm(pixel-_set)
        if minor_distance > distance:
            minor_distance = distance
            minor_distance_set = _set

    return minor_distance_set

def main():
    color_number = sys.argv[1]
    image_name = sys.argv[2]
    image = ocv.imread(image_name, 1)
    # ocv.imshow("image", image)
    # ocv.waitKey(0)
    # ocv.destroyAllWindows()

    red = np.linspace(0, 255, 3)
    green = np.linspace(0, 255, 3)
    blue = np.linspace(0, 255, 3)

    sets = list(itertools.product(blue, green, red))
    sets = np.array(sets)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image[i][j] = minor_distance(image[i][j], sets)

    ocv.imshow("image", image)
    ocv.waitKey(0)
    ocv.destroyAllWindows()

    # cv2.imwrite('messigray.png',img)

if __name__ == "__main__":
    main()