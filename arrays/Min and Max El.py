
def get_min_max(arr):
    """
        Time: O(n)
        Space: O(1)
    """
    if len(arr) == 0:
        return None
    
    highest = arr[0]
    lowest = arr[0]

    for num in arr:
        if num > highest:
            highest = num
            continue
        if num < lowest:
            lowest = num
    return highest,lowest

res = get_min_max([9,2,0,5,6])
print(res)
        