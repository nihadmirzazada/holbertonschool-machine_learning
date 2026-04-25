#!/usr/bin/env python3
"""Module for performing matrix multiplication using numpy."""
import numpy as np


def np_matmul(mat1, mat2):
    """Perform matrix multiplication on two numpy ndarrays.

    Args:
        mat1: A numpy ndarray.
        mat2: A numpy ndarray.

    Returns:
        A new numpy ndarray representing the matrix product.
    """
    return np.matmul(mat1, mat2)
