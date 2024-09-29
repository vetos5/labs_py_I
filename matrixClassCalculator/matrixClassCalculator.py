from matrixExceptions import MatrixExceptions
from matrixClass import Matrix


class MatrixCalculator:

    @staticmethod
    def read_matrix(file_path):
        try:
            with open(file_path) as fin:
                data = [list(map(int, line.strip().split())) for line in fin]

            return Matrix(data)

        except FileNotFoundError as e:
            print(f"{MatrixExceptions.FILE_NOT_FOUND_MSG} - {e.filename}")
            exit()

        except ValueError as e:
            print(f"{MatrixExceptions.VALUE_CONVERSION_ERROR_MSG} - {e}")
            exit()

        except Exception as e:
            print(f"{MatrixExceptions.UNEXPECTED_ERROR_MSG} - {e}")
            exit()

    @staticmethod
    def print_matrix(matrix, operation):
        print(f"Result of {operation}:")
        for row in matrix.data:
            print(' '.join(str(element) for element in row))

        with open('result.txt', 'a') as f:
            f.write(f"Result of {operation}:\n")
            for row in matrix.data:
                f.write(' '.join(str(element) for element in row) + '\n')
            f.write('\n')


if __name__ == "__main__":
    with open('result.txt', 'w') as f:
        f.write("Results\n\n")

    matrixA = MatrixCalculator.read_matrix('matrixA.txt')
    matrixB = MatrixCalculator.read_matrix('matrixB.txt')

    matrixC = matrixA.add(matrixB)
    MatrixCalculator.print_matrix(matrixC, "Addition")

    matrixD = matrixA.subtract(matrixB)
    MatrixCalculator.print_matrix(matrixD, "Subtraction")

    matrixE = matrixA.multiply(matrixB)
    MatrixCalculator.print_matrix(matrixE, "Multiplication")