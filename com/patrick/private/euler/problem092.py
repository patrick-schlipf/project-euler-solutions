import itertools
from collections import Counter

from com.patrick.private.utils.benchmark import Benchmark
from com.patrick.private.utils.math_utils import MathUtils

import math


class Problem92(object):
    """
    A number chain is created by continuously adding the square of the digits in a number
    to form a new number until it has been seen before.

    For example,

    44 → 32 → 13 → 10 → 1 → 1
    85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

    Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
    What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

    How many starting numbers below ten million will arrive at 89?
    """

    def __init__(self, limit: int):
        self.limit = limit
        print(f"Problem 92: How many starting numbers below {self.limit:_} will arrive at 89?")
        print(f"limit={self.limit:_}")

    @Benchmark
    def attempt_1(self):
        result = 0
        square_digit = {str(i): i ** 2 for i in range(10)}.get

        cache_size = (9 ** 2) * MathUtils.len(self.limit - 1) + 1
        cache = [False] * cache_size
        cache[1] = 1
        cache[89] = 89

        # calculate the first 567 numbers - 9^2 * 7 digits
        for num in range(1, len(cache)):
            next_num = int(sum(map(square_digit, str(num))))
            while not cache[next_num] and next_num != 1 and next_num != 89:
                next_num = int(sum(map(square_digit, str(next_num))))

            cache[num] = cache[next_num]

        result = cache.count(89)

        for num in range(len(cache), self.limit):
            next_num = int(sum(map(square_digit, str(num))))

            if cache[next_num] == 89:
                result += 1

        print("")
        print(f"Result: {result}")

    @Benchmark
    def attempt_2(self):
        happy_numbers = 0
        # pick a number to permutate [1..n]
        size = MathUtils.len(self.limit - 1)
        square_digit = {str(i): i ** 2 for i in range(0, 10)}.get

        cache_size = (9 ** 2) * MathUtils.len(self.limit - 1) + 1
        cache = [False] * cache_size
        cache[1] = 1
        cache[89] = 89

        # calculate the first 567 numbers - 9^2 * 7 digits
        for num in range(1, len(cache)):
            next_num = int(sum(map(square_digit, str(num))))
            while not cache[next_num] and next_num != 1 and next_num != 89:
                next_num = int(sum(map(square_digit, str(next_num))))

            cache[num] = cache[next_num]

        square_digit = {i: i ** 2 for i in range(0, 10)}.get
        for combination in itertools.combinations_with_replacement(range(10), size):
            next_num = int(sum(map(square_digit, combination)))

            if cache[next_num] == 1:
                res = Counter(combination)

                permutations = \
                    math.factorial(sum(n for n in res.values())) // \
                    math.prod(math.factorial(n) for n in res.values())
                happy_numbers += permutations

        # subtract the happy numbers and also the combination for 0
        result = self.limit - happy_numbers - 1

        print("")
        print(f"Result: {result}")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")

    @staticmethod
    def get_digits_str(num):
        for n_str in str(num):
            yield int(n_str)


if __name__ == '__main__':
    problem = Problem92(limit=int(1e7))

    problem.attempt_1()
    problem.attempt_2()
    problem.official_solution()
