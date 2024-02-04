def remove_cons(s):
    # principle: we use a new string, check if the prev char in the string is same as current one, if not only then we add the string
    new_string = ""
    for char in s:
        if len(new_string) > 0:
            if char.lower() != new_string[len(new_string) - 1].lower():
                new_string += char
        else:
            new_string = char
    return new_string

res = remove_cons("aabbccAa")
print(res)