from com.patrick.private.utils.benchmark import Benchmark


class Problem13(object):
    """
    The following iterative sequence is defined for the set of positive integers:

            n → n/2 (n is even)
            n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

            13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
    Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
    """

    def __init__(self, limit: int):
        assert limit > 0
        self.limit = limit
        print(f"Problem 14: Which starting number, under {self.limit}, produces the longest collatz chain?")
        print(f"limit={self.limit}")

    @Benchmark
    def attempt_1(self):
        result = 0
        max_steps = 0
        lookup = {1: 1}
        for n in range(self.limit // 2, self.limit):
            steps = calculate_collatz(n, lookup)
            if steps > max_steps:
                max_steps = steps
                result = n

        print("")
        print(f"Result: {result} - {lookup.get(result)}")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")


def calculate_collatz(number, lookup):
    collatz = number
    collatz_list = []
    while collatz > 1:
        if collatz in lookup:
            break

        collatz_list.append(collatz)
        if collatz % 2 == 0:
            collatz //= 2
        else:
            collatz = (3 * collatz) + 1

    collatz_list.reverse()
    steps = lookup.get(collatz)
    for i, num in enumerate(collatz_list, start=1):
        lookup[num] = steps + i

    return lookup[number]


if __name__ == '__main__':
    problem = Problem13(limit=10 ** 6)

    problem.attempt_1()
    problem.official_solution()
