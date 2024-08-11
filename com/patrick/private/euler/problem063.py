from com.patrick.private.utils.benchmark import Benchmark
from com.patrick.private.utils.math_utils import MathUtils


class Problem63(object):
    """
    The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

    How many n-digit positive integers exist which are also an nth power?
    """

    def __init__(self):
        print("Problem 63: How many n-digit positive integers exist which are also an nth power?")

    @Benchmark
    def attempt_1(self):
        result = 0

        # 10^n always produces (n+1)-digit numbers
        base_limit = 9

        # 9^n always produces n-digit numbers up to this limit
        exp_limit = self.calculate_limit()

        # n^1 produces n-digit numbers for n<10
        # 9^n produces n-digit numbers for n<=exp_limit
        # 9^1 is added twice, so remove the duplicate from the result
        result = base_limit + exp_limit - 1

        for base in range(1, base_limit):
            for exponent in range(2, exp_limit):
                num = pow(base, exponent)
                if MathUtils.len(num) == exponent:
                    print(f"{base}^{exponent} = {num}")
                    result += 1

        print("")
        print(f"Result: {result}")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")

    def calculate_limit(self):
        exponent = 1
        while MathUtils.len(pow(9, exponent)) == exponent:
            exponent += 1

        return exponent - 1


if __name__ == '__main__':
    problem = Problem63()

    problem.attempt_1()
    problem.official_solution()
