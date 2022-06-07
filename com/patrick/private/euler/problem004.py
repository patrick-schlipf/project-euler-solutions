from com.patrick.private.utils.benchmark import Benchmark
from com.patrick.private.utils.math_utils import MathUtils

import math


class Problem4(object):
    """
    A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers is

            9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    """

    def __init__(self, digits: int):
        self.digits = digits
        self.lower_bound = int(math.pow(10, self.digits - 1))
        self.upper_bound = int(math.pow(10, self.digits) - 1)
        print(f"Problem 4: Find the largest palindrome made from the product of two {self.digits}-digit numbers.")
        print(f"range={self.lower_bound}-{self.upper_bound}")

    @Benchmark
    def attempt_1(self):
        result = 0

        for a in range(self.upper_bound, self.lower_bound - 1, -1):
            for b in range(a, self.lower_bound - 1, -1):
                temp = a * b
                if temp <= result:
                    break
                if MathUtils.is_palindrome(temp):
                    result = temp

        print("")
        print(f"Result: {result}")

    @Benchmark
    def official_solution(self):
        result = 0

        for a in range(self.upper_bound, self.lower_bound - 1, -1):
            if a % 11 == 0:
                b_upper_bound = 999
                step = 1
            else:
                b_upper_bound = 990  # The largest number less than or equal 999 and divisible by 11
                step = 11

            for b in range(b_upper_bound, self.lower_bound - 1, -step):
                temp = a * b
                if temp <= result:
                    break
                if MathUtils.is_palindrome(temp):
                    result = temp

        print("")
        print(f"Result: {result}")


if __name__ == '__main__':
    problem = Problem4(digits=3)

    problem.attempt_1()
    problem.official_solution()
