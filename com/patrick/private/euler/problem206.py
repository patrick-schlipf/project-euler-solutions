import itertools
import math

from com.patrick.private.utils.benchmark import Benchmark


def find_all(a_str: str, sub: str) -> list[int]:
    start = 0
    idx_list = []
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return idx_list

        idx_list.append(start)
        start += 1


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

        # if squared number ends in 0, then we know the second last digit is also 0
        if self.square_pattern.endswith("_0"):
            self.square_pattern = self.square_pattern[:-2] + "00"

        base_number = int(self.square_pattern.replace("_", "0"))
        index_of_placeholder = find_all(self.square_pattern, "_")
        number_of_placeholder = len(index_of_placeholder)
        power_of_placeholder = [len(self.square_pattern) - 1 - n for n in index_of_placeholder]

        for perm in itertools.product(range(9, 0, -1), repeat=number_of_placeholder):
            permutated_number = base_number
            permutated_number += sum([int(n * math.pow(10, power)) for n, power in zip(perm, power_of_placeholder)])

            if math.isqrt(permutated_number) ** 2 == permutated_number:
                result = math.isqrt(permutated_number)
                print(f"Permutation: {perm}")
                print(f"Permutated number: {permutated_number}")
                print(f"Square root: {math.isqrt(permutated_number)}")
                break

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
