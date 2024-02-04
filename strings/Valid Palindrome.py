def is_alnum(char):
    allowed_chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    return char.lower() in allowed_chars

def is_palindrome(s): #O(n/2)
    start = 0
    end = len(s) - 1
    while start <= end:
        if not is_alnum(s[start]):
            start += 1
            continue
        if not is_alnum(s[end]):
            end -= 1
            continue
        if s[start].lower() != s[end].lower():
            return False
        else:
            start += 1
            end -= 1
        
    return True

res = is_palindrome("ma am")
print(res)




