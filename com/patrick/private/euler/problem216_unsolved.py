from com.patrick.private.utils.benchmark import Benchmark
from com.patrick.private.utils.math_utils import MathUtils

import math


class Problem216(object):
    """
    Consider numbers t(n) of the form t(n) = 2n2-1 with n > 1.
    The first such numbers are 7, 17, 31, 49, 71, 97, 127 and 161.
    It turns out that only 49 = 7*7 and 161 = 7*23 are not prime.
    For n ≤ 10000 there are 2202 numbers t(n) that are prime.

    How many numbers t(n) are prime for n ≤ 50,000,000 ?
    """

    def __init__(self, limit: int):
        self.limit = limit
        print(f"Problem 216: How many numbers t(n) are prime for n ≤ {self.limit} ?")
        print(f"limit={self.limit}")

    @Benchmark
    def attempt_1(self):
        result = 0
        for n in range(2, self.limit):
            fn = 2 * (n ** 2) - 1
            if MathUtils.is_prime(fn):
                result += 1
                # print(f"{n}: True  - {fn}")
            # else:
            # print(f"{n}: False - {fn}")

        print("")
        print(f"Result: {result}")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")


if __name__ == '__main__':
    problem = Problem216(limit=10_000)

    problem.attempt_1()
    problem.official_solution()
