import math


class MathUtils(object):

    @staticmethod
    def gaussian_sum(number: int) -> float:
        return (number * (number + 1)) / 2

    @staticmethod
    def sum_of_digits(number: str) -> int:
        return sum([int(i) for i in number])

    @staticmethod
    def sum_of_digits(number: int) -> int:
        return sum([int(i) for i in str(number)])

    @staticmethod
    def calculate_fibonacci(start: tuple):
        prev, curr = start

        while True:
            yield curr
            nxt = prev + curr
            prev = curr
            curr = nxt

    @staticmethod
    def is_perfect_square(n: int) -> bool:
        """
        Returns True if the provided number is a
        perfect square (and False otherwise).
        """
        return math.isqrt(n) ** 2 == n

    @staticmethod
    def is_palindrome(n: int) -> bool:
        return str(n) == str(n)[::-1]

    @staticmethod
    def primes_sieve(limit):
        a = [True] * limit  # Initialize the primality list
        a[0] = a[1] = False

        for (i, isprime) in enumerate(a):
            if isprime:
                yield i
                for n in range(i * i, limit, i):  # Mark factors non-prime
                    a[n] = False

    @staticmethod
    def is_prime(n):
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
    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    @staticmethod
    def divisors(n):
        divs = [1]
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                divs.extend([i, n // i])
        divs.append(n)
        return sorted(list(set(divs)))
