#!/usr/bin/env python3
"""Module for element-wise operations on numpy ndarrays."""
import numpy as np


def np_elementwise(mat1, mat2):
    """Perform element-wise addition, subtraction, multiplication, division.

    Args:
        mat1: A numpy ndarray.
        mat2: A numpy ndarray or scalar.

    Returns:
        A tuple of (sum, difference, product, quotient) as numpy ndarrays.
    """
    mat1, mat2 = np.array(mat1), np.array(mat2)
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
