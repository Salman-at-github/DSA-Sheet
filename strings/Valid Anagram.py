def is_alnum(char):
    allowed_chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    return char.lower() in allowed_chars

def is_anagram(s, t):
    memory = {}
    for char in t:
        if is_alnum(char):
            if char in memory:
                memory[char] += 1
            else:
                memory[char] = 1
    
    for char in s:
        if is_alnum(char):
            if char in memory:
                memory[char] -= 1
                if memory[char] == 0:
                    del memory[char]
    return not memory

res = is_anagram("banana","anazn a")
print(res)