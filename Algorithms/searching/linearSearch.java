package Algorithms.searching;

/**
 * linearSearch
 */
public class linearSearch {

    static int search(int[] arr, int key) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == key)
                return i;
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = { 1, 3, 2, 0, 5, 4, -1 };
        int key = 3;
        if (linearSearch.search(arr, 3) != -1) {
            System.out.println(key + " found at index " + linearSearch.search(arr, key));
        } else
            System.out.println(key + " not found");
    }
}