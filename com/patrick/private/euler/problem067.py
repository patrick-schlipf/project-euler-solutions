from operator import attrgetter

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

        print(f"Problem 67: Find the maximum total from top to bottom of the given triangle.")

    @Benchmark
    def attempt_1(self):
        result = 0

        root, leafs = TreeNode.from_triangle_tree(self.triangle_numbers)

        result = max(leafs, key=attrgetter('result')).result

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
    problem = Problem67(filename="../../../../resources/problem067.txt")

    problem.attempt_1()
    problem.official_solution()
