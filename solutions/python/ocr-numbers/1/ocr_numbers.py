def convert(input_grid):
    rows_len = len(input_grid)
    if rows_len % 4 != 0:
        raise ValueError('Number of input lines is not a multiple of four')
    cols_len = len(input_grid[0])
    if cols_len % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")
    DIGIT_PATTERNS = {
    (" _ ", "| |", "|_|"): "0",
    ("   ", "  |", "  |"): "1",  
    (" _ ", " _|", "|_ "): "2",
    (" _ ", " _|", " _|"): "3",  
    ("   ", "|_|", "  |"): "4",  
    (" _ ", "|_ ", " _|"): "5",
    (" _ ", "|_ ", "|_|"): "6",
    (" _ ", "  |", "  |"): "7",
    (" _ ", "|_|", "|_|"): "8",
    (" _ ", "|_|", " _|"): "9",
}
    result_lines = [] 
    
    for r in range(0, rows_len, 4):
        curr_line_digits = []
        for c in range(0, cols_len, 3):
            digit_block = []
            for row_offset in range(4):
                digit_block.append(input_grid[r + row_offset][c:c+3])
            
            
            pattern_key = (digit_block[0], digit_block[1], digit_block[2])
            if pattern_key in DIGIT_PATTERNS:
                curr_line_digits.append(DIGIT_PATTERNS[pattern_key])
            else:
                curr_line_digits.append("?")
        result_lines.append("".join(curr_line_digits))
    return ",".join(result_lines)  
    

