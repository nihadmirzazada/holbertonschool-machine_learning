#!/usr/bin/env python3
"""Inverse module"""
from advanced_linear_algebra.determinant import Determinant
from advanced_linear_algebra.adjugate import Adjugate
 
 
class Inverse:
    """Calculates the inverse of a matrix"""
 
    @staticmethod
    def calculate(matrix):
        """Returns the inverse of a matrix, or None if singular"""
        if not isinstance(matrix, list):
            raise TypeError("matrix must be a list of lists")
        for row in matrix:
            if not isinstance(row, list):
                raise TypeError("matrix must be a list of lists")
        if len(matrix) == 0:
            raise TypeError("matrix must be a list of lists")
        n = len(matrix)
        if len(matrix[0]) == 0 or any(len(row) != n for row in matrix):
            raise ValueError("matrix must be a non-empty square matrix")
        det = Determinant.calculate(matrix)
        if det == 0:
            return None
        if n == 1:
            return [[1 / matrix[0][0]]]
        adj = Adjugate.calculate(matrix)
        return [[adj[i][j] / det for j in range(n)] for i in range(n)]
