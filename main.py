#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools
import numpy as np
import cv2 as ocv
import random

def minor_distance(image, sets):
    print(None)
    #calcular distancia

def main():
    color_number = sys.argv[1]
    image_name = sys.argv[2]
    image = ocv.imread(image_name, 1)
    # ocv.imshow("image", image)
    # ocv.waitKey(0)
    # ocv.destroyAllWindows()

    red = np.linspace(0, 255, 5)
    green = np.linspace(0, 255, 3)
    blue = np.linspace(0, 255, 2)

    sets = list(itertools.product(blue, green, red))
    sets = np.array(sets)

    image[1:100:1,1:100:1] = sets[np.random.randint(0, 28)]
    # for i in f:
    #     print(i)

    # image[:,:] = minor_distance

    ocv.imshow("image", image)
    ocv.waitKey(0)
    ocv.destroyAllWindows()

    # cv2.imwrite('messigray.png',img)

if __name__ == "__main__":
    main()