# Authors: Jason Phan
# silly program


# Calculate the determinant
def determinant(matrix: list[list[int]]) -> int:
    if len(matrix) == 0:
        return 0
    if len(matrix) != len(matrix[0]):
        raise AttributeError
    check_len = len(matrix[0])
    for row in matrix:
        if len(row) != check_len:
            raise AttributeError

    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:

        det = 0
        for i in range(len(matrix[0])):
            if matrix[0][i] != 0:
                if (i + 1) % 2 != 0:
                    det += matrix[0][i] * determinant(_matrix_without_cord(matrix, 0, i))
                else:
                    det -= matrix[0][i] * determinant(_matrix_without_cord(matrix, 0, i))
        return det


# Determinant helper
def _matrix_without_cord(matrix: list[list[int]], row: int, col: int) -> list[list[int]]:
    matrix = matrix[:row] + matrix[row + 1:]
    for i in range(len(matrix)):
        matrix[i] = matrix[i][:col] + matrix[i][col + 1:]
    return matrix


# Transposing a matrix
def transpose(matrix: list[list[int]]) -> list[list[int]]:
    if len(matrix[0]) == 0:
        return [[]]
    new_matrix = []
    for i in range(len(matrix[0])):
        tmp_lst = []
        for x in range(len(matrix)):
            tmp_lst.append(matrix[x][i])
        new_matrix.append(tmp_lst)
    return new_matrix


# Matrix multiplication
def matrix_mult(mx1: list[list[int]], mx2: list[list[int]]) -> list[list[int]]:
    pass


def RREF(matrix: list[list[int]]) -> list[list[int]]:
    pass

