class CombSort {
    int next(int gap) { // A.1
        gap = (gap * 10) / 13; // A.2
        if(gap < 1)
            return 1;
        return gap;
    }
    void combsort(int[] array) { 
        int length = array.length;
        int gap = length; // A.3
        boolean swapped = true;
        while(gap != 1 || swapped == true) { // A.4
            gap = next(gap); // A.5
            swapped = false;
            for(int i = 0; i < length - gap; i++) // A.6
                if(array[i] > array[i+gap]) {
                    int temp = array[i];
                    array[i] = array[i+gap];
                    array[i+gap]  = temp;
                    swapped = true;
                }
        }
    }
}
