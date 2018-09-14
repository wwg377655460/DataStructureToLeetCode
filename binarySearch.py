import random
import time

from utils.MyUtil import generate_ordered_array


def binary_search(arr, n, target):
    l, r = 0, n - 1  # search in [l...r]
    while l <= r:  # while l==r, this array has one element
        mid = (l + r) // 2 # bug 容易超出整形的范围
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1


if __name__ == "__main__":
    n = 10000000
    arr = generate_ordered_array(n)

    target = random.randint(0, n)

    start_time = time.clock()

    index = binary_search(arr, n, target)

    end_time = time.clock()

    print('Running time: {} Seconds'.format(end_time - start_time))
    print(index)
