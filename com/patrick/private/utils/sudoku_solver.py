class Sudoku:

    def __init__(self, grid: list[str], rows: int = 9, columns: int = 9):
        self.grid_no = int(grid[0][-2:])
        self.grid = []
        self.rows = rows
        self.columns = columns

        for row in grid[1:]:
            self.grid.append([int(digit) for digit in list(row)])

    def solve(self) -> None:
        solved = self._solve_sudoku(0, 0)
        print(f"Solved Sudoku {self.grid_no}: {solved}")

    # Checks whether it will be
    # legal to assign num to the
    # given row, col
    def _is_safe(self, row, col, num):

        # Check if we find the same num
        # in the similar row , we
        # return false
        for x in range(self.columns):
            if self.grid[row][x] == num:
                return False

        # Check if we find the same num in
        # the similar column , we
        # return false
        for x in range(self.rows):
            if self.grid[x][col] == num:
                return False

        # Check if we find the same num in
        # the particular 3*3 matrix,
        # we return false
        start_row = row - row % (self.rows // 3)
        start_col = col - col % (self.columns // 3)
        for i in range(self.rows // 3):
            for j in range(self.columns // 3):
                if self.grid[i + start_row][j + start_col] == num:
                    return False
        return True

    # Takes a partially filled-in grid and attempts
    # to assign values to all unassigned locations in
    # such a way to meet the requirements for
    # Sudoku solution (non-duplication across rows,
    # columns, and boxes) */
    def _solve_sudoku(self, row, col):

        # Check if we have reached the 8th
        # row and 9th column (0
        # indexed matrix) , we are
        # returning true to avoid
        # further backtracking
        if row == self.rows - 1 and col == self.columns:
            return True

        # Check if column value  becomes 9 ,
        # we move to next row and
        # column start from 0
        if col == self.columns:
            row += 1
            col = 0

        # Check if the current position of
        # the grid already contains
        # value >0, we iterate for next column
        if self.grid[row][col] > 0:
            return self._solve_sudoku(row, col + 1)
        for num in range(1, self.rows + 1, 1):

            # Check if it is safe to place
            # the num (1-9)  in the
            # given row ,col  ->we
            # move to next column
            if self._is_safe(row, col, num):

                # Assigning the num in
                # the current (row,col)
                # position of the grid
                # and assuming our assigned
                # num in the position
                # is correct
                self.grid[row][col] = num

                # Checking for next possibility with next
                # column
                if self._solve_sudoku(row, col + 1):
                    return True

            # Removing the assigned num ,
            # since our assumption
            # was wrong , and we go for
            # next assumption with
            # diff num value
            self.grid[row][col] = 0
        return False
