#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import cv2 as cv
import argparse
import quantizer as qnt
from helpers import psnr


def read_args():
    parser = argparse.ArgumentParser(
        description='Performs image color quantization.')
    parser.add_argument('-i', dest='input', type=str,
                        help='Input image path', required=True)
    parser.add_argument('-o', dest='output', type=str,
                        help='Output image path to write the result')
    parser.add_argument('-a', dest='alg', type=str, choices=['simple', 'uniform', 'mediancut'],
                        default='uniform', help='Quantization algorithm to be used.')
    parser.add_argument('-n', dest='number', type=int, default='256',
                        help='Number of colors to be used in quantization.')
    return parser.parse_args()


def main():
    args = read_args()
    img_path = args.input
    alg = args.alg
    n = args.number

    img = cv.imread(img_path)

    if alg == 'simple':
        img_qnt = qnt.simple(img, n)
    elif alg == 'uniform':
        img_qnt = qnt.uniform(img, n)
    else:
        img_qnt = qnt.median_cut(img, n)

    if args.output is not None:
        cv.imwrite(args.output, img_qnt)

    cpsrn = psnr(img, img_qnt)
    print('Color Peak Signal to Noise-Ratio: %f' % cpsrn)

    cv.imshow('img input', img)
    cv.imshow('img output', img_qnt)

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
