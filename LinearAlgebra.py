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
def matrix_mult(mtrx1: list[list[int]], mtrx2: list[list[int]]) -> list[list[int]]:
    # TODO: Ignoring the checking if the inputs are valid matrix
    if len(mtrx1[0]) != len(mtrx2):
        raise AttributeError
    new_mtrx = []
    new_mtrx2 = transpose(mtrx2)
    for row1 in mtrx1:
        tmp = []
        for row2 in new_mtrx2:
            i = 0
            num = 0
            while i < len(row1):
                num += row1[i] * row2[i]
                i += 1
            tmp.append(num)
        new_mtrx.append(tmp)
    return new_mtrx


def scale_matrix(scaler: int, matrix: list[list[int]]) -> list[list[int]]:
    new_matrix = []
    for row in matrix:
        tmp = []
        for col in row:
            tmp.append(col * scaler)
        new_matrix.append(tmp)
    return new_matrix


def scale_vector(scaler: int, vector: list[int]) -> list[int]:
    new_vect = []
    for i in vector:
        new_vect.append(i * scaler)
    return new_vect


def dot_product(v1: list[int], v2: list[int]) -> int:
    # TODO: Ignore bad inputs lmao
    num = 0
    for i in range(len(v1)):
        num += v1[i] * v2[i]
    return num


def projection(base: list[int], vect: list[int]) -> list[int]:
    dot = dot_product(base, vect)
    mag = magnitude(base)**2
    scale = dot//mag
    return [x * scale for x in base]
    

def magnitude(vector: list[int]) -> int:
    num = 0
    for i in vector:
        num += i**2
    return int(num ** 0.5)


def rref(matrix: list[list[int]]) -> list[list[int]]:
    pass


if __name__ == '__main__':
    print(matrix_mult([[1, 1], [1, 0]], [[13], [8]]))
