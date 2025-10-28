def rebase(input_base, digits, output_base):
    # Validate bases with EXACT messages
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    # Validate each digit with EXACT message
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")  # ← Changed!
    
    # Empty input returns [0]
    if not digits:
        return [0]
    
    # Convert to base 10
    digits_in_base_10 = 0
    for digit in digits:  
        digits_in_base_10 = digits_in_base_10 * input_base + digit
    
    if digits_in_base_10 == 0:
        return [0]
    
    # Convert to output base
    result = []
    while digits_in_base_10 > 0:
        result.append(digits_in_base_10 % output_base)
        digits_in_base_10 //= output_base
    
    return result[::-1]