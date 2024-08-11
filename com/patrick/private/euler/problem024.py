import itertools
from functools import reduce
from typing import Iterable, Iterator

from com.patrick.private.utils.benchmark import Benchmark


class Problem24(object):
    """
    A permutation is an ordered arrangement of objects.
    For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
    If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
    The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
    """

    def __init__(self, digits: Iterable[int], nth_permutation: int):
        self.digits = digits
        self.nth_permutation = nth_permutation
        print(f"Problem 24: What is the {self.nth_permutation:_}th lexicographic permutation "
              f"of the digits {self.digits}?")
        print(f"digit_set={self.digits}")
        print(f"nth_permutation={self.nth_permutation:_}")

    @Benchmark
    def attempt_1(self):
        result = "N/A"

        permutation = itertools.permutations(self.digits)
        for _ in range(self.nth_permutation):
            result = next(permutation)

        result = reduce(lambda x, y: x * 10 + y, result)
        print("")
        print(f"Result: {result}")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")


if __name__ == '__main__':
    problem = Problem24(digits=range(10), nth_permutation=1_000_000)

    problem.attempt_1()
    problem.official_solution()
