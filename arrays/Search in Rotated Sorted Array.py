def get_index_sorted_rot(arr, t):
    start = 0
    end = len(arr) -1
    while start <= end:
        mid = (start + end) //2
        if arr[mid] == t:
            return mid
        #if left is sorted, look for t there
        if arr[start] <= arr[mid]:
            #if target is in left, update end index
            if arr[start] <= t <= arr[mid]:
                end = mid - 1
            #target not in left, update start index
            else:
                start = mid + 1
        #left is not sorted, right is 
        else:
            #check if target is in right side, if yes, update start
            if arr[mid] <= t <= arr[end]:
                start = mid + 1
            #else target not in left, update end index for left
            else:
                end = mid - 1
    #return false if target not found
    return -1


            


res = get_index_sorted_rot([4,5,6,7,0,1,2], 2)
print(res)