from com.patrick.private.utils.benchmark import Benchmark


class Problem15(object):
    """
    Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
    there are exactly 6 routes to the bottom right corner.

    How many such routes are there through a 20×20 grid?
    """

    def __init__(self, grid_size: int):
        self.grid_size = grid_size
        self.grid = [[False for _ in range(self.grid_size + 1)] for _ in range(self.grid_size + 1)]
        print(f"Problem 15: How many such routes are there through a {self.grid_size}×{self.grid_size} grid?")
        print(f"grid_size={self.grid_size}")

    @Benchmark
    def attempt_1(self):
        self.grid = [[False for _ in range(self.grid_size + 1)] for _ in range(self.grid_size + 1)]
        result = self.calculate_routes_recursive(self.grid_size, self.grid_size)

        print("")
        print(f"Result: {result}")

    @Benchmark
    def attempt_2(self):
        result = self.calculate_routes_iterative(self.grid_size, self.grid_size)

        print("")
        print(f"Result: {result}")

    @Benchmark
    def official_solution(self):
        result = 1
        limit = self.grid_size + 1

        for i in range(1, limit):
            result = result * (self.grid_size + i) // i

        print("")
        print(f"Result: {result}")

    def calculate_routes_recursive(self, dim_x, dim_y):
        if dim_x == 0 or dim_y == 0:
            return 1

        if self.grid[dim_x][dim_y]:
            return self.grid[dim_x][dim_y]

        self.grid[dim_x][dim_y] = \
            self.calculate_routes_recursive(dim_x - 1, dim_y) + self.calculate_routes_recursive(dim_x, dim_y - 1)

        return self.grid[dim_x][dim_y]

    @staticmethod
    def calculate_routes_iterative(dim_x, dim_y):
        grid = [[0 for _ in range(dim_x + 1)] for _ in range(dim_y + 1)]
        for i in range(dim_x + 1):
            grid[i][0] = 1

        for i in range(dim_y + 1):
            grid[0][i] = 1

        for x in range(1, dim_x + 1):
            for y in range(1, dim_y + 1):
                grid[x][y] = grid[x - 1][y] + grid[x][y - 1]

        return grid[dim_x][dim_y]


if __name__ == '__main__':
    problem = Problem15(grid_size=20)

    problem.attempt_1()
    problem.attempt_2()
    problem.official_solution()
