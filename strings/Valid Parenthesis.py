def valid_parenthesis(s):
    pairs = {
        "(":")",
        "[":"]",
        "{":"}",
    }
    opened_stack = []

    for bracket in s:
        # check if opnening bracket, if yes push to stack
        if bracket in pairs:
            opened_stack.append(bracket)
        # else it is a closing bracket or something else, check if stack is empty, it means closing br has no opening br,
        #next check if current closing br matches the closing br for its opening br in stack in pairs, this checks order
        elif len(opened_stack) == 0 or bracket != pairs[opened_stack.pop()]:
            return False
    
    # after all conditions, if stack is emtpy, it means 
    return len(opened_stack) == 0

res = valid_parenthesis("([}]){")
print(res)