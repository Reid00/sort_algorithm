import random
import numpy as np


def merge_sort(list):
    if len(list) < 2:
        return list
    mid = int(len(list) // 2)
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge(left, right)


# def merge(left, right):
#     res = []
#     i, j = 0, 0
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#
#     res += left[i:]
#     res += right[j:]
#     return res

def merge(left, right):
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    res = res + left + right
    return res


if __name__ == '__main__':
    # list = np.random.randint(1, 100, 15)
    list = [15, 2, 6, 18, 3, 7]
    print('排序前:', list)
    print('排序后：', merge_sort(list))
