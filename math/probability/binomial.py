#!/usr/bin/env python3
"""Binomial distribution"""


class Binomial:
    """Represents a Binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize Binomial distribution"""
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError(
                    "p must be greater than 0 and less than 1"
                )
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            p = 1 - (variance / mean)
            n = mean / p
            self.n = round(n)
            self.p = mean / self.n

    def _factorial(self, k):
        """Returns factorial of k"""
        result = 1
        for i in range(2, k + 1):
            result *= i
        return result

    def pmf(self, k):
        """Calculates the PMF for a given number of successes"""
        k = int(k)
        if k < 0 or k > self.n:
            return 0
        comb = (self._factorial(self.n) //
                (self._factorial(k) * self._factorial(self.n - k)))
        return comb * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """Calculates the CDF for a given number of successes"""
        k = int(k)
        if k < 0:
            return 0
        return sum(self.pmf(i) for i in range(k + 1))
