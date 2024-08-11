from operator import attrgetter

from com.patrick.private.euler.problem018 import TreeNode
from com.patrick.private.utils.benchmark import Benchmark


class Problem67(object):
    """
    By starting at the top of the triangle below and moving to adjacent numbers on the row below,
    the maximum total from top to bottom is 23.

           3
          7 4
         2 4 6
        8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom of the given triangle.

    NOTE: This is a much more difficult version of Problem 18.
    It is not possible to try every route to solve this problem, as there are 299 altogether!
    If you could check one trillion (10^12) routes every second it would take over
    twenty billion years to check them all.
    There is an efficient algorithm to solve it. ;o)
    """

    def __init__(self, filename: str):
        with open(filename) as f:
            self.triangle_numbers = [[int(n) for n in line.split(" ")] for line in f.readlines()]

        print("Problem 67: Find the maximum total from top to bottom of the given triangle.")

    @Benchmark
    def attempt_1(self):
        root, leafs = TreeNode.from_triangle_tree(self.triangle_numbers)
        result = max(leafs, key=attrgetter('result')).result

        print("")
        print(f"Result: {result}")

    @Benchmark
    def attempt_2(self):
        numbers = self.triangle_numbers
        for row_ix in range(1, len(numbers)):
            row = numbers[row_ix]
            prev = numbers[row_ix - 1]
            for ix, number in enumerate(row):
                if ix == 0:
                    row[ix] = number + prev[ix]
                elif ix == len(row) - 1:
                    row[ix] = number + prev[ix - 1]
                else:
                    row[ix] = max(number + prev[ix - 1], number + prev[ix])

        result = max(numbers[len(numbers) - 1])
        print("")
        print(f"Result: {result}")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")


if __name__ == '__main__':
    problem = Problem67(filename="../../../../resources/problem067.txt")

    problem.attempt_1()
    problem.attempt_2()
    problem.official_solution()
