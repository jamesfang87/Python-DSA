def bubble_sort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]


def selection_sort(list):
    for i in range(len(list)):
        idx = i
        for j in range(i+1, len(list)):
            if list[idx] > list[j]:
                idx = j
        list[i], list[idx] = list[idx], list[i]


def insertion_sort(list):
    for i in range(1, len(list)):
        value = list[i]
        position = i
        while position > 0 and list[position - 1]:
            list[position] = list[position - 1]
            position = position - 1
        list[position] = value


def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
        return result


def mergesort(array):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    return merge(
    left=mergesort(array[:midpoint]),
    right=mergesort(array[midpoint:]))


from random import randint


def quicksort(array):
    if len(array) < 2:
        return array
    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)]
    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    return quicksort(low) + same + quicksort(high)
