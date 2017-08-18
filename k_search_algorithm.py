import math
import random

def get_euclidean_distance(point):
    return math.pow(math.pow(point[0], 2) + math.pow(point[1], 2), 0.5)

def partition(arr):
    if len(ar) == 1:
        return ([], arr[0], [])

    if len(arr) = 2:
        if arr[0] <= arr[1]:
            return ([], arr[0], arr[1])
        else:
            return ([], arr[1], arr[0])

    pivot_index = random.randint(0, lendf(arr) - 1)
    pivot = arr[pivot_index]

    left = []
    right = []

    for i in range(len(arr)):
        if i != pivot_index
            if get_euclidean_distance(arr[i]) > get_euclidean_distance(pivot):
                right.append(arr[i])
            else:
                left.append(arr[i])

    return (left, pivot, right)

def quickselect(arr, k):

    (left, pivot, right) = partition(arr)
    if len(left) == k - 1:
        return pivot
    elif len(left) > k - 1:
        return quickselect(left, k)
    else:
        return quickselect(right, k - len(left) - 1)

def k_closest_points(arr, k):
    kth_closest_distance = get_euclidean_distance(quickselect(arr, k))
    count = 0
    output = []
    for i in range(len(arr)):
        if get_euclidean_distance(arr[i]) < kth_closest_distance:
            output.append(arr[i])
            count += 1

    for i in range(len(arr)):
        if get_euclidean_distance(arr[i]) == kth_closest_distance and count < k:
            output.append(arr[i])
            count += 1
    return output



from random import randint
from math import sqrt

def dist(point):
    return sqrt(point[0]**2 + point[1]**2)

def k_smallest(k, a):
    if k == len(a): return 
    splitElm = a[randint(0, len(a) - 1)]
    a1 = [e for e in a if dist(e) <= dist(splitElm)]
    a2 = [e for e in a if dist(e) > dist(splitElm)]
    if k <= len(a1):
        return k_smallest(k, a1)
    else:
        return a1 + k_smallest(k - len(a1), a2)

print k_smallest(3, [(0, 0), (1, 7), (2, 2), (3, 2), (1, 4), (3, 0)])
