import itertools
import math

from com.patrick.private.utils.benchmark import Benchmark
from com.patrick.private.utils.math_utils import MathUtils


def find_all(a_str: str, sub: str) -> list[int]:
    start = 0
    idx_list = []
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return idx_list

        idx_list.append(start)
        start += len(sub)


class Problem206(object):
    """
    Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
    where each “_” is a single digit.
    """

    def __init__(self, square_pattern: str, sub: str):
        self.square_pattern = square_pattern
        self.sub = sub
        print(f"Problem 206: Find the unique positive integer whose square has the form {self.square_pattern}, "
              f"where each “{self.sub}” is a single digit.")
        print(f"Square pattern={self.square_pattern}")
        print(f"Sub=“{self.sub}”")

    @Benchmark
    def attempt_1(self):
        result = "N/A"

        internal_sub = "_"
        pattern = self.square_pattern.replace(self.sub, internal_sub)

        # if squared number ends in 0, then we know the second last digit is also 0
        if pattern.endswith(internal_sub + "0"):
            pattern = pattern[:-2] + "00"

        base_number = int(pattern.replace(internal_sub, "0"))
        index_of_placeholder = find_all(pattern, internal_sub)
        number_of_placeholder = len(index_of_placeholder)
        power_of_placeholder = [len(pattern) - 1 - n for n in index_of_placeholder]

        for perm in itertools.product(range(9, 0, -1), repeat=number_of_placeholder):
            permuted_number = base_number
            permuted_number += sum([int(n * math.pow(10, power)) for n, power in zip(perm, power_of_placeholder)])

            if MathUtils.is_perfect_square(permuted_number):
                result = math.isqrt(permuted_number)
                print(f"Permutation: {perm}")
                print(f"Permuted number: {permuted_number}")
                break

        print("")
        print(f"Result: {result}")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")


if __name__ == '__main__':
    problem206 = Problem206(square_pattern="1_2_3_4_5_6_7_8_9_0", sub="_")

    problem206.attempt_1()
    problem206.official_solution()
