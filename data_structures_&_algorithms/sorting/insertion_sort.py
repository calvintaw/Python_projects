"""
insertion_sort.py

Template for implementing Insertion Sort.
You only need to complete the sorting logic inside insertion_sort().
"""

from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list using the Insertion Sort algorithm.

    Args:
        arr (List[int]): The list to sort.

    Returns:
        List[int]: The sorted list.
    """

    # ---- DO NOT MODIFY ABOVE THIS LINE ----
    n = len(arr)

    # TODO: Implement Insertion Sort logic here
    # Iterate through the list and insert each element
    # into its correct position in the sorted portion of the list.

    # for i in range(1, n):
    #   for j in range(i):
    #     if arr[j] > arr[i]:
    #         arr[j], arr[i] = arr[i], arr[j]

    # for i in range(1, n):
    #   for j in range(i - 1, -1, -1):
    #     if arr[j] > arr[j+1]:
    #         arr[j+1], arr[j] = arr[j], arr[j+1]

    # for i in range(1, n):
    #     temp = arr[i]
    #     j = i - 1

    #     while j >= 0 and arr[j] > temp:
    #         arr[j+1] = arr[j];
    #         j-=1

    #     arr[j+1] = temp;    
    for i in range(1, n):
        j = i - 1
        while j >= 0 and arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j-=1

    # ---- DO NOT MODIFY BELOW THIS LINE ----
    return arr

import random as r

def main():
    """
    Main function for testing insertion sort.
    """

    sample_data = [64, 34, 25, 12, 22, 11, 90]

    print("Original list:", sample_data)

    sorted_data = insertion_sort(sample_data.copy())

    print("Sorted list:  ", sorted_data)

if __name__ == "__main__":
    main()