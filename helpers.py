import numpy as np


def factor3(n):
    if n <= 1:
        return 1, 1, 1

    c = n
    nums = []
    for i in range(2, n + 1):
        while c % i == 0:
            nums.append(i)
            c /= i

    if len(nums) == 1:
        nums = [nums[0], 1, 1]
    elif len(nums) == 2:
        nums = [nums[0], nums[1], 1]
    elif len(nums) > 3:
        while len(nums) > 3:
            i1 = np.argmin(nums)
            n1 = nums[i1]
            nums.pop(i1)
            i2 = np.argmin(nums)
            nums[i2] *= n1

    return nums


def aprox(img, scheme):
    scheme = np.array(scheme).reshape(-1, 3)
    distance = np.linalg.norm(img[:, :, None] - scheme[None, None, :], axis=3)
    scheme_indexes = np.argmin(distance, axis=2)
    return scheme[scheme_indexes]


def argmedian(array, column):
    return np.argsort(array[:, column])[len(array) // 2]


def psnr(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * np.math.log10(PIXEL_MAX / np.math.sqrt(mse))
