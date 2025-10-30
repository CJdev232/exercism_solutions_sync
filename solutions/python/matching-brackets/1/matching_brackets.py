def is_paired(input_string):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for item in input_string:
        if item in pairs:  # Opening bracket
            stack.append(item)
        elif item in pairs.values():  # Closing bracket
            if stack and pairs[stack[-1]] == item:
                stack.pop()
            else:
                return False  # Mismatched or unmatched closing bracket
    
    return not stack