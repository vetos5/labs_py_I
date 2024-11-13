from deque import *


def reverse_file_lines(input_filename, output_filename):

    with open(input_filename, 'r') as infile:
        lines = infile.readlines()

    stack = Deque()
    for line in lines:
        stack.append(line.strip())

    with open(output_filename, 'w') as outfile:
        while len(stack) > 0:
            outfile.write(stack.pop() + '\n')
            