#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools
import numpy as np
import cv2 as ocv

def main():
    color_number = sys.argv[1]
    image_name = sys.argv[2]
    image = ocv.imread(image_name, 1)
    # ocv.imshow("image", image)
    # ocv.waitKey(0)
    # ocv.destroyAllWindows()

    a = np.linspace(0, 255, 5)
    b = np.linspace(0, 255, 3)
    c = np.linspace(0, 255, 2)

    sets = list(itertools.product(a, b, c))
    for i in range(len(sets)):
        sets[i] = list(sets[i])

    print(len(sets))


    # print(a, b)
    # print(d)
    # cv2.imwrite('messigray.png',img)

if __name__ == "__main__":
    main()