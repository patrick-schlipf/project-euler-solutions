from com.patrick.private.utils.benchmark import Benchmark


class Problem250(object):
    """
    Find the number of non-empty subsets of

            {1^1, 2^2, 3^3, ..., 250250^250250}

    the sum of whose elements is divisible by 250.

    Enter the rightmost 16 digits as your answer.
    """

    def __init__(self, size: int, divisor: int):
        self.size = size
        self.divisor = divisor
        print(f"Problem 250: Find the number of non-empty subsets of {{1^1, 2^2, 3^3, ..., {self.size}^{self.size}}} "
              f"the sum of whose elements is divisible by {self.divisor}.")
        print(f"size={self.size}")
        print(f"divisor={self.divisor}")

    @Benchmark
    def attempt_1(self):
        # 3blue1brown - Olympiad level counting
        # https://www.youtube.com/watch?v=bOXCLR3Wric
        # if the set was {1, 2, 3, ..., 250250}, then the result would be
        #       result = "1/250 * ( 2^250250 + 249 * 2^1001)"

        result = False
        print("")
        print(f"Result: {result}")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")


if __name__ == '__main__':
    problem = Problem250(size=250250, divisor=250)

    problem.attempt_1()
    problem.official_solution()
