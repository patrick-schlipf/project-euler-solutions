from com.patrick.private.utils.benchmark import Benchmark
from com.patrick.private.utils.math_utils import MathUtils

import math


class Problem6(object):
    """
    The sum of the squares of the first ten natural numbers is,

            1^2 + 2^2 + ... + 10^2 = 385

    The square of the sum of the first ten natural numbers is,

            (1 + 2 + ... + 10)^2 = 55^2 = 3025

    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

            3025 - 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred natural numbers
    and the square of the sum.
    """

    def __init__(self, lower_bound: int, upper_bound: int):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        print(f"Problem 6: Find the difference between the sum of the squares and the square of the sum.")
        print(f"range={self.lower_bound}-{self.upper_bound}")

    @Benchmark
    def attempt_1(self):
        sum_of_squares = 0
        for n in range(self.lower_bound, self.upper_bound + 1):
            sum_of_squares += math.pow(n, 2)

        squares_of_sum = MathUtils.gaussian_sum(self.upper_bound) - MathUtils.gaussian_sum(self.lower_bound - 1)
        squares_of_sum = math.pow(squares_of_sum, 2)

        result = squares_of_sum - sum_of_squares

        print("")
        print(f"Result: {int(result)}")

    @Benchmark
    def official_solution(self):
        upper_limit = self.upper_bound
        lower_limit = self.lower_bound - 1

        sum_upper = upper_limit * (upper_limit + 1) / 2
        sum_lower = lower_limit * (lower_limit + 1) / 2
        sum_n = sum_upper - sum_lower

        sum_sq_upper = (2 * upper_limit + 1) * (upper_limit + 1) * upper_limit / 6
        sum_sq_lower = (2 * lower_limit + 1) * (lower_limit + 1) * lower_limit / 6
        sum_sq = sum_sq_upper - sum_sq_lower
        result = sum_n ** 2 - sum_sq

        print("")
        print(f"Result: {int(result)}")


if __name__ == '__main__':
    problem = Problem6(lower_bound=1, upper_bound=100)

    problem.attempt_1()
    problem.official_solution()
