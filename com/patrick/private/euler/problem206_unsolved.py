import math

from com.patrick.private.utils.benchmark import Benchmark


class Problem206(object):
    """
    Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
    where each “_” is a single digit.
    """

    def __init__(self, square_pattern: str):
        self.square_pattern = square_pattern
        print("Problem 206: Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0, "
              "where each “_” is a single digit.")
        print(f"Square pattern={self.square_pattern}")

    @Benchmark
    def attempt_1(self):
        result = "N/A"
        print(self.square_pattern)
        print(f"{int(math.sqrt(1928374655647380910)) ** 2:.0f}")
        print("")
        print(f"Result: {result}")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")


if __name__ == '__main__':
    problem206 = Problem206(square_pattern="1_2_3_4_5_6_7_8_9_0")

    problem206.attempt_1()
    problem206.official_solution()
