def show_duplicates(s):
    memory = {}
    for char in s:
        if char != " ":
            if char in memory:
                memory[char] += 1
            else:
                memory[char] = 1
        
    for key in memory:
        if memory[key] > 1:
            print(f"{key}, count = {memory[key]}")

show_duplicates("Hi bro hello bbb")