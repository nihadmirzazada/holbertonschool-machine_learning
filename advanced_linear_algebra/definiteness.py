#!/usr/bin/env python3
"""Definiteness module"""
import numpy as np
 
 
class Definiteness:
    """Calculates the definiteness of a matrix"""
 
    @staticmethod
    def calculate(matrix):
        """Returns Positive definite / Positive semi-definite /
        Negative definite / Negative semi-definite / Indefinite / None"""
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
