from math import log as ln

from com.patrick.private.utils.benchmark import Benchmark
from com.patrick.private.utils.math_utils import MathUtils

import math


class Problem7(object):
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10 001st prime number?
    """

    def __init__(self, nth_prime: int):
        self.nth_prime = nth_prime
        print(f"Problem 7: What is the {self.nth_prime} prime number?")
        print(f"nth_prime={self.nth_prime}")

    @Benchmark
    def attempt_1(self):
        result = 0

        # Prime number theorem - where n is the nth prime
        # ------------------------------------------------------------------------------------------------------------
        #       n * ln(n) + n * (ln(ln(n)) − 1) < nth_prime < n * ln(n) + n * ln(ln(n)) for n≥6
        # ------------------------------------------------------------------------------------------------------------
        n = self.nth_prime
        # lower_bound = n * ln(n) + n * (ln(ln(n)) - 1)
        upper_bound = n * ln(n) + n * ln(ln(n))
        # ------------------------------------------------------------------------------------------------------------

        prime = MathUtils.primes_sieve_of_eratosthenes(int(upper_bound))
        for n in range(self.nth_prime - 1):
            result = next(prime)

        print("")
        print(f"Result: {result}")

    @Benchmark
    def official_solution(self):
        result = 1
        count = 1

        while count != self.nth_prime:
            result += 2
            if MathUtils.is_prime(result):
                count += 1

        print("")
        print(f"Result: {result}")


if __name__ == '__main__':
    problem = Problem7(nth_prime=10_001)

    problem.attempt_1()
    problem.official_solution()
