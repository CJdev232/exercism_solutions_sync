def sum_of_multiples(limit, multiples):
    mul_set = set()
    
    for base in multiples:
        # Skip invalid bases
        if base <= 0:
            continue
        
        # Add all multiples of base that are STRICTLY LESS THAN limit
        # range(base, limit, base) automatically gives us base, 2*base, 3*base, etc.
        for multiple in range(base, limit, base):
            mul_set.add(multiple)
    
    return sum(mul_set)