from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list using the Bubble Sort algorithm.

    Args:
        arr (List[int]): The list to sort.

    Returns:
        List[int]: The sorted list.
    """

    # ---- DO NOT MODIFY ABOVE THIS LINE ----

    n = len(arr)

    # TODO: Implement Bubble Sort logic here
    # Repeatedly compare adjacent elements and swap them
    # if they are in the wrong order. Continue until the list is sorted.

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # ---- DO NOT MODIFY BELOW THIS LINE ----
    return arr


def main():
    """
    Main function for testing bubble sort.
    """

    sample_data = [64, 34, 25, 12, 22, 11, 90]

    print("Original list:", sample_data)

    sorted_data = bubble_sort(sample_data.copy())

    print("Sorted list:  ", sorted_data)


if __name__ == "__main__":
    main()