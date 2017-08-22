import java.util.*;
import java.io.*;
class Test extends HeapSort {
    private static void write(String fname, int[] arr) {
        try {
            BufferedWriter writer = null;
            writer = new BufferedWriter(new FileWriter(fname));
            for (int i = 0; i < arr.length; i++)
                writer.write(arr[i] + " ");
            writer.write("\n");
            writer.flush();  
            writer.close();
        } catch(IOException e) {e.printStackTrace();}         
    }
    private static int[] array(ArrayList<Integer> list) {
        int[] arr = new int[list.size()];
        for(int i = 0; i < arr.length; i++)
            arr[i] = list.get(i);
        return arr;
    }
    private static void print(int[] array) {
        for(int i : array)
            System.out.print(i + " ");
        System.out.println();
    }
    public static void main(String[] args) {
        if(args.length == 0) {
            System.err.println("err: args.length > 0");
            System.exit(0);
        } else if(args.length == 1) {
            Scanner in = null;
            try {in = new Scanner(new File(args[0]));}
            catch(Exception e) {e.printStackTrace();}
            if(in == null) {
                System.err.println("file not read");
                System.exit(0);
            }
            ArrayList<Integer> list = new ArrayList<>();
            while(in.hasNext())
                list.add(in.nextInt());
            int[] arraylist = array(list);
            HeapSort sort = new HeapSort();
            write("original.txt", arraylist);
            sort.heapSort(arraylist); 
            write("modified.txt", arraylist);
        } else {
            HeapSort sort = new HeapSort();
            int[] array = new int[args.length];
            for(int i = 0; i < array.length; i++)
                array[i] = Integer.parseInt(args[i]);
            print(array);
            sort.heapSort(array);
            print(array);
        }
    }
}
