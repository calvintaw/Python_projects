from utils import get_search_params

def binary_search(arr, val):
    left = 0
    right = len(arr) - 1
    steps = 0
    ans = None

    while left <= right:
        mid = left + (right - left) // 2
        steps += 1

        if arr[mid] == val:
            ans = mid
            break
        elif arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1

    print(f"Steps taken: {steps}")
    return ans if ans is not None else -1


if __name__ == "__main__":
    val, arr_size = get_search_params()

    arr = list(range(arr_size))
    index = binary_search(arr, val)

    if index != -1:
        print(f"Ans: at index {index} | arr[{index}] = {arr[index]}")
    else:
        print("Ans: not found.")