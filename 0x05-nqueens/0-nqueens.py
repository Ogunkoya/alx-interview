#!/usr/bin/python3

import sys


def is_safe(board, row, col, N):
    # Check if a queen can be placed at board[row][col]

    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check the upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(N):
    board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_util(board, 0, N, solutions)
    return solutions


def solve_util(board, col, N, solutions):
    if col == N:
        # Found a solution, add it to the list
        solution = []
        for row in range(N):
            for i in range(N):
                if board[row][i] == 'Q':
                    solution.append([row, i])
        solutions.append(solution)
        return

    for row in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 'Q'
            solve_util(board, col + 1, N, solutions)
            board[row][col] = '.'


def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(row)
        print()


def main():
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Parse the argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check the value of N
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)


if __name__ == '__main__':
    main()