    
    # logic: We first select any word as base, for its number of chars we run a loop, we nest a loop for next strings in the list, comparing current index to see if it exceedings len of any next words, if yes we return the base[0:i], also if base[i] != word[i] for other words, we return
    #We exit the loop and return base when:
        #current index == len of word
        #base of current index != word of current index
def longest_common_prefix(arr):
    # if array of strings is empty return same
    if len(arr) == 0:
        return ""
    
    base_word = arr[0]
    for i in range(len(base_word)):
        for word in arr[1:] :
            if i == len(word) or base_word[i] != word[i]:
                return base_word[0:i]
    
    # if loop completes, entire base word is cf
    return base_word

res = longest_common_prefix(["ab","a"])
print(res)