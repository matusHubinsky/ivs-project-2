###############################################################################
# Name of the project: ivs project 2
#
###############################################################################
#
# @file stddev.py
# @brief file to calculate sample standard deviation 
#
# @date 08.04.2023
# @author Adam Ďurica
#
###############################################################################

import sys
import math
import mathlib

# Read the file name from the command line argument
if len(sys.argv) != 2:
    print("Usage: python sample_standard_deviation.py <file_name>")
    exit()
file_name = sys.argv[1]

# Read the numbers from the file
with open(file_name, 'r') as f:
    numbers = f.read().split()
    numbers = [float(x) for x in numbers if x != '']

# @brief calculates sum of all numbers in text file
# @param result, number
# @return result sum of all numbers in text file
def summary(numbers):
    result = 0
    for number in numbers:
        result = mathlib.add(None, result, number)
    return result

# Calculate the sample mean
mean = summary(numbers) / len(numbers)

# Calculate the sum of squares of differences from the mean
squares = 0
for number in numbers:
    squares = mathlib.add(None, squares, (number - mean) ** 2)

# Calculate the sample standard deviation
stddev = mathlib.root(None, mathlib.div(None, squares, len(numbers) - 1), 2)

# Print the result of the sample standard deviation
print(stddev)
