def _layers_size_helper(size):
    """Returns how many numbers are in each layer"""
    layers = []
    layer_size = size
    
    while layer_size > 0:
        # Numbers in this layer's perimeter
        if layer_size == 1:
            # Special case: center square has just 1 number
            num_in_layer = 1
        else:
            num_in_layer = 2 * layer_size + 2 * (layer_size - 2)
        
        layers.append(num_in_layer)
        layer_size -= 2
    
    return layers
def spiral_matrix(size):
    # Create empty matrix
    matrix = [[0] * size for _ in range(size)]
    
    num = 1
    layer = 0
    
    # Process each layer
    while layer < size // 2 + 1:
        top = layer
        bottom = size - 1 - layer
        left = layer
        right = size - 1 - layer
        
        # If we've gone past the middle, stop
        if top > bottom or left > right:
            break
        
        #  Fill TOP row (left to right)
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        
        #  Fill RIGHT column (top to bottom, skip top corner already filled)
        for row in range(top + 1, bottom + 1):
            matrix[row][right] = num
            num += 1
        
        #  Fill BOTTOM row (right to left, only if there's a different row)
        if top < bottom:
            for col in range(right - 1, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
        
        #  Fill LEFT column (bottom to top, skip both corners already filled)
        if left < right:
            for row in range(bottom - 1, top, -1):
                matrix[row][left] = num
                num += 1
        
        layer += 1
    
    return matrix
