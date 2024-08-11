import math
from typing import Iterator

import numpy
import sympy


class MathUtils(object):
    phi = (1 + math.sqrt(5)) / 2
    phi_negative = (1 - math.sqrt(5)) / 2

    @staticmethod
    def is_even(number: int) -> bool:
        return number % 2 == 0

    @staticmethod
    def is_odd(number: int) -> bool:
        return number % 2 == 1

    @staticmethod
    def gaussian_sum(number: int) -> float:
        return (number * (number + 1)) / 2

    @staticmethod
    def sum_of_digits(number: str) -> int:
        return sum([int(digit) for digit in number])

    @staticmethod
    def sum_of_digits(number: int) -> int:
        return MathUtils.sum_of_digits(str(number))

    @staticmethod
    def len(number: int) -> int:
        return int(math.log10(number)) + 1

    @staticmethod
    def fibonacci(start: tuple = (0, 1)) -> Iterator[int]:
        """
        The Fibonacci numbers are generated by setting F(0) = 0, F(1) = 1, and then using the recursive formula:

                F(n) = F(n-1) + F(n-2)

        Thus, the sequence begins: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, … .
        """
        prev, curr = start

        while True:
            yield curr
            nxt = prev + curr
            prev = curr
            curr = nxt

    @staticmethod
    def nth_fibonacci(n: int) -> int:
        """
        Returns the n-th number of the Fibonacci sequence.

        a(n) = [φ^n – (-1/φ)^n] / Sqrt[5]

        φ == phi == golden ratio == 1.618033... == (1 + Sqrt[5]) / 2
        """
        return int((pow(MathUtils.phi, n) - pow(MathUtils.phi_negative, n)) / math.sqrt(5))

    @staticmethod
    def is_perfect_square(n: int) -> bool:
        """
        Returns True if the provided number is a
        perfect square (and False otherwise).
        """
        return math.isqrt(n) ** 2 == n

    @staticmethod
    def is_palindrome(n: int) -> bool:
        """Checks if the given number is a palindrome."""
        return str(n) == str(n)[::-1]

    @staticmethod
    def primes_sieve_of_eratosthenes(limit: int) -> Iterator[int]:
        """
        Sieve of Eratosthenes

        Finding all prime numbers up to a given limit.
        """
        a = [True] * limit  # Initialize the primality list
        a[0] = a[1] = False

        for (i, isprime) in enumerate(a):
            if isprime:
                yield i
                for n in range(i * i, limit, i):  # Mark factors non-prime
                    a[n] = False

    @staticmethod
    def is_prime(n: int) -> bool:
        """Primality test using 6k+-1 optimization."""
        if n <= 3:
            return n > 1
        if not n % 2 or not n % 3:
            return False
        i = 5
        stop = int(n ** 0.5)
        while i <= stop:
            if not n % i or not n % (i + 2):
                return False
            i += 6
        return True

    @staticmethod
    def is_prime_fast(n: int) -> bool:
        return sympy.isprime(n)

    @staticmethod
    def prime_factors(number: int) -> list[int]:
        """Returns all prime factors for the given number."""
        factors = [1]
        factor = 2

        # Check if number is even
        if MathUtils.is_even(number):
            factors.append(factor)
            number //= factor
            while MathUtils.is_even(number):
                number //= factor
                factors.append(factor)

        # Now we can skip all even numbers
        factor = 3
        while factor * factor <= number:
            if number % factor == 0:
                number //= factor
                factors.append(factor)
            else:
                factor += 2

        # Add last number
        if number > 1:
            factors.append(number)
        return factors

    @staticmethod
    def divisors(number: int) -> list[int]:
        """Returns a sorted list of all divisors for the given number."""
        divisors = [1]
        for divisor in range(1, int(math.sqrt(number)) + 1):
            if number % divisor == 0:
                divisors.extend([divisor, number // divisor])
        divisors.append(number)
        return sorted(list(set(divisors)))

    @staticmethod
    def sqrt_convergents(number: int, simplify: bool = True) -> Iterator[tuple[int, int]]:
        # https://en.wikipedia.org/wiki/Square_root_of_2#Continued_fraction
        numerator = 1
        denominator = 1
        while True:
            numerator, denominator = numerator + number * denominator, numerator + denominator
            if simplify:
                numerator, denominator = MathUtils.simplify_fraction(numerator, denominator)
            yield numerator, denominator

    @staticmethod
    def simplify_fraction(numerator: int, denominator: int) -> tuple[int, int]:
        gcd = numpy.gcd(numerator, denominator)
        return int(numerator / gcd), int(denominator / gcd)
