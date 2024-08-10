from com.patrick.private.utils.benchmark import Benchmark
from com.patrick.private.utils.math_utils import MathUtils


class Problem57(object):
    """
    It is possible to show that the square root of two can be expressed as an infinite continued fraction.
    By expanding this for the first four iterations, we get:

    1 + \frac 1 2 = \frac  32 = 1.5
    1 + \frac 1 {2 + \frac 1 2} = \frac 7 5 = 1.4
    1 + \frac 1 {2 + \frac 1 {2+\frac 1 2}} = \frac {17}{12} = 1.41666 \dots
    1 + \frac 1 {2 + \frac 1 {2+\frac 1 {2+\frac 1 2}}} = \frac {41}{29} = 1.41379 \dots

    The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985,
    is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

    In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
    """

    def __init__(self, steps: int):
        self.steps = steps
        print(f"Problem 57: In the first {self.steps} expansions, "
              f"how many fractions contain a numerator with more digits than the denominator?")
        print(f"steps={self.steps}")

    @Benchmark
    def attempt_1(self):
        result = 0

        sqrt_2_convergents = MathUtils.sqrt_convergents(2, simplify=False)

        for _ in range(self.steps + 1):
            numerator, denominator = next(sqrt_2_convergents)
            if MathUtils.len(numerator) > MathUtils.len(denominator):
                result += 1

        print("")
        print(f"Result: {result}")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")


if __name__ == '__main__':
    problem = Problem57(steps=1000)

    problem.attempt_1()
    problem.official_solution()
