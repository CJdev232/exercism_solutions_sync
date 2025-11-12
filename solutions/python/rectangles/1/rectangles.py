def _find_plus_signs_on_same_row(plus_signs, row):
    return sorted([p for p in plus_signs if p[0] == row], key=lambda p: p[1])

def _find_plus_signs_on_same_col(plus_signs, col):
    return sorted([p for p in plus_signs if p[1] == col], key=lambda p: p[0])

def _is_valid_rectangle(strings, r1, c1, r2, c2):
    """Validate all edges of potential rectangle"""
    horizontal_valid_choices = {'+', '-'}
    vertical_valid_choices = {'+', '|'}
    
    # Top edge (row r1, columns c1 to c2)
    for c in range(c1, c2 + 1):
        if strings[r1][c] not in horizontal_valid_choices:
            return False
    
    # Bottom edge (row r2, columns c1 to c2)
    for c in range(c1, c2 + 1):
        if strings[r2][c] not in horizontal_valid_choices:
            return False
    
    # Left edge (column c1, rows r1 to r2)
    for r in range(r1, r2 + 1):
        if strings[r][c1] not in vertical_valid_choices:
            return False
    
    # Right edge (column c2, rows r1 to r2)
    for r in range(r1, r2 + 1):
        if strings[r][c2] not in vertical_valid_choices:
            return False
    
    return True

def rectangles(strings):
    # Handle empty input
    if not strings or not strings[0]:
        return 0
    
    # Find all '+' signs
    plus_signs = []
    for i in range(len(strings)):
        for j in range(len(strings[0])):
            if strings[i][j] == '+':
                plus_signs.append((i, j))
    
    plus_signs_set = set(plus_signs)
    count = 0
    
    # For each potential top-left corner
    for r1, c1 in plus_signs:
        # Find all '+' on same row as (r1,c1) with column > c1
        r1_row = [c for r, c in plus_signs if r == r1 and c > c1]
        
        # Find all '+' on same column as (r1,c1) with row > r1
        c1_col = [r for r, c in plus_signs if c == c1 and r > r1]
        
        # Try all combinations of potential top-right and bottom-left corners
        for c2 in r1_row:
            for r2 in c1_col:
                # Check if bottom-right corner exists and rectangle is valid
                if (r2, c2) in plus_signs_set and _is_valid_rectangle(strings, r1, c1, r2, c2):
                    count += 1
    
    return count