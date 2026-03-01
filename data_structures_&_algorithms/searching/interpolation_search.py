from utils import get_search_params


def interpolation_search(arr, val):
    """
    Interpolation search works on sorted, uniformly distributed arrays.

    Instead of always checking the middle element (like binary search),
    it estimates where the target value should be based on its value.

    The idea:
    If values are evenly distributed, we can "interpolate" the likely
    position of the target using a proportional formula.

    Probe formula:

        probe = left + (right - left) *
                (val - arr[left]) / (arr[right] - arr[left])

    Explanation of the formula:

    (val - arr[left]) / (arr[right] - arr[left])
        → gives the relative position of val within the value range.

    (right - left)
        → scales that ratio to the index range.

    left + ...
        → shifts the estimate into the correct index space.

    Important edge case:
    If arr[left] == arr[right], then the denominator
    (arr[right] - arr[left]) becomes 0, which would cause
    a division by zero error.

    This situation occurs when:
    - Only one element remains (left == right), or
    - All remaining elements are identical.

    In that case, interpolation is no longer needed.
    We simply check whether that value equals val and stop.

    This works best when data is uniformly distributed.
    If distribution is uneven, performance can degrade toward O(n).
    """

    left = 0
    right = len(arr) - 1
    steps = 0
    ans = -1

    while left <= right and arr[left] <= val <= arr[right]:

        if arr[left] == arr[right]:
            if arr[left] == val:
                ans = left
            break

        probe = int(
            left
            + (right - left)
            * (val - arr[left])
            / (arr[right] - arr[left])
        )

        steps += 1
        print(f"Probe: {probe}")

        if arr[probe] == val:
            ans = probe
            break
        elif arr[probe] < val:
            left = probe + 1
        else:
            right = probe - 1

    print(f"Steps taken: {steps}")
    return ans


if __name__ == "__main__":
    val, arr_size = get_search_params()

    arr = list(range(0, arr_size + 1))
    print (arr)
    index = interpolation_search(arr, val)

    if index != -1:
        print(f"Ans: at index {index} | arr[{index}] = {arr[index]}")
    else:
        print("Ans: not found.")