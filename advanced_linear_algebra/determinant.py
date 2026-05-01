#!/usr/bin/env python3
"""Determinant module"""
 
 
class Determinant:
    """Calculates the determinant of a matrix"""
 
    @staticmethod
    def calculate(matrix):
        """Returns the determinant of a matrix"""
        if not isinstance(matrix, list):
            raise TypeError("matrix must be a list of lists")
        for row in matrix:
            if not isinstance(row, list):
                raise TypeError("matrix must be a list of lists")
        if len(matrix) == 0:
            raise TypeError("matrix must be a list of lists")
        if matrix == [[]]:
            return 1
        n = len(matrix)
        if any(len(row) != n for row in matrix):
            raise ValueError("matrix must be a square matrix")
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        det = 0
        for j in range(n):
            sub = [[matrix[i][k] for k in range(n) if k != j]
                   for i in range(1, n)]
            det += ((-1) ** j) * matrix[0][j] * Determinant.calculate(sub)
        return det
