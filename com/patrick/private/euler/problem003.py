import math

from com.patrick.private.utils.benchmark import Benchmark
from com.patrick.private.utils.math_utils import MathUtils


class Problem3(object):
    """
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    """

    def __init__(self, number: int):
        self.number = number
        print(f"Problem 3: What is the largest prime factor of the number {self.number} ")
        print(f"number={self.number}")

    @Benchmark
    def attempt_1(self):
        factors = [1]
        n = self.number

        primes = MathUtils.primes_sieve(10000)
        for prime in primes:
            if n < prime:
                break

            while n != 0 and n % prime == 0:
                factors.append(prime)
                n /= prime

        print("")
        print(f"Prime factors: {factors}")
        print(f"Result: {max(factors)}")

    @Benchmark
    def attempt_2(self):
        factors = MathUtils.prime_factors(self.number)
        print("")
        print(f"Prime factors: {factors}")
        print(f"Result: {max(factors)}")

    @Benchmark
    def official_solution(self):
        factors = [1]
        n = self.number

        factor = 2

        if n % factor == 0:
            factors.append(factor)
            n /= factor
            while n % factor == 0:
                n /= factor

        factor = 3
        max_factor = math.isqrt(n)

        while n > 1 and factor <= max_factor:
            if n % factor == 0:
                factors.append(factor)
                n /= factor
                while n % factor == 0:
                    n /= factor

                max_factor = math.isqrt(int(n))

            factor += 2

        if n > 1:
            factors.append(int(n))

        print("")
        print(f"Prime factors: {factors}")
        print(f"Result: {max(factors)}")


if __name__ == '__main__':
    problem = Problem3(number=600851475143)

    problem.attempt_1()
    problem.attempt_2()
    problem.official_solution()
