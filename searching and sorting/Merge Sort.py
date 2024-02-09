#Time "O(n logn)"

def merge_sort(arr):
    # Step 1: Divide into left and right
    if len(arr) > 1: #cant divide array after it has only 1 element
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively apply merge_sort to each half
        merge_sort(left_half)
        merge_sort(right_half)

        # indexes for left, right, and merged array
        i = j = k = 0

        # Step 3: Merge after comparison
        while i < len(left_half) and j < len(right_half):
            # Compare elements from left_half and right_half
            if left_half[i] < right_half[j]:
                # If the element in left_half is smaller, place it in the merged array
                arr[k] = left_half[i]
                i += 1
            else:
                # If the element in right_half is smaller, place it in the merged array
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy any remaining elements from left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements from right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr
        

# Example usage:
my_array = [64, 34, 25, 12, 22, 11, 90]
print(my_array)
# Step 2: Conquer (Implicit in the merge_sort function)
# This function sorts the individual subarrays and merges them
res = merge_sort(my_array)

# Display the sorted array
print("Sorted array using Merge Sort:", res)
