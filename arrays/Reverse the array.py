def reverse_array(arr):
    """
        We use two pointer approach here
        Time: O(n)
        Space: O(1)
    """
    start = 0
    end = len(arr) - 1

    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

res = reverse_array([1,2,3,4,5,6])
print(res)