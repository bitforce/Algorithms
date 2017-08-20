class QuickSort {
    private int partition(int[] array, int low, int high) { // A.1
        // A.2.2J
        int pivot = array[high];
        int i = low - 1;
        for(int j = low; j < high; j++) { // A.3
            if(array[j] <= pivot) {
                i++;
                swap(array, i, j);
            }
        }
        // A.4.4J
        swap(array, i+1, high);
        return i+1;
    }
    private void swap(int[] array, int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    private void sort(int[] array, int low, int high) { // A.5
        if(low < high) { // A.6
            int part = partition(array, low, high);
            sort(array, low, part-1);
            sort(array, part+1, high);
        }
    }
    void quicksort(int[] array) {sort(array, 0, array.length-1);} // A.7
}
