def bubblesort(A):
    for i in range(len(A)):
        for j in range(len(A) - 1):
            if(A[j] > A[i]):
                tmp = A[j]
                A[j] = A[i]
                A[i] = tmp
