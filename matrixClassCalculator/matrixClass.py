from dataclasses import dataclass
from matrixExceptions import MatrixExceptions


@dataclass
class Matrix:
    data: list

    def __len__(self):
        return len(self.data), len(self.data[0]) if self.data else 0

    def __getitem__(self, index):
        return self.data[index]

    def add(self, other):
        if not self.data or not other.data:
            print(MatrixExceptions.MALFORMED_DATA_MSG)
            exit(1)

        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            print(MatrixExceptions.MATRIX_SIZE_MISMATCH_MSG)
            exit(1)

        try:
            result_matrix = [
                [self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))]
                for i in range(len(self.data))
            ]
        except IndexError:
            print(MatrixExceptions.UNEXPECTED_ERROR_MSG)
            exit(1)

        return Matrix(result_matrix)

    def subtract(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            print(MatrixExceptions.MATRIX_SIZE_MISMATCH_MSG)
            exit(1)

        result_matrix = [
            [self.data[i][j] - other.data[i][j] for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ]

        return Matrix(result_matrix)

    def multiply(self, other):
        if len(self.data[0]) != len(other.data):
            print(MatrixExceptions.MATRIX_SIZE_MISMATCH_MSG)
            exit(1)

        result_matrix = [
            [sum(self.data[i][k] * other.data[k][j] for k in range(len(self.data[0])))
             for j in range(len(other.data[0]))]
            for i in range(len(self.data))
        ]

        return Matrix(result_matrix)

    def determinant(self):
        if len(self.data) != 3 or len(self.data[0]) != 3:
            print(MatrixExceptions.MATRIX_DETERMINANT_ERROR_MSG)
            exit(1)

        a, b, c = self.data[0]
        d, e, f = self.data[1]
        g, h, i = self.data[2]

        det = (a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g))

        return det

    def inverse(self):
        det = self.determinant()

        if det == 0:
            print(MatrixExceptions.MATRIX_DETERMINANT_ERROR_MSG)
            exit(1)

        a, b, c = self.data[0]
        d, e, f = self.data[1]
        g, h, i = self.data[2]

        adjugate = [
            [(e * i - f * h), -(b * i - c * h), (b * f - c * e)],
            [-(d * i - f * g), (a * i - c * g), -(a * f - c * d)],
            [(d * h - e * g), -(a * h - b * g), (a * e - b * d)]
        ]

        inverse_matrix = [[element / det for element in row] for row in adjugate]

        return Matrix(inverse_matrix)

    def divide(self, other):
        other_inverse = other.inverse()
        return self.multiply(other_inverse)