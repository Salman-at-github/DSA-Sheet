def longest_sub(s):
    if len(s) == 0:
        return ""
    sub = ""
    for char in s:
        if char in sub:
            return sub
        else:
            sub += char

res = longest_sub("abcabcbb")
print(res)