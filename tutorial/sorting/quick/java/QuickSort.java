class QuickSort {
    private int partition(int[] array, int low, int high) { // A.1
        // B.1.2J
        int pivot = array[high];
        int i = low - 1;
        for(int j = low; j < high; j++) { // A.2
            if(array[j] <= pivot) {
                i++;
                // B.2.3J
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
        // B.3,4J
        int temp = array[i+1];
        array[i+1] = array[high];
        array[high] = temp;
        return i+1;
    }
    void quickSort(int[] array, int low, int high) { // A.3
        if(low < high) { // A.4
            int part = partition(array, low, high);
            quickSort(array, low, part-1);
            quickSort(array, part+1, high);
        }
    }
}
