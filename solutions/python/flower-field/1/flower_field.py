def _not_edge(*,matrix,pos):
    row,col = pos
    rows = len(matrix)
    cols = len(matrix[0]) if rows >0 else 0
    return 0 < row < rows - 1 and 0 < col < cols - 1
    
    
def _update_dp_for_surroundings_of_flower(*,dp,flower_pos):
    flower_pos_dim0, flower_pos_dim1 = flower_pos
    offsets = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,-1), (-1,1)]
    
    # Fast path: if not on edge, we know all 8 neighbors exist!
    if _not_edge(matrix=dp, pos=flower_pos):
        for offset in offsets:
            offset_dim0, offset_dim1 = offset
            new_row = flower_pos_dim0 + offset_dim0
            new_col = flower_pos_dim1 + offset_dim1
            dp[new_row][new_col] += 1
    else:
        # Slow path: check each neighbor individually
        for offset in offsets:
            offset_dim0, offset_dim1 = offset
            new_row = flower_pos_dim0 + offset_dim0
            new_col = flower_pos_dim1 + offset_dim1
            if 0 <= new_row < len(dp) and 0 <= new_col < len(dp[0]):
                dp[new_row][new_col] += 1
        
def annotate(garden):
    # Function body starts here
    if not garden:
        return []
    if garden and garden[0]:  # Not empty
        width = len(garden[0])
        for row in garden:
            if len(row) != width:
                raise ValueError("The board is invalid with current input.")
            for char in row:
                if char not in [' ', '*']:
                    raise ValueError("The board is invalid with current input.")
    result = [list(row) for row in garden]
    dp = [[0 for _ in range(len(garden[0]))] for _ in range(len(garden))]
    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if garden[i][j] == '*':
                dp[i][j] = -1 
                _update_dp_for_surroundings_of_flower(dp=dp,flower_pos=(i,j))
    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if result[i][j] == ' ' and dp[i][j] > 0:
                result[i][j] = str(dp[i][j])
    return [''.join(row) for row in result]
        

            
            
