from operator import attrgetter

from com.patrick.private.utils.benchmark import Benchmark


class Problem18(object):
    """
    By starting at the top of the triangle below and moving to adjacent numbers on the row below,
    the maximum total from top to bottom is 23.

           3
          7 4
         2 4 6
        8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom of the triangle below:

                      75
                     95 64
                    17 47 82
                   18 35 87 10
                  20 04 82 47 65
                 19 01 23 75 03 34
                88 02 77 73 07 63 67
               99 65 04 28 06 16 70 92
              41 41 26 56 83 40 80 70 33
             41 48 72 33 47 32 37 16 94 29
            53 71 44 65 25 43 91 52 97 51 14
           70 11 33 28 77 73 17 78 39 68 17 57
          91 71 52 38 17 14 91 43 58 50 27 29 48
         63 66 04 68 89 53 67 30 73 16 69 87 40 31
        04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    """

    def __init__(self, filename: str):
        with open(filename) as f:
            self.triangle_numbers = [[int(n) for n in line.split(" ")] for line in f.readlines()]

        print(f"Problem 18: Find the maximum total from top to bottom of the given triangle.")

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


class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.has_parent = False
        self.data = data
        self.weight = 100 - data
        self.distance = self.weight
        self.result = data
        self.left = left
        self.right = right

    def insert(self, left, right):
        self.left = left
        if (not left.has_parent and left.distance < self.distance + left.weight) or \
                (left.has_parent and left.distance > self.distance + left.weight):
            left.distance = self.distance + left.weight
            left.result = self.result + left.data
            left.has_parent = True

        self.right = right
        if (not right.has_parent and right.distance < self.distance + right.weight) or \
                (right.has_parent and right.distance > self.distance + right.weight):
            right.distance = self.distance + right.weight
            right.result = self.result + right.data
            right.has_parent = True

        return self

    @staticmethod
    def from_triangle_tree(triangle_numbers):
        triangle_nodes = [[TreeNode(number) for number in numbers] for numbers in triangle_numbers]

        for row in range(len(triangle_nodes) - 1):
            next_row = triangle_nodes[row + 1]
            for ix, node in enumerate(triangle_nodes[row]):
                node.insert(next_row[ix], next_row[ix + 1])

        root = triangle_nodes[0][0]
        leafs = triangle_nodes[len(triangle_nodes) - 1]

        return root, leafs


if __name__ == '__main__':
    problem = Problem18(filename="../../../../resources/problem018.txt")

    problem.attempt_1()
    problem.attempt_2()
    problem.official_solution()
