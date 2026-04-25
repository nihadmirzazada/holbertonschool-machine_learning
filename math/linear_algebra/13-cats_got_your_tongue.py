#!/usr/bin/env python3
"""Module for concatenating two numpy ndarrays along a specific axis."""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenate two numpy ndarrays along a specific axis.

    Args:
        mat1: A numpy ndarray.
        mat2: A numpy ndarray.
        axis: The axis along which to concatenate (default 0).

    Returns:
        A new numpy ndarray with mat1 and mat2 concatenated.
    """
    return np.concatenate((mat1, mat2), axis=axis)
