# # Given an unsorted array and a number n, find if there exists a pair of elements in the array whose difference is n. 

#Bruteforce would be O(n*n)

#HASHMAP
#T: O(n)
#S: O(n)
def get_pair(arr, target):
    n = len(arr)
    seen = {}  # store num with its index here, we will check if y exists in {},
    
    for i in range(n):
        current_num = arr[i]
        #t = a - b implies b = a - target
        required_num = current_num - target
        if required_num in seen:  # y exists as num in array, it means we have x and found y
            return [i, seen[required_num]]
        else:  # if it's not in {}, add number with its index to {} so that we can compare future diff to it 
            seen[current_num] = i  # {number: index}
    
    print(seen)
    return "404 Not Found"

res = get_pair([1, 2, 3, 4, 5, 6], 3)
print(res)

#SORTING
#T: O(nlogn)
#S: O(1)

def get_pair_sort(arr, t):
    arr.sort()
    
    size = len(arr)
    # initialize two pointers
    i = 0
    j = 0
    while i < size and j < size:
        if i != j and (arr[j] - arr[i]) == t:
            return f"Pair index is {j} and {i}"
        elif (arr[j] - arr[i]) < t:
            j += 1
        else:
            i += 1
    return "Not found"

res = get_pair_sort([1, 2, 3, 4, 5, 6], 3)
print(res)

