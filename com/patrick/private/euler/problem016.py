from com.patrick.private.utils.benchmark import Benchmark
from com.patrick.private.utils.math_utils import MathUtils

import math


class Problem16(object):
    """
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?
    """

    def __init__(self, exponent: int):
        self.exponent = exponent
        print(f"Problem 16: What is the sum of the digits of the number 2^{self.exponent}")
        print(f"exponent={self.exponent}")

    @Benchmark
    def attempt_1(self):
        result = MathUtils.sum_of_digits(pow(2, self.exponent))
        print("")
        print(f"Result: {result}")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")


if __name__ == '__main__':
    problem = Problem16(exponent=1000)

    problem.attempt_1()
    problem.official_solution()
