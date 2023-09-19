from com.patrick.private.utils.benchmark import Benchmark
from com.patrick.private.utils.math_utils import MathUtils


class Problem(object):
    """
    The first two consecutive numbers to have two distinct prime factors are:

            14 = 2 × 7
            15 = 3 × 5

    The first three consecutive numbers to have three distinct prime factors are:

            644 = 2^2 × 7 × 23
            645 = 3 × 5 × 43
            646 = 2 × 17 × 19

    Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
    """

    def __init__(self, distinct_prime_factors: int, chain: int):
        self.distinct_prime_factors = distinct_prime_factors
        self.chain = chain
        print(f"Problem 47: "
              f"Find the first {self.chain} consecutive integers to have {self.distinct_prime_factors} distinct prime factors each. "
              f"What is the first of these numbers?")
        print(f"distinct_prime_factors={self.distinct_prime_factors}")
        print(f"chain={self.chain}")

    @Benchmark
    def attempt_1(self):
        current_chain = []
        found = False
        number = 1

        while not found:
            prime_factors = MathUtils.prime_factors(number)
            prime_factors.remove(1)

            if len(set(prime_factors)) == self.distinct_prime_factors:
                current_chain.append((number, prime_factors))
            else:
                current_chain = []

            if len(current_chain) == self.chain:
                break

            number += 1

        print(current_chain)
        result = current_chain[0][0]
        print("")
        print(f"Result: {result}")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")


if __name__ == '__main__':
    problem = Problem(distinct_prime_factors=4, chain=4)

    problem.attempt_1()
    problem.official_solution()
