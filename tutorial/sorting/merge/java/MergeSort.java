class MergeSort {
    public static void merge(int[] arr, int left, int mid, int right) {
        int llen = mid - left + 1;
        int rlen = right - mid;
        int larr[] = new int [llen];
        int rarr[] = new int [rlen];
        for (int i = 0; i < llen; ++i)
            larr[i] = arr[left + i];
        for (int j = 0; j < rlen; ++j)
            rarr[j] = arr[mid + 1 + j];
        int k = left;
        int i = 0;
        int j = 0;
        while (i < llen && j < rlen) {
            if (larr[i] <= rarr[j]) {
                arr[k] = larr[i];
                i++;
            } else {
                arr[k] = rarr[j];
                j++;
            }
            k++;
        }
        while (i < llen) {
            arr[k] = larr[i];
            i++;
            k++;
        }
        while (j < rlen) {
            arr[k] = rarr[j];
            j++;
            k++;
        }
    }
    public static void mergeSort(int[] arr, int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;
            mergeSort(arr, left, mid);
            mergeSort(arr , mid + 1, right);
            merge(arr, left, mid, right);
        }
    }
}
