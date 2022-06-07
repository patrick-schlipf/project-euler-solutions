from com.patrick.private.utils.benchmark import Benchmark


class Problem28(object):
    """
    Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

        21 22 23 24 25
        20  7  8  9 10
        19  6  1  2 11
        18  5  4  3 12
        17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
    """

    def __init__(self, dimension: int):
        self.dimension = dimension
        print(f"Problem 28: Sum of the numbers on the diagonals in a {self.dimension}x{self.dimension} spiral.")
        print(f"dimension={self.dimension}")

        assert dimension % 2, "The dimension must be odd."

    @Benchmark
    def attempt_1(self):
        last_number = self.dimension ** 2
        print(f"Last number = {last_number}")

        total = 1
        curr = 1
        iteration = 0
        while curr < last_number:
            iteration += 1
            diff = 2 * iteration
            for _ in range(4):
                curr += diff
                total += curr

        print(f"Iterations needed: {iteration}")
        print("")
        print(f"Result: {total}")

    @Benchmark
    def attempt_2(self):
        total = 1
        iteration = 0
        # max_iterations = (self.dimension - 1) / 2
        # for iteration in range(1, max_iterations):
        #    n = 2 * iteration - 1
        #    diff = 6 * iteration
        #    highest = n ** 2
        #    lowest = highest - diff
        #    spiral_sum = 2 * (highest + lowest)
        #    total += spiral_sum
        #
        #    ... then simplify to get the below algorithm

        max_range = self.dimension + 1
        for n in range(3, max_range, 2):
            total += (4 * n ** 2) - 6 * (n - 1)
            iteration += 1

        print(f"Iterations needed: {iteration}")
        print("")
        print(f"Result: {total}")

    @Benchmark
    def official_solution(self):
        diagonals = [1]
        n = 3
        iteration = 0
        while n <= self.dimension:
            square = n * n
            diff = n - 1

            diagonals.append(square - 3 * diff)
            diagonals.append(square - 2 * diff)
            diagonals.append(square - diff)
            diagonals.append(square)

            n += 2
            iteration += 1

        total = sum(diagonals)

        print(f"Iterations needed: {iteration}")
        print("")
        print(f"Result: {total}")


if __name__ == '__main__':
    problem28 = Problem28(dimension=1001)

    problem28.attempt_1()
    problem28.attempt_2()
    problem28.official_solution()
