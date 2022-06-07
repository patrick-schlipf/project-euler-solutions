from com.patrick.private.utils.benchmark import Benchmark
from com.patrick.private.utils.math_utils import MathUtils


class Problem26(object):
    """
    A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions
    with denominators 2 to 10 are given:

                1/2	= 	0.5
                1/3	= 	0.(3)
                1/4	= 	0.25
                1/5	= 	0.2
                1/6	= 	0.1(6)
                1/7	= 	0.(142857)
                1/8	= 	0.125
                1/9	= 	0.(1)
                1/10= 	0.1

    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit
    recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
    """

    def __init__(self, limit: int):
        self.limit = limit
        print(f"Problem 26: Find the value of d < {self.limit} for which 1/d contains "
              f"the longest recurring cycle in its decimal fraction part.")
        print(f"limit={self.limit}")

    @Benchmark
    def attempt_1(self):
        result = 0
        max_cycle_length = 0
        reversed_primes = list(MathUtils.primes_sieve_of_eratosthenes(self.limit))[::-1]
        for prime in reversed_primes:
            if prime < max_cycle_length:
                break

            print(f"Checking: {prime}")

            # Long division
            stop_condition = prime // 2
            mod = 10
            seen = [False] * prime
            cycle_length = 0
            while mod != 0:
                div, mod = divmod(mod, prime)
                if seen[mod]:
                    break

                seen[mod] = True
                mod *= 10
                cycle_length += 1

                # If cycle length is bigger than "prime / 2", the cycle length is always "prime - 1"
                #   If the repetend length of "1/p" for prime p is equal to "p − 1"
                #   then the repetend, expressed as an integer, is called a cyclic number.
                #   https://en.wikipedia.org/wiki/Repeating_decimal#Fractions_with_prime_denominators
                if cycle_length > stop_condition:
                    cycle_length = prime - 1
                    break

            if max_cycle_length < cycle_length:
                max_cycle_length = cycle_length
                result = prime

        print(f"Cycle length: {max_cycle_length}")
        print("")
        print(f"Result: {result}")

    @Benchmark
    def attempt_2(self, force: bool = False):
        if not force and self.limit >= 10_000:
            print("This method will print the cyclic period.")
            print("Limit must be < 10_000")
            return

        result = 2
        max_cycle = ""
        max_cycle_length = 0
        for prime in list(MathUtils.primes_sieve_of_eratosthenes(self.limit))[::-1]:
            if prime < max_cycle_length:
                break

            print(f"Checking: {prime}")

            mod = 10
            seen = [False] * prime
            cycle = 0
            cycle_length = 0
            while mod != 0:
                div, mod = divmod(mod, prime)
                if seen[mod]:
                    break

                seen[mod] = True
                mod *= 10
                cycle = 10 * cycle + div
                cycle_length += 1

            if max_cycle_length < cycle_length:
                max_cycle_length = cycle_length
                max_cycle = cycle
                result = prime

        print(f"Max cycle: 0.({max_cycle})")
        print(f"Cycle length: {max_cycle_length}")
        print("")
        print(f"Result: {result}")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")


if __name__ == '__main__':
    problem = Problem26(limit=1_000)

    problem.attempt_1()

    # calculates the cycle, thus slower
    problem.attempt_2()

    problem.official_solution()
