from com.patrick.private.utils.benchmark import Benchmark
from com.patrick.private.utils.math_utils import MathUtils

import math


class Problem5(object):
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """

    def __init__(self, limit: int):
        self.limit = limit
        print(f"Problem 5: What is the smallest positive number that is evenly divisible "
              f"by all of the numbers from 1 to {self.limit}.")
        print(f"limit={self.limit}")

    @Benchmark
    def attempt_1(self):
        # Brute force
        result = self.limit * (self.limit - 1)
        divisors = list(range(int(self.limit / 2) + 1, self.limit + 1))
        print(f"Divisors: {divisors}")

        if self.limit > 2:
            while True:
                is_result = True
                for div in divisors:
                    if result % div != 0:
                        is_result = False
                        break

                if is_result:
                    break

                result += self.limit * (self.limit - 1)

        print("")
        print(f"Result: {result}")

    @Benchmark
    def attempt_2(self):
        # Prime factorization
        result = 1
        prime_factors = [MathUtils.prime_factors(n) for n in range(1, self.limit + 1)]

        smallest_common_factors = []

        for factors in prime_factors:
            for factor in factors:
                if smallest_common_factors.count(factor) < factors.count(factor):
                    smallest_common_factors.append(factor)

        print(f"Smalles common factors: {smallest_common_factors}")
        for n in smallest_common_factors:
            result *= n

        print("")
        print(f"Result: {result}")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")


if __name__ == '__main__':
    problem = Problem5(limit=20)

    problem.attempt_1()
    problem.attempt_2()
    problem.official_solution()
