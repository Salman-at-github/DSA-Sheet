def has_duplicate(arr):
    if len(arr) == 0:
        return None
    seen = {}
    for item in arr:
        if item in seen:
            return True
        else:
            seen[item] = True
    
    return False

res = has_duplicate([1,2,3,4,5,1])
print(res)
