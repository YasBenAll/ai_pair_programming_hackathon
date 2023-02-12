"""
We will explore the hypothesis unit testing library.
https://hypothesis.readthedocs.io/en/latest/

Hypothesis is a library for property-based testing.
It is a testing library that allows you to write tests which are parameterized by some specification of data.

Write a test for the following functions.
Apply the decorator @given to a test function to make it a property-based test.
https://hypothesis.readthedocs.io/en/latest/details.html#hypothesis.given

Make adjustments to your use of hypothesis for a succesfull test.

"""
from hypothesis import given, strategies as st


def gcd(n, m):
    """Compute the GCD of two integers by Euclid's algorithm."""

    n, m = abs(n), abs(m)
    n, m = min(n, m), max(n, m)  # Sort their absolute values.
    while m % n:  # While `n` doesn't divide into `m`:
        n, m = m % n, n  # update the values of `n` amd `m`.
    return n


def pythagorean_triple(a, b, c):
    """Check if the given numbers are a Pythagorean triple."""

    return a**2 + b**2 == c**2


def is_prime(n):
    """Check if the given number is a prime number."""

    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
