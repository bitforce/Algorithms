def merge(arr, left, mid, right):
    llen = mid - left + 1
    rlen = right - mid
    larr = [0] * (llen)
    rarr = [0] * (rlen)
    for i in range(0, llen):
        larr[i] = arr[left + i]
    for j in range(0, rlen):
        rarr[j] = arr[mid + 1 + j]
    i = 0
    j = 0
    k = left
    while i < llen and j < rlen:
        if larr[i] <= rarr[j]:
            arr[k] = larr[i]
            i += 1
        else:
            arr[k] = rarr[j]
            j += 1
        k += 1
    while i < llen:
        arr[k] = larr[i]
        i += 1
        k += 1
    while j < rlen:
        arr[k] = rarr[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + (right - 1)) / 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
