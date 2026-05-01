#!/usr/bin/env python3
"""Calculates the inverse of a matrix"""
 
 
def _det(m):
    """Helper determinant (no validation)"""
    n = len(m)
    if n == 1:
        return m[0][0]
    if n == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    det = 0
    for j in range(n):
        sub = [[m[i][k] for k in range(n) if k != j] for i in range(1, n)]
        det += ((-1) ** j) * m[0][j] * _det(sub)
    return det
 
 
def inverse(matrix):
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
    det = _det(matrix)
    if det == 0:
        return None
    if n == 1:
        return [[1 / matrix[0][0]]]
    cofactor = []
    for i in range(n):
        row = []
        for j in range(n):
            sub = [[matrix[r][c] for c in range(n) if c != j]
                   for r in range(n) if r != i]
            row.append(((-1) ** (i + j)) * _det(sub))
        cofactor.append(row)
    adj = [[cofactor[j][i] for j in range(n)] for i in range(n)]
    return [[adj[i][j] / det for j in range(n)] for i in range(n)]
