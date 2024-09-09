def fibonacci(input_values, steps):
    if len(input_values) >= steps:
        return input_values
    next_value = input_values[-1] + input_values[-2]
    result = input_values + [next_value]
    return fibonacci(result, steps)


def fibonacci_bordered(input_values, border):

    if len(input_values) < 2:
        return input_values
    result = input_values[-1] + input_values[-2]
    if result > border:
        return input_values
    if result <= border:
        result = input_values + [result]
    return fibonacci_bordered(result, border)


def main():
    try:
        with open('input.txt', 'r') as f:
            input_values = f.read()
            input_values = [float(numbers) for numbers in input_values.split(',')]

        with open('steps.txt', 'r') as f:
            steps = int(f.read())

        with open('border.txt', 'r') as f:
            border = float(f.read())

        if steps < 2:
            raise ValueError("Number of steps must be at least 2")

        result = fibonacci(input_values, steps)
        output_str = ', '.join(str(num) for num in result)
        with open('output.txt', 'w') as f:
            f.write(output_str)
            f.close()

        result_border = fibonacci_bordered(input_values, border)
        output_str_border = ', '.join(str(num) for num in result_border)
        with open('output_bordered.txt', 'w') as f:
            f.write(output_str_border)
            f.close()

    except FileNotFoundError as e:
        print(f"Error: File not found - {e.filename}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
