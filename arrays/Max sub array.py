#Given an integer array nums, find the subarray with the largest sum, and return its sum.
def get_max_subarr(arr):

    """
        Time: O(n)
        Space: O(1)
    """

    if len(arr) == 0:
        return None
    highest_sum = arr[0]
    current_sum = 0
    for num in arr:
        current_sum += num
        if current_sum > highest_sum:
            highest_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return highest_sum

res = get_max_subarr([-2,-1,-3,-4,-9])
print(res)