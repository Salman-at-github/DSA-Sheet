# Given an array of N integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 

# Each student gets one packet.
# The difference between the number of chocolates in the packet with maximum chocolates and the packet with minimum chocolates given to the students is minimum.

def get_least_diff(arr, m):
    
    arr.sort()
    least_diff = arr[len(arr)-1] - arr[0] 

    for i in range(len(arr) - m  +1):
        current_diff = arr[m-1 + i] - arr[i]
        if current_diff < least_diff:
            least_diff = current_diff

    return least_diff

def min_chocolate_difference_unsorted(arr, m): #O(m*n)
    if m > len(arr):
        return None

    arr_min = min(arr)
    arr_max = max(arr)

    min_difference = float('inf')

    for i in range(len(arr) - m + 1):
        current_difference = max(arr[i:i+m]) - min(arr[i:i+m])
        min_difference = min(min_difference, current_difference)

    return min_difference

# Example usage:
arr = [7, 3, 2, 4, 9, 12, 56]
m = 3

result_sorted = get_least_diff(arr, m)
result_unsorted = min_chocolate_difference_unsorted(arr, m)

print(f"Minimum Difference (Sorted) is {result_sorted}")
print(f"Minimum Difference (Unsorted) is {result_unsorted}")
