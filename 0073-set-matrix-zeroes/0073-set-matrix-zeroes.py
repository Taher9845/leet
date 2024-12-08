class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        Row, Col = len(matrix), len(matrix[0])
        rowzero = False  # Tracks whether the first row needs to be zeroed out

        # Mark rows and columns that need to be zeroed
        for r in range(Row):
            for c in range(Col):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0  # Mark the column in the first row
                    if r > 0:
                        matrix[r][0] = 0  # Mark the row in the first column
                    else:
                        rowzero = True  # Mark that the first row needs to be zeroed

        # Process the matrix based on the marks, skipping the first row and column
        for r in range(1, Row):
            for c in range(1, Col):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Handle the first column separately
        if matrix[0][0] == 0:
            for r in range(Row):
                matrix[r][0] = 0

        # Handle the first row separately
        if rowzero:
            for c in range(Col):
                matrix[0][c] = 0
