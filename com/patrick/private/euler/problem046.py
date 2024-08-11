import math

from com.patrick.private.utils.benchmark import Benchmark
from com.patrick.private.utils.math_utils import MathUtils


class Problem46(object):
    """
    It was proposed by Christian Goldbach that every odd composite number can be written
    as the sum of a prime and twice a square.

        9 = 7 + 2 * 1^2
        15 = 7 + 2 * 2^2
        21 = 3 + 2 * 3^2
        25 = 7 + 2 * 3^2
        27 = 19 + 2 * 2^2
        33 = 31 + 2 * 1^2

    It turns out that the conjecture was false.

    What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
    """

    def __init__(self):
        print("Problem 46: What is the smallest odd composite that cannot be written "
              "as the sum of a prime and twice a square?")

    @Benchmark
    def attempt_1(self):
        result = "N/A"
        found = False

        composite = 3
        while not found:
            # skip if prime
            if MathUtils.is_prime_fast(composite):
                composite += 2
                continue

            upper_bound = math.isqrt(composite // 2)
            for n in range(upper_bound, 0, -1):
                p = composite - 2 * n ** 2
                if MathUtils.is_prime_fast(p):
                    break

            else:
                result = composite
                found = True

            composite += 2

        print("")
        print(f"{p} -> {MathUtils.prime_factors(p)}")
        print(f"Result: {result} = {p} + 2 * {n}^2")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")


if __name__ == '__main__':
    problem = Problem46()

    problem.attempt_1()
    problem.official_solution()
