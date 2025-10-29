def square_root(number):
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number")
    
    # Handle negative numbers
    if number < 0:
        raise ValueError("Cannot compute square root of negative number")
    
    if number == 0:
        return 0
    last = 0
    res = 1
    while (last != res):
        last = res
        res = (res+number/res)/2
    return res
