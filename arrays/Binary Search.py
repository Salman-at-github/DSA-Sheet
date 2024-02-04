def get_index_sorted(arr, t):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == t:
            return mid
        
        if arr[start] <= t <= arr[mid]:
            start += 1
            end = mid
        else:
            start = mid
            end -= 1
    
    return -1

res = get_index_sorted([1,2,3,4,5,6,7,8], 5)
print(res)