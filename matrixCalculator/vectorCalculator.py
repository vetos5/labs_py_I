def add(vector1, vector2):
    if len(vector1) != len(vector2):
        raise Exception("Vector size mismatch")

    result = []
    for i in range(len(vector1)):
        result.append(vector1[i] + vector2[i])
    return result


def subtract(vector1, vector2):
    if len(vector1) != len(vector2):
        raise Exception("Vector size mismatch")

    result = []
    for i in range(len(vector1)):
        result.append(vector1[i] - vector2[i])
    return result


def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise Exception("Vector size mismatch")

    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
    return result


def divide(vector1, vector2):
    if len(vector1) != len(vector2):
        raise Exception("Vector size mismatch")

    if any(b == 0 for b in vector2):
        raise Exception("Division by zero encountered.")

    result = []
    for i in range(len(vector1)):
        result.append(vector1[i] / vector2[i])
    return result


def read_vector(file_path):
    try:
        with open(file_path, 'r') as f:
            vector = f.read()
            vector = [float(numbers) for numbers in vector.split(',')]
        return vector
    except FileNotFoundError as e:
        print(f"Error: File not found - {e.filename}")
    except ValueError as e:
        print(f"Error: Unable to convert data to float - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def print_vector(result):
    with open('vector_result', 'w') as file:
        file.write(str(result))


print_vector(dot_product(read_vector('vector1.txt'), read_vector('vector2.txt')))
