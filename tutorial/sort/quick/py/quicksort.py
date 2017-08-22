def partition(array, low, high):  # A.1
    # A.2
    i = low - 1
    pivot = array[high]
    for j in range(low, high):  # A.3
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]  # A.4
    return i + 1


def sort(array, low, high):  # A.5
    if low < high:  # A.6
        part = partition(array, low, high)
        sort(array, low, part - 1)
        sort(array, part + 1, high)


def quicksort(array):  # A.7
    sort(array, 0, len(array) - 1)
