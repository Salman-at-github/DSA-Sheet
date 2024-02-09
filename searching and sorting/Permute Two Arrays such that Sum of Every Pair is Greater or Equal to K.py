def PermuteForSumK(arr_first, arr_second, k):
    sorted_first = sorted(arr_first)
    rev_sorted_sec = sorted(arr_second, reverse=True)
    for i in range(len(arr_first)):
        if sorted_first[i] + rev_sorted_sec[i] != k:
            return "No"
    return "Yes" 


res = PermuteForSumK([2, 1, 3], [7, 8, 9], 10)
print(res)