#!/usr/bin/env python3
"""Module for mean and covariance calculation."""
import numpy as np


def mean_cov(X):
    """Calculate the mean and covariance of a data set.

    Args:
        X (numpy.ndarray): shape (n, d) containing the data set.

    Returns:
        tuple: mean of shape (1, d), covariance of shape (d, d).
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise TypeError("X must be a 2D numpy.ndarray")
    n, d = X.shape
    if n < 2:
        raise ValueError("X must contain multiple data points")
    mean = np.mean(X, axis=0, keepdims=True)
    X_c = X - mean
    cov = (X_c.T @ X_c) / (n - 1)
    return mean, cov
