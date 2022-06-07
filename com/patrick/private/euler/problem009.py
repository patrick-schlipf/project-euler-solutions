from com.patrick.private.utils.benchmark import Benchmark
from com.patrick.private.utils.math_utils import MathUtils

import math


class Problem9(object):
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

            a^2 + b^2 = c^2

    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """

    def __init__(self, expected_sum: int):
        self.expected_sum = expected_sum
        print(f"Problem 9: Find the product a * b * c for the Pythagorean triplet.")
        print(f"a + b + c = {self.expected_sum}")

        assert not self.expected_sum % 2, "The dimension must be even."

    @Benchmark
    def attempt_1(self):
        result = 0

        # https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
        #
        # a + b + c == kx²-ky²+2kxy+kx²+ky² == 2kx²+2kxy == 2kx(x+y)
        # 2kx(x+y) = 1000   | div 2
        # kx(x+y) = 500     | sub s = (x+y)
        # kxs = 500

        n = self.expected_sum // 2
        divisors = MathUtils.divisors(n)

        for x in divisors:
            for s in divisors:
                if x < s < 2 * x and n % (x * s):
                    y = s - x
                    k = n / (x * s)

                    a = k * (math.pow(x, 2) - math.pow(y, 2))
                    b = 2 * k * x * y
                    c = k * (math.pow(x, 2) + math.pow(y, 2))

                    print(f"a: {a}")
                    print(f"b: {b}")
                    print(f"c: {c}")
                    result = a * b * c

        print("")
        print(f"Result: {int(result)}")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")


if __name__ == '__main__':
    problem = Problem9(expected_sum=1_000)

    problem.attempt_1()
    problem.official_solution()
