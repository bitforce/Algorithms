class QuickSort {
    private int partition(int[] array, int low, int high) { // A.1
        // A.2.2J
        int pivot = array[high];
        int i = low - 1;
        for(int j = low; j < high; j++) { // A.3
            if(array[j] <= pivot) {
                i++;
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
        // A.4.4J
        int temp = array[i+1];
        array[i+1] = array[high];
        array[high] = temp;
        return i+1;
    }
    private void quicksort(int[] array, int low, int high) { // A.5
        if(low < high) { // A.6
            int part = partition(array, low, high);
            quicksort(array, low, part-1);
            quicksort(array, part+1, high);
        }
    }
    void quicksort(int[] array) {quicksort(array, 0, array.length-1);} // A.7
}
