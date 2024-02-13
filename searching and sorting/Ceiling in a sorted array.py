# Given a sorted array and a value x, the ceiling of x is the smallest element in an array greater than or equal to x, and the floor is the greatest element smaller than or equal to x. Assume that the array is sorted in non-decreasing order. Write efficient functions to find the floor and ceiling of x. 

#CUSTOM
#T: O(n)
#S: O(1)

def get_ceil(arr, x):
    smallest = arr[0]
    if smallest == x:
        return smallest
    for num in arr:
        if num < smallest and num >= x:
            return num
    return "No ceil"

def get_floor(arr, x):
    biggest = arr[0]
    if biggest == x:
        return biggest
    for num in arr:
        if num > biggest and num >= x:
            return num
    return "No ceil"

# arr = [1, 2, 8, 10, 10, 12, 19]
# x=1
# res1 = get_ceil(arr, x)
# res2 = get_floor(arr, x)
# print(res1, res2)


#BINARY SEARCH
#T: O(logn)
#S: O(1)


def binary_search_ceil(arr, x):
    start = 0
    end = len(arr) - 1
    ceil = None  # Placeholder for ceil value

    # Binary search for ceil, 
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == x:
            return arr[mid]

        elif arr[mid] < x:
            start = mid + 1

        else:
            ceil = arr[mid]
            end = mid - 1

    # Check if a ceil value was found
    if ceil is not None:
        return ceil
    else:
        return "No ceil"

def binary_search_floor(arr, x):
    start = 0
    end = len(arr) - 1
    floor = None  # Placeholder for floor value

    # Binary search for floor
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == x:
            return arr[mid]

        elif arr[mid] < x:
            floor = arr[mid]
            start = mid + 1

        else:
            end = mid - 1

    # Check if a floor value was found
    if floor is not None:
        return floor
    else:
        return "No floor"

arr = [1, 2, 8, 10, 10, 12, 19]
x = 20
ceil = binary_search_ceil(arr, x)
floor = binary_search_floor(arr, x)
print(ceil, floor)
