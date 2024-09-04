# Fibonacci Sequence 

This project implements a Fibonacci sequence generator based on an initial pair of numbers and a specified number of steps. 

## Overview

The Fibonacci sequence is a series where each number is the sum of the two preceding ones. For this project, the sequence starts with two numbers provided in an `input.txt` file. The number of steps to generate in the sequence is specified in a `steps.txt` file.

## Files

1. **input.txt**: This file contains two numbers separated by a comma. These numbers are the first two numbers of the sequence.

    Example:
    ```
    7,12
    ```

2. **steps.txt**: This file contains a single number that specifies how many numbers in total should be generated in the sequence.

    Example:
    ```
    5
    ```

3. **output.txt**: This file will contain the generated Fibonacci sequence up to the specified number of steps.

## How It Works

1. Read the initial two numbers from `input.txt`.
2. Read the number of steps from `steps.txt`.
3. Generate the Fibonacci sequence starting from the initial two numbers and continuing until the desired number of steps is reached.
4. Write the resulting sequence to `output.txt`.

## Example

Given the following files:

- `input.txt`:
    ```
    7,12
    ```

- `steps.txt`:
    ```
    5
    ```

The output in `output.txt` will be:

`7,12,19,31,50`


## Usage

1. Ensure that `input.txt` and `steps.txt` are correctly created with the appropriate content.
2. Run the program.
3. Check `output.txt` for the result.

