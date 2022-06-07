from com.patrick.private.utils.benchmark import Benchmark
from com.patrick.private.utils.math_utils import MathUtils


class Problem1(object):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """

    def __init__(self, upper_limit: int):
        self.upper_limit = upper_limit - 1
        print(f"Problem 1: Find the sum of all the multiples of 3 or 5 below {self.upper_limit + 1}.")
        print(f"limit={self.upper_limit}")

    @Benchmark
    def attempt_1(self):
        total = self.sum_multiples_of(3) + self.sum_multiples_of(5) - self.sum_multiples_of(3 * 5)
        print("")
        print(f"Result: {total:.0f}")

    def sum_multiples_of(self, digit: int):
        # amount of multiples below the limit
        multiples = self.upper_limit // digit

        total = MathUtils.gaussian_sum(multiples) * digit

        print(f"Sum of the multiples of {digit}: {total:.0f}")
        return total

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")


if __name__ == '__main__':
    problem = Problem1(upper_limit=1000)

    problem.attempt_1()
    problem.official_solution()
