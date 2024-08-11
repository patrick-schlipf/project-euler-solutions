import itertools
import math

from com.patrick.private.utils.benchmark import Benchmark
from com.patrick.private.utils.math_utils import MathUtils


class Problem41(object):
    """
    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
    For example, 2143 is a 4-digit pandigital and is also prime.

    What is the largest n-digit pandigital prime that exists?
    """

    def __init__(self,):
        print("Problem 41: What is the largest n-digit pandigital prime that exists?")

    @Benchmark
    def attempt_1(self):
        result = "N/A"
        found = False

        # There is no 9-digit pandigital prime, because it's always divisible by 3
        # No pandigital prime for 8-digit numbers
        upper_bound = 7

        while not found:
            for perm in itertools.permutations(range(upper_bound, 0, -1)):
                pandigit = sum([int(n * math.pow(10, power - 1)) for n, power in zip(perm, range(len(perm), 0, -1))])
                if MathUtils.is_prime_fast(pandigit):
                    result = pandigit
                    found = True
                    break

        print("")
        print(f"Result: {result} is prime")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")


if __name__ == '__main__':
    problem = Problem41()

    problem.attempt_1()
    problem.official_solution()
