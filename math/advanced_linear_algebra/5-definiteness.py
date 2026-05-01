#!/usr/bin/env python3
"""Calculates the definiteness of a matrix"""
import numpy as np
 
 
def definiteness(matrix):
    """Returns the definiteness of a matrix as a string, or None"""
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1] or matrix.size == 0:
        return None
    if not np.allclose(matrix, matrix.T):
        return None
    eigenvalues = np.linalg.eigvalsh(matrix)
    if np.all(eigenvalues > 0):
        return "Positive definite"
    elif np.all(eigenvalues >= 0):
        return "Positive semi-definite"
    elif np.all(eigenvalues < 0):
        return "Negative definite"
    elif np.all(eigenvalues <= 0):
        return "Negative semi-definite"
    else:
        return "Indefinite"
