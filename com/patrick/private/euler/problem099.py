import math

from com.patrick.private.utils.benchmark import Benchmark


class Problem99(object):
    """
    Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that
    2^11 = 2048 < 3^7 = 2187.

    However, confirming that 632382^518061 > 519432^525806 would be much more difficult,
    as both numbers contain over three million digits.

    Using base_exp.txt, a 22K text file containing one thousand lines with a base/exponent pair on each line,
    determine which line number has the greatest numerical value.

    NOTE: The first two lines in the file represent the numbers in the example given above.
    """

    def __init__(self, filename: str):
        with open(filename) as f:
            self.base_exp = [[int(n) for n in line.split(",")] for line in f.readlines()]

        print(f"Problem 99: Determine which line number has the greatest numerical value.")

    @Benchmark
    def attempt_1(self):
        num = self.base_exp[0]
        log = num[1] * math.log(num[0])
        max_ix = 0
        max_num = log
        min_ix = 0
        min_num = log

        for ix, num in enumerate(self.base_exp):
            log = num[1] * math.log(num[0])
            if max_num < log:
                max_num = log
                max_ix = ix
            if min_num > log:
                min_num = log
                min_ix = ix

        print(f"Max: {max_ix + 1} - {self.base_exp[max_ix][0]}^{self.base_exp[max_ix][1]}")
        print(f"Min: {min_ix + 1} - {self.base_exp[min_ix][0]}^{self.base_exp[min_ix][1]}")
        result = max_ix + 1
        print("")
        print(f"Result: {result}")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")


if __name__ == '__main__':
    problem = Problem99(filename="../../../../resources/problem099.txt")

    problem.attempt_1()
    problem.official_solution()
