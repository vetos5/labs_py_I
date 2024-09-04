def fibonacci(a, b, n, result=None):
    if result is None:
        result = [a, b]
    if len(result) == n:
        return result
    result.append(result[-1] + result[-2])
    return fibonacci(a, b, n, result)


def main():
    try:
        with open('input.txt', 'r') as f:
            input_values = f.read().split(',')
            a = int(input_values[0])
            b = int(input_values[1])

        with open('steps.txt', 'r') as f:
            n = int(f.read())

        if n < 2:
            raise ValueError("Number of steps must be at least 2")

        result = fibonacci(a, b, n)
        output_str = ', '.join(str(x) for x in result)
        with open('output.txt', 'w') as f:
            f.write(output_str)

    except FileNotFoundError as e:
        print(f"Error: File not found - {e.filename}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
