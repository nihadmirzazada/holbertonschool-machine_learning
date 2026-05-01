#!/usr/bin/env python3
"""Minor module"""
from advanced_linear_algebra.determinant import Determinant
 
 
class Minor:
    """Calculates the minor matrix of a matrix"""
 
    @staticmethod
    def calculate(matrix):
        """Returns the minor matrix of a matrix"""
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
        if n == 1:
            return [[1]]
        result = []
        for i in range(n):
            row = []
            for j in range(n):
                sub = [[matrix[r][c] for c in range(n) if c != j]
                       for r in range(n) if r != i]
                row.append(Determinant.calculate(sub))
            result.append(row)
        return result
