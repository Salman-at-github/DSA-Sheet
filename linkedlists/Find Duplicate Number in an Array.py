# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

#NOTE: THIS CAN'T BE SOLVED USING ARRAYS WITH T o(n) AND S o(1), only option is linked list, since the elements are 1 to n where n is the size, and n+1 elements are present, the index of the array will not be more than the elements, so we can use LL here
#eg         [1, 3,  4,  2,  2], 
#index      0   1   2   3   4
#if 1 is the head node, using elmenents as nodes we get 1-->3-->2<-->4 so loop exists at 4, we can use Floy's algo to detect this loop, it begins from 2 so 2 is the duplicate element. Once loop is found, enter another loop to find the start of loop by initiating slow from beginning, the fast will remain at same place but now move one step at a time, they will meet eventually at the beginning of the loop

def get_duplicate(arr): #T o(n), S o(1)
    slow = arr[0]
    fast = arr[0]

    while True: #start a loop, end it once we find the cycle
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    
    # now reset slow pointer, and set fast to move at one step at a time, they'll meet at the intersection
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow

res = get_duplicate([3,1,3,4,2])
print(res)