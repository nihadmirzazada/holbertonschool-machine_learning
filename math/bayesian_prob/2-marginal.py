#!/usr/bin/env python3
"""Marginal probability module for Bayesian probability"""
import numpy as np


def marginal(x, n, P, Pr):
    """Calculate the marginal probability of obtaining the data.

    Args:
        x: patients with severe side effects
        n: total patients observed
        P: 1D numpy.ndarray of hypothetical probabilities
        Pr: 1D numpy.ndarray of prior beliefs

    Returns:
        float: marginal probability
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError(
            "Pr must be a numpy.ndarray with the same shape as P")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")
    if np.any(Pr < 0) or np.any(Pr > 1):
        raise ValueError("All values in Pr must be in the range [0, 1]")
    if not np.isclose(Pr.sum(), 1):
        raise ValueError("Pr must sum to 1")

    c = 1
    for i in range(x):
        c = c * (n - i) // (i + 1)
    lk = float(c) * (P ** x) * ((1 - P) ** (n - x))
    return np.sum(lk * Pr)
