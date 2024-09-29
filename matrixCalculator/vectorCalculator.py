VECTOR_SIZE_MISMATCH_MSG = "Vector size mismatch"
DIVISION_BY_ZERO_MSG = "Division by zero encountered."
FILE_NOT_FOUND_MSG = "File not found."
VALUE_CONVERSION_ERROR_MSG = "Unable to convert data to float."
UNEXPECTED_ERROR_MSG = "An unexpected error occurred."
MALFORMED_DATA_MSG = "Vector data is incomplete or incorrectly formatted."


def add(vectorA, vectorB):
    if len(vectorA) != len(vectorB):
        raise Exception(VECTOR_SIZE_MISMATCH_MSG)

    result = []
    for i in range(len(vectorA)):
        result.append(vectorA[i] + vectorB[i])
    return result


def subtract(vectorA, vectorB):
    if len(vectorA) != len(vectorB):
        raise Exception(VECTOR_SIZE_MISMATCH_MSG)

    result = []
    for i in range(len(vectorA)):
        result.append(vectorA[i] - vectorB[i])
    return result


def dot_product(vectorA, vectorB):
    if len(vectorA) != len(vectorB):
        raise Exception(VECTOR_SIZE_MISMATCH_MSG)

    result = 0
    for i in range(len(vectorA)):
        result += vectorA[i] * vectorB[i]
    return result


def divide(vectorA, vectorB):
    if len(vectorA) != len(vectorB):
        raise Exception(VECTOR_SIZE_MISMATCH_MSG)

    if any(b == 0 for b in vectorB):
        raise Exception(DIVISION_BY_ZERO_MSG)

    result = []
    for i in range(len(vectorA)):
        result.append(vectorA[i] / vectorB[i])
    return result


def read_vector(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()

        if not content:
            raise ValueError(FILE_NOT_FOUND_MSG)

        items = content.split(',')
        vector = []
        for item in items:
            item = item.strip()
            if not item.isdigit():
                raise Exception(VALUE_CONVERSION_ERROR_MSG)

            vector.append(int(item))

        return vector

    except FileNotFoundError as e:
        print(f"{FILE_NOT_FOUND_MSG} - {e.filename}")
        exit()
    except ValueError as e:
        print(f"{VALUE_CONVERSION_ERROR_MSG} - {e}")
        exit()
    except Exception as e:
        print(f"{UNEXPECTED_ERROR_MSG} - {e}")
        exit()


def print_vector(result):
    with open('vector_result', 'w') as file:
        file.write(str(result))


print_vector(dot_product(read_vector('vectorA.txt'), read_vector('vectorB.txt')))
