def _is_palindrome(number):
    s = str(number)
    return s == s[::-1]

def smallest(min_factor, max_factor):
    """Find smallest palindrome product."""
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    
    min_palindrome = None
    min_factors = []
    
    # Generate products starting from smallest
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j
            
            # Early exit: if product is already larger than found palindrome, skip
            if min_palindrome and product > min_palindrome:
                break
            
            if _is_palindrome(product):
                if min_palindrome is None or product < min_palindrome:
                    min_palindrome = product
                    min_factors = [(i, j)]
                elif product == min_palindrome:
                    min_factors.append((i, j))
    
    if min_palindrome is None:
        return (None, [])
    return (min_palindrome, min_factors)

def largest(min_factor, max_factor):
    """Find largest palindrome product."""
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    
    max_palindrome = None
    max_factors = []
    
    # Generate products starting from largest
    for i in range(max_factor, min_factor - 1, -1):
        # Early exit: if i*max_factor is smaller than found palindrome, we're done
        if max_palindrome and i * max_factor < max_palindrome:
            break
            
        for j in range(max_factor, i - 1, -1):
            product = i * j
            
            # Early exit: if product is already smaller than found palindrome, skip rest
            if max_palindrome and product < max_palindrome:
                break
            
            if _is_palindrome(product):
                if max_palindrome is None or product > max_palindrome:
                    max_palindrome = product
                    max_factors = [(i, j)]
                elif product == max_palindrome:
                    max_factors.append((i, j))
    
    if max_palindrome is None:
        return (None, [])
    return (max_palindrome, max_factors)