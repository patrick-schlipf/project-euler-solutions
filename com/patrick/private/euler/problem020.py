import math

from com.patrick.private.utils.benchmark import Benchmark
from com.patrick.private.utils.math_utils import MathUtils


class Problem20(object):
    """
    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
    """

    def __init__(self, number: int):
        self.number = number
        print(f"Problem 20: Find the sum of the digits in the number {self.number}!")
        print(f"number={self.number}")

    @Benchmark
    def attempt_1(self):
        result = MathUtils.sum_of_digits(math.factorial(self.number))

        print("")
        print(f"Result: {result}")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")


if __name__ == '__main__':
    problem = Problem20(number=100)

    problem.attempt_1()
    problem.official_solution()
