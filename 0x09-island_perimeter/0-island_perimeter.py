#!/usr/bin/python3
"""
Module to find the perimeter of an island
"""


def island_perimeter(grid):
    """
      Function to calculate the perimeter of an island on a grid.
    Args:
        grid (List[List[int]]): Rectangular grid where 0 is water
                               and 1 is land on the island
    Returns:
        int: perimeter of the islnd
    """

    if not grid:
        return 0

    rows = len(grid)
    columns = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if j == columns-1 or grid[i][j+1] == 0:
                    perimeter += 1
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1

    return perimeter
