#!/usr/bin/env python3
"""Adjugate module"""
from advanced_linear_algebra.cofactor import Cofactor
 
 
class Adjugate:
    """Calculates the adjugate matrix of a matrix"""
 
    @staticmethod
    def calculate(matrix):
        """Returns the adjugate (transpose of cofactor) of a matrix"""
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
        cof = Cofactor.calculate(matrix)
        return [[cof[j][i] for j in range(n)] for i in range(n)]
