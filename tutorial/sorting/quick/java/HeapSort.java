class HeapSort {
    public static void heapify(int[] arr, int size, int idx) {
        int largest = idx;
        int left = 2 * idx + 1;
        int right = 2 * idx + 2;
        if (left < size && arr[left] > arr[largest])
            largest = left;
        if (right < size && arr[right] > arr[largest])
            largest = right;
        if (largest != idx) {
            int swap = arr[idx];
            arr[idx] = arr[largest];
            arr[largest] = swap;
            heapify(arr, size, largest);
        }
    }
    public static void heapSort(int[] arr) {
        int len = arr.length;
        for(int i = len / 2; i >= 0; i--)
            heapify(arr, len, i);
        for(int i = len - 1; i >= 0; i--) {
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;
            heapify(arr, i, 0);
        }
    }
}
