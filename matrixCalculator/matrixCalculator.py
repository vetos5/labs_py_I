def add(matrix1, matrix2):
    matrix1Rows, matrix1Cols = len(matrix1), len(matrix1[0])
    matrix2Rows, matrix2Cols = len(matrix2), len(matrix2[0])

    if matrix1Rows != matrix2Rows or matrix1Cols != matrix2Cols:
        raise Exception("Matrix size mismatch")

    resultMatrix = [[0 for _ in range(matrix1Cols)] for _ in range(matrix1Rows)]

    for i in range(matrix1Rows):
        for j in range(matrix1Cols):
            resultMatrix[i][j] = matrix1[i][j] + matrix2[i][j]

    return resultMatrix


def multiply(matrix1, matrix2):
    matrix1Rows, matrix1Cols = len(matrix1), len(matrix1[0])
    matrix2Rows, matrix2Cols = len(matrix2), len(matrix2[0])

    if matrix1Rows != matrix2Rows:
        raise Exception("Matrix size mismatch")

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
        raise Exception("Matrix size mismatch")

    resultMatrix = [[0 for _ in range(matrix1Cols)] for _ in range(matrix1Rows)]

    for i in range(matrix1Rows):
        for j in range(matrix1Cols):
            resultMatrix[i][j] = matrix1[i][j] - matrix2[i][j]

    return resultMatrix


def determinant(matrix):
    if len(matrix) != 3 or len(matrix[0]) != 3:
        raise ValueError("Matrix must be 3x3")

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
        raise ValueError("Matrix is singular and cannot be inverted")

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
        with open(file_path, 'r') as file:
            lines = file.readlines()
            matrix = [list(map(float, line.split())) for line in lines]
        return matrix
    except FileNotFoundError as e:
        print(f"Error: File not found - {e.filename}")
    except ValueError as e:
        print(f"Error: Unable to convert data to float - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

    result = '\n'.join(' '.join(map(str, row)) for row in matrix)
    with open('result.txt', 'w') as f:
        f.write(result)


print_matrix(divide(read_matrix('matrixA.txt'), read_matrix('matrixB.txt')))

print('\n')

print_matrix(multiply(read_matrix('matrixA.txt'), read_matrix('matrixB.txt')))
