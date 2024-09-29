from vectorClass import Vector
from vectorExceptions import VectorExceptions


class VectorCalculator:

    @staticmethod
    def read_vector(file_path):
        try:
            with open(file_path, 'r') as fin:
                data = list(map(int, fin.read().strip().split(',')))

            return Vector(data)

        except FileNotFoundError as e:
            print(f"{VectorExceptions.FILE_NOT_FOUND_MSG} - {e.filename}")
            exit()

        except ValueError as e:
            print(f"{VectorExceptions.VALUE_CONVERSION_ERROR_MSG} - {e}")
            exit()

        except Exception as e:
            print(f"{VectorExceptions.UNEXPECTED_ERROR_MSG} - {e}")
            exit()

    @staticmethod
    def print_vector(self, operation):
        print(f"Result of {operation}:")
        print(' '.join(str(element) for element in self.data))

        with open('vectorResult.txt', 'a') as f:
            f.write(f"Result of {operation}:\n")
            f.write(' '.join(str(element) for element in self.data) + '\n')
            f.write('\n')


if __name__ == "__main__":
    with open('vectorResult.txt', 'w') as f:
        f.write("Results\n\n")

    vectorA = VectorCalculator.read_vector('vectorA.txt')
    vectorB = VectorCalculator.read_vector('vectorB.txt')

    added_vector = vectorA.add(vectorB)
    VectorCalculator.print_vector(added_vector, "Addition")
    subtracted_vector = vectorA.subtract(vectorB)
    VectorCalculator.print_vector(subtracted_vector, "Subtraction")
    dot_product_result = vectorA.dot_product(vectorB)
    print('Dot product result: ', dot_product_result)
    with open('vectorResult.txt', 'a') as f:
        f.write(f"Dot Product: {dot_product_result}\n")


