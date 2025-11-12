class PascalTriangleTree:
    def __init__(self, value, left_prev, right_prev):
        self.value = value
        self.left_prev = left_prev
        self.right_prev = right_prev
    
    def __repr__(self):
        return f"{self.value}"


def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    if row_count == 0:
        return []
    
    # Recursive call: get all previous rows
    prev_triangle = rows(row_count - 1)
    
    # Build the new row
    if row_count == 1:
        new_row = [1]
    else:
        last_row = prev_triangle[-1]  # Get the last computed row
        new_row = [1]
        for j in range(len(last_row) - 1):
            new_row.append(last_row[j] + last_row[j + 1])
        new_row.append(1)
    # Note: This recursive approach is required by the test specification,
    # which validates the recursion depth limit to ensure proper implementation.
    return prev_triangle + [new_row]
                
                
