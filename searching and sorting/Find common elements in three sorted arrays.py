# Given three Sorted arrays in non-decreasing order, print all common elements in these arrays.

#T: O(n*m*p)
#S: O(n)
#Bruteforce
def get_common(a1, a2, a3):
    commons = []
    for num in a1:
        if num in a2 and num in a3:
            commons.append(num)
    return commons

res = get_common([1, 5, 5], [3, 4, 5, 5, 10], [5, 5, 10, 20])
print(res)


#T: O(n + p + q)
#S: O(1)
#3 pointer
def findCommon(ar1, ar2, ar3): 
    # Initialize starting indexes for ar1[], ar2[], and ar3[]
    i, j, k = 0, 0, 0

    # Iterate through three arrays while all arrays have elements
    while i < len(ar1) and j < len(ar2) and k < len(ar3):
        # If elements in all three arrays are equal, print any of them and move ahead in all arrays
        if ar1[i] == ar2[j] == ar3[k]:
            print(ar1[i])
            i += 1
            j += 1
            k += 1
        # If ar1[i] is smaller, move ahead in ar1[]
        elif ar1[i] < ar2[j]:
            i += 1
        # If ar2[j] is smaller, move ahead in ar2[]
        elif ar2[j] < ar3[k]:
            j += 1
        # If ar3[k] is smaller, move ahead in ar3[]
        else:
            k += 1

# Driver program to check above function
ar1 = [10, 5, 10, 20, 40, 80]
ar2 = [10,6, 7, 20, 80, 100]
ar3 = [10,3, 4, 15, 20, 30, 70, 80, 120]

print("Common elements are:")
findCommon(ar1, ar2, ar3)
