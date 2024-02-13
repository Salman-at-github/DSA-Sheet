# A step array is an array of integers where each element has a difference of at most k with its neighbor. Given a key x, we need to find the index value of x if multiple-element exist to return the first occurrence of the key.

#Custom 
#T: O(n)
#S: O(1)
#k is difference of elements, x is targ
def get_index(arr, k, x):
    for i in range(1,len(arr)):
        if len(arr) > 1:
            if i == 0 and arr[i] == x and arr[i + 1] <= k:
                return i
            if arr[i] - arr[i - 1] <= k:
                if arr[i] == x:
                    return i
    
    return False

# res = get_index([4, 5, 6, 7, 6], 1, 6)
res = get_index([20, 40, 50, 70, 70, 60], 20, 60)
print(res)



#Jump method
#T: O(n/k) = O(n)
#S: O(1)

def search(arr, n, x, k):

	# Traverse the given array starting from
	# leftmost element
	i = 0
	while (i < n):
	
		# If x is found at index i
		if (arr[i] == x):
			return i

		# Jump the difference between current
		# array element and x divided by k
		# We use max here to make sure that i
		# moves at-least one step ahead.
		i = i + max(1, int(abs(arr[i] - x) / k)) #This division essentially determines the number of steps or jumps the algorithm should take.
        

	print("number is not present!")
	return -1

# arr[i] - x: Calculates the absolute difference between the current array element at index i and the target element x.	
# abs(arr[i] - x) / k: Computes the absolute difference divided by the given value of k. This division essentially determines the number of steps or jumps the algorithm should take.

# int(abs(arr[i] - x) / k): Converts the result of the division to an integer. This ensures that the number of steps is a whole number, as array indices must be integers.

# max(1, int(abs(arr[i] - x) / k)): Takes the maximum of the calculated number of steps and 1. This ensures that the algorithm always moves at least one step ahead, preventing an infinite loop if the division result is zero.

# i = i + max(1, int(abs(arr[i] - x) / k)): Updates the index i by adding the calculated number of steps.

# Driver program to test above function
arr = [2, 4, 5, 7, 7, 6]
x = 6
k = 2
n = len(arr)
print("Element", x, "is present at index",search(arr, n, x, k))

# This code is contributed
# by Smitha Dinesh Semwal
