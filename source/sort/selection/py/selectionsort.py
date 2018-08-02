def selection_sort(A):
    for i in range(len(A)):
        mini = min(A[i:])
        mindex = A[i:].index(mini)
        A[i + mindex] = A[i]
        A[i] = mini
