#!/usr/bin/python3
"""
This module contains the island_perimeter function.
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.

    Args:
        grid (List[List[int]]): The grid representing the island.

    Returns:
        int: The perimeter of the island.

    Raises:
        ValueError: If the grid is empty or not rectangular.

    Examples:
        >>> grid = [
        ...     [0, 0, 0, 0, 0, 0],
        ...     [0, 1, 0, 0, 0, 0],
        ...     [0, 1, 0, 0, 0, 0],
        ...     [0, 1, 1, 1, 0, 0],
        ...     [0, 0, 0, 0, 0, 0]
        ... ]
        >>> island_perimeter(grid)
        12
    """
    if not grid or not all(len(row) == len(grid[0]) for row in grid):
        raise ValueError("Invalid grid")

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter