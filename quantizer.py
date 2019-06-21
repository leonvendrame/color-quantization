import numpy as np
from helpers import factor3, aprox, argmedian


def simple(img, n):
    nums = factor3(n)
    m = np.amax(img) + 1
    rgb = np.zeros(img.shape, 'uint8')

    for i, num in enumerate(nums):
        aux = np.uint8(img[..., i] * float(num / m))
        rgb[..., i] = np.uint8(
            127 if num == 1 else (aux / (num - 1.)) * 255)

    return rgb


def uniform(img, n):
    nums = factor3(n)

    a = np.linspace(0, 255, num=nums[0], dtype=int)
    b = np.linspace(0, 255, num=nums[1], dtype=int)
    c = np.linspace(0, 255, num=nums[2], dtype=int)

    scheme = np.array(np.meshgrid(a, b, c)).T.reshape(-1, 3)

    return aprox(img, scheme).astype('uint8')


def median_cut(img, n):
    bucket = []
    scheme = []
    dispersal = []

    colors = np.concatenate(img[:, :], axis=0)
    colors = np.unique(colors, axis=0)

    for i in range(3):
        dispersal.append(np.amax(colors[:, i]) - np.amin(colors[:, i]))

    dispersal_key = dispersal.index(max(dispersal))
    colors = sorted(colors, key=lambda x: x[dispersal_key])

    bucket.append(colors)

    while len(bucket) < n:
        size = len(bucket)
        new_bucket = []
        for i in range(size):
            bk = np.array(bucket[i], int)
            middle = argmedian(bk, dispersal_key)
            a = bk[:middle]
            b = bk[middle:]
            new_bucket.append(a)
            new_bucket.append(b)
        del bucket
        bucket = new_bucket

    for i in range(len(bucket)):
        bk = np.array(bucket[i], int)
        middle = argmedian(bk, dispersal_key)
        scheme.append(bk[middle])

    del bucket

    return aprox(img, scheme).astype('uint8')
