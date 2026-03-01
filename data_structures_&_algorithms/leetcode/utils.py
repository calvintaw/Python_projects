from typing import List

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            continue


def get_search_params():
    val = get_int("Enter a number to search: ")
    arr_size = get_int("Enter array size: ")
    return val, arr_size

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(li: ListNode, text: string = "Linked List") -> None:
    arr = []
    while li is not None:
        arr.append(li.val)
        li = li.next

    print(f"{text}: {arr}")

