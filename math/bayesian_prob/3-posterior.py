#!/usr/bin/env python3
"""Posterior probability module for Bayesian probability"""
import numpy as np


def posterior(x, n, P, Pr):
    """Calculate posterior probability for hypothetical probabilities.

    Args:
        x: patients with severe side effects
        n: total patients observed
        P: 1D numpy.ndarray of hypothetical probabilities
        Pr: 1D numpy.ndarray of prior beliefs

    Returns:
        1D numpy.ndarray of posterior probabilities
    """
    inter = __import__('1-intersection').intersection
    marg = __import__('2-marginal').marginal
    return inter(x, n, P, Pr) / marg(x, n, P, Pr)
