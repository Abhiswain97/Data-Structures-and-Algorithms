package Algorithms.searching.binary_search;

import java.util.Arrays;

/**
 * binary_search
 */
public class binary_search {

    static int search(int[] arr, int key) {
        int leftIndex = 0, rightIndex = arr.length - 1;

        while (leftIndex <= rightIndex) {
            int mid = (leftIndex + rightIndex) / 2;
            if (arr[mid] == key) {
                return mid;
            } else if (arr[mid] > key) {
                rightIndex = mid - 1;
            } else {
                leftIndex = mid + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {

        int[] arr = { 1, 3, 2, 0, 5, 4, -1 };
        int key = 3;

        Arrays.sort(arr);

        int s = search(arr, key);
        if (s != -1) {
            System.out.printf("%d found at index %d", key, s);
        } else {
            System.out.printf("%d not found", key);
        }
    }
}