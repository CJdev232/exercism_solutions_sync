class Matrix:
    def __init__(self, matrix_string):
        # Save the original string
        self.matrix_string = matrix_string
        
        # Split by newlines to get each row as a string
        row_strings = matrix_string.split('\n')
        
        # Convert each row string into a list of integers
        self.matrix = []
        for row_string in row_strings:
            # Split by spaces and convert each number from string to int
            row_numbers = [int(num) for num in row_string.split(' ')]
            self.matrix.append(row_numbers)
        
        # Calculate dimensions
        self.row_count = len(self.matrix)
        self.col_count = len(self.matrix[0]) if self.matrix else 0

    def row(self, index):
        # Return the row at the given index (1-indexed)
        return self.matrix[index - 1]

    def column(self, index):
        # Build and return the column at the given index (1-indexed)
        col = []
        for row in self.matrix:
            col.append(row[index - 1])
        return col