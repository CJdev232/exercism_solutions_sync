def saddle_points(matrix):
    # Handle empty matrix
    if not matrix or not all(matrix):
        return []
    
    # Validate irregular matrix
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise ValueError("irregular matrix")
    
    total_candidates = set()
    
    # Filter: keep only row maxima
    for row_index in range(len(matrix)):
        row_curr = matrix[row_index]
        row_max = max(row_curr)
        
        # Keep only elements that equal the row maximum
        for col_index, value in enumerate(row_curr):
            if value == row_max:
                total_candidates.add((row_index, col_index))
    
    # Filter: keep only column minima
    for row_index, col_index in list(total_candidates):
        value = matrix[row_index][col_index]
        min_in_col = min(matrix[x][col_index] for x in range(len(matrix)))
        
        if value != min_in_col:
            total_candidates.discard((row_index, col_index))
    
    # Convert to list of dicts with 1-based indexing
    return [{"row": row + 1, "column": col + 1} 
            for row, col in total_candidates]