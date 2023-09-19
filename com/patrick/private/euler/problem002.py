from com.patrick.private.utils.benchmark import Benchmark
from com.patrick.private.utils.math_utils import MathUtils


class Problem2(object):
    """
    Each new term in the Fibonacci sequence is generated by adding the previous two terms.
    By starting with 1 and 2, the first 10 terms will be:

            1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not exceed four million,
    find the sum of the even-valued terms.
    """

    def __init__(self, upper_limit: int):
        self.upper_limit = upper_limit
        print(f"Problem 2: Find the sum of the even Fibonacci numbers up to {self.upper_limit}.")
        print(f"limit={self.upper_limit}")

    @Benchmark
    def attempt_1(self):
        total = 0
        number = 0
        fib = MathUtils.fibonacci()
        while number <= self.upper_limit:
            if MathUtils.is_even(number):
                total += number

            number = next(fib)

        print("")
        print(f"Result: {total}")

    @Benchmark
    def official_solution(self):
        total = 0
        number = 0
        fib = self.even_fibonacci(start=(0, 2))

        while number <= self.upper_limit:
            total += number
            number = next(fib)

        print("")
        print(f"Result: {total}")

    @staticmethod
    def even_fibonacci(start: tuple):
        prev, curr = start

        while True:
            yield curr
            nxt = 4 * curr + prev
            prev = curr
            curr = nxt


if __name__ == '__main__':
    problem = Problem2(upper_limit=int(4e6))

    problem.attempt_1()
    problem.official_solution()
