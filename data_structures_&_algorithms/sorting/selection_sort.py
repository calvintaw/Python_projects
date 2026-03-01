"""
selection_sort.py

Template for implementing Selection Sort.
You only need to complete the sorting logic inside selection_sort().
"""

from typing import List

def selection_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list using the Selection Sort algorithm.

    Args:
        arr (List[int]): The list to sort.

    Returns:
        List[int]: The sorted list.
    """

    # ---- DO NOT MODIFY ABOVE THIS LINE ----

    n = len(arr)

    # TODO: Implement Selection Sort logic here
    # Use nested loops to repeatedly select the minimum element
    # from the unsorted portion and swap it with the first unsorted element.

    for i in range(n - 1):
      min = i

      for j in range(i + 1, n):
        if arr[j] < arr[min]:
          min = j
      arr[i], arr[min] = arr[min], arr[i]

    # ---- DO NOT MODIFY BELOW THIS LINE ----
    return arr


def main():
    """
    Main function for testing selection sort.
    """

    sample_data = [64, 25, 12, 22, 11, 90]

    print("Original list:", sample_data)

    sorted_data = selection_sort(sample_data.copy())

    print("Sorted list:  ", sorted_data)


if __name__ == "__main__":
    main()