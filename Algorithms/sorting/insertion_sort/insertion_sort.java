package Algorithms.sorting.insertion_sort;

public class insertion_sort {

    static void printList(int[] arr) {
        for (int i : arr) {
            System.out.print(i + " ");
        }
        System.out.println("\n");
    }

    static void insertionSort(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            int key = arr[i];

            int j = i - 1;

            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];

                j--;
            }

            arr[j + 1] = key;
        }
    }

    public static void main(String[] args) {
        int[] arr = { 1, 3, 2, 0, 5, 4, -1 };

        printList(arr);

        insertionSort(arr);

        printList(arr);

    }
}
