def binary_search(arr, value):
    size = len(arr) - 1
    start = 0
    end = size
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == value:
            return mid
        if value > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    if start > end:
        return None


values = [2, 7, 19, 34, 53, 72]
binary_search(values, 34)


def interpolation_search(arr, search_for):
    start = 0
    end = len(arr) - 1
    while start <= end and arr[start] <= search_for <= arr[end]:
        probe = start + \
                int(((float(end - start) / (arr[end] - arr[start]))
                     * (search_for - arr[start])))
        if arr[probe] == search_for:
            return "Found" + str(search_for) + " at index " + str(probe)
        if arr[probe] < search_for:
            start = probe + 1
        if arr[probe] > search_for:
            end = probe - 1
    return "Searched element not in the list"


l = [2, 7, 11, 19, 34, 53, 72]

print(interpolation_search(l, 11))
