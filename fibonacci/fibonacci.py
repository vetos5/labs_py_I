def fibonacci(first_num, second_num, steps, border, result=None):
    if result is None:
        result = [first_num, second_num]
    if len(result) >= steps or (result[-1] + result[-2] > border):
        return result[:steps]

    next_value = result[-1] + result[-2]
    if next_value <= border:
        result.append(next_value)

    return fibonacci(first_num, second_num, steps, border, result)


def main():
    try:
        with open('input.txt', 'r') as f:
            input_values = f.read().split(',')
            first_num = float(input_values[0])
            second_num = float(input_values[1])

        with open('steps.txt', 'r') as f:
            steps = int(f.read())

        with open('border.txt', 'r') as f:
            border = float(f.read())

        if steps < 2:
            raise ValueError("Number of steps must be at least 2")

        result = fibonacci(first_num, second_num, steps, border)
        output_str = ', '.join(str(x) for x in result)
        with open('output.txt', 'w') as f:
            f.write(output_str)

    except FileNotFoundError as e:
        print(f"Error: File not found - {e.filename}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
