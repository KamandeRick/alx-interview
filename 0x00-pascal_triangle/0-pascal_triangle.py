#!/usr/bin/python3
"""
Program to print a pascals Triangle
"""


def pascal_triangle(n):
    """
    Print pascal triangle f size n
    :parameter n: The number of rows to generate in Pascal's triangle.
    :type n: integer
    :return: List of lists representing Pascal's triangle
    :return type: list
    """

    if n <= 0:
        return[]

    tri = [[1]]

    for i in range(1, n):
        row = [1] + [
                tri[i-1][j] + tri[i-1][j+1]
                for j in range(len(tri[i-1]) - 1)] + [1]
        tri.append(row)

    return tri
