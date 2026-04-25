#!/usr/bin/env python3
"""Module for transposing a numpy ndarray."""
import numpy as np


def np_transpose(matrix):
    """Transpose a numpy ndarray.

    Args:
        matrix: A numpy ndarray.

    Returns:
        A new numpy ndarray representing the transposed matrix.
    """
    return np.array(matrix).T
