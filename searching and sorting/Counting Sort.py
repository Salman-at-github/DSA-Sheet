# Counting Sort is a non-comparison-based sorting algorithm that works well when there is limited range of input values. It is particularly efficient when the range of input values is small compared to the number of elements to be sorted. The basic idea behind Counting Sort is to count the frequency of each distinct element in the input array and use that information to place the elements in their correct sorted positions.

#Good only for short numbers and less items, the range shouldn't be much either (eg, a lot of elements from 0-10 are good but [1,100,1000] isn't good for this algo)

# Function to find the maximum element in an array
def get_maximum(arr):
    if len(arr) > 0:
        highest = arr[0]
        for num in arr:
            if num > highest:
                highest = num
    return highest

# Counting Sort function
def count_sort(input_array):
    # Finding the maximum element in the input_array.
    M = get_maximum(input_array)

    # Initializing count_array with 0 for each possible value.
    count_array = [0] * (M + 1)

    # Counting the frequency of each element in the input_array.
    for num in input_array:
        count_array[num] += 1

    # Calculating the prefix sum at each index of count_array.
    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]

    # Creating the output_array from count_array.
    output_array = [0] * len(input_array)

    # Placing elements in their correct sorted positions in the output_array.
    for i in range(len(input_array) - 1, -1, -1):
        # Decrement the count of the current element in count_array for placing element in right position
        count_array[input_array[i]] -= 1
        # Place the current element at its correct position in the output_array.
        output_array[count_array[input_array[i]]] = input_array[i]
    return output_array

# Driver code
if __name__ == "__main__":
    # Input array
    input_array = [4, 3, 12, 1, 5, 5, 3, 9]
    # Output array
    output_array = count_sort(input_array)
    print(output_array)