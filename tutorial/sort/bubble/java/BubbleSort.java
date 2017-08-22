class BubbleSort {
    public static void bubbleSort(int[] array) {
        int length = array.length;
        for(int i = 0; i < length; i++)
            for(int j = 0; j < length - 1; j++)
                if(array[j] > array[i]) {
                    int temp = array[j];
                    array[j] = array[i];
                    array[i] = temp;
                }
    }
}
