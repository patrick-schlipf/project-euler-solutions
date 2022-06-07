from com.patrick.private.utils.benchmark import Benchmark
from com.patrick.private.utils.math_utils import MathUtils

import math


class Problem10(object):
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    """

    def __init__(self, limit: int):
        self.limit = limit
        print(f"Problem 10: Find the sum of all the primes below {self.limit}.")
        print(f"limit={self.limit}")

    @Benchmark
    def attempt_1(self):
        result = sum([int(prime) for prime in MathUtils.primes_sieve(self.limit)])
        print("")
        print(f"Result: {result}")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")


if __name__ == '__main__':
    problem = Problem10(limit=int(2e6))

    problem.attempt_1()
    problem.official_solution()
