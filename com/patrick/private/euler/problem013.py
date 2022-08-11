from com.patrick.private.utils.benchmark import Benchmark
from com.patrick.private.utils.math_utils import MathUtils

import math


class Problem13(object):
    """
    Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
    """

    def __init__(self, digits: int, filename: str):
        with open(filename) as f:
            self.numbers = [int(line.strip()) for line in f.readlines()]

        self.digits = digits
        print(f"Problem 13: Work out the first {self.digits} digits of the sum "
              f"of the following one-hundred 50-digit numbers.")

    @Benchmark
    def attempt_1(self):
        result = sum(self.numbers)

        print("")
        print(f"Result: {result}")
        print(f"Result: {math.floor(result / pow(10, MathUtils.len(result) - self.digits))}")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")


if __name__ == '__main__':
    problem = Problem13(digits=10,
                        filename="../../../../resources/problem013.txt")

    problem.attempt_1()
    problem.official_solution()
