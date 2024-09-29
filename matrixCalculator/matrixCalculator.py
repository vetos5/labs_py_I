MATRIX_SIZE_MISMATCH_MSG = "Matrix size mismatch"
DIVISION_BY_ZERO_MSG = "Division by zero encountered."
FILE_NOT_FOUND_MSG = "File not found."
VALUE_CONVERSION_ERROR_MSG = "Unable to convert data to float."
UNEXPECTED_ERROR_MSG = "An unexpected error occurred."
MALFORMED_DATA_MSG = "Matrix data is incomplete or incorrectly formatted."
MATRIX_SIZE_ERROR = "Matrix should be 3x3."
MATRIX_DETERMINANT_ERROR_MSG = "Matrix is singular and cannot be inverted."
MATRIX_IS_NONE = "Matrix is empty."


def add(matrix1, matrix2):
    matrix1Rows, matrix1Cols = len(matrix1), len(matrix1[0])
    matrix2Rows, matrix2Cols = len(matrix2), len(matrix2[0])

    if matrix1Rows != matrix2Rows or matrix1Cols != matrix2Cols:
        raise Exception(MATRIX_SIZE_MISMATCH_MSG)

    resultMatrix = [[0 for _ in range(matrix1Cols)] for _ in range(matrix1Rows)]

    for i in range(matrix1Rows):
        for j in range(matrix1Cols):
            resultMatrix[i][j] = matrix1[i][j] + matrix2[i][j]

    return resultMatrix


def multiply(matrix1, matrix2):
    matrix1Rows, matrix1Cols = len(matrix1), len(matrix1[0])
    matrix2Rows, matrix2Cols = len(matrix2), len(matrix2[0])

    if matrix1Cols != matrix2Rows:
        raise Exception(MATRIX_SIZE_MISMATCH_MSG)
        exit()

    resultMatrix = [[0 for _ in range(matrix2Cols)] for _ in range(matrix1Rows)]

    for i in range(matrix1Rows):
        for j in range(matrix2Cols):
            for k in range(matrix1Cols):
                resultMatrix[i][j] += matrix1[i][k] * matrix2[k][j]
    return resultMatrix


def subtract(matrix1, matrix2):
    matrix1Rows, matrix1Cols = len(matrix1), len(matrix1[0])
    matrix2Rows, matrix2Cols = len(matrix2), len(matrix2[0])

    if matrix1Rows != matrix2Rows or matrix1Cols != matrix2Cols:
        raise Exception(MATRIX_SIZE_MISMATCH_MSG)

    resultMatrix = [[0 for _ in range(matrix1Cols)] for _ in range(matrix1Rows)]

    for i in range(matrix1Rows):
        for j in range(matrix1Cols):
            resultMatrix[i][j] = matrix1[i][j] - matrix2[i][j]

    return resultMatrix


def determinant(matrix):
    if len(matrix) != 3 or len(matrix[0]) != 3:
        raise ValueError(MATRIX_SIZE_ERROR)

    if matrix is None:
        raise ValueError(MATRIX_IS_NONE)

    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    det = (a * (e * i - f * h)
           - b * (d * i - f * g)
           + c * (d * h - e * g))

    return det


def inverse(matrix):
    det = determinant(matrix)
    if det == 0:
        raise ValueError(MATRIX_DETERMINANT_ERROR_MSG)

    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    adjugate = [
        [(e * i - f * h), -(b * i - c * h), (b * f - c * e)],
        [-(d * i - f * g), (a * i - c * g), -(a * f - c * d)],
        [(d * h - e * g), -(a * h - b * g), (a * e - b * d)]
    ]

    inverse_matrix = [[element / det for element in row] for row in adjugate]

    return inverse_matrix


def divide(matrix1, matrix2):
    matrix2_inverse = inverse(matrix2)
    return multiply(matrix1, matrix2_inverse)


def read_matrix(file_path):
    try:
        matrix = []
        with open(file_path, 'r') as fin:
            for i in fin:
                row = list(map(int, i.strip().split()))
                matrix.append(row)

        for row in matrix:
            if len(row) != len(matrix[0]):
                print(MALFORMED_DATA_MSG)
                exit()

        return matrix

    except FileNotFoundError as e:
        print(f"{FILE_NOT_FOUND_MSG} - {e.filename}")
        return None

    except ValueError as e:
        print(f"{VALUE_CONVERSION_ERROR_MSG} - {e}")
        return None

    except Exception as e:
        print(f"{UNEXPECTED_ERROR_MSG} - {e}")
        return None


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

    result = '\n'.join(' '.join(map(str, row)) for row in matrix)
    with open('result.txt', 'w') as f:
        f.write(result)


print_matrix(divide(read_matrix('matrixA.txt'), read_matrix('matrixB.txt')))

print('\n')

print_matrix(multiply(read_matrix('matrixA.txt'), read_matrix('matrixB.txt')))

print('\n')

print_matrix(subtract(read_matrix('matrixA.txt'), read_matrix('matrixB.txt')))
