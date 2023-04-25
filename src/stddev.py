###############################################################################
# Name of the project: ivs project 2
#
###############################################################################
#
# @file stddev.py
# @brief file to calculate sample standard deviation 
#
# @date 25.04.2023
# @author Adam Ďurica, Matúš Hubinský
#
###############################################################################

import os
import sys
import math
import mathlib

directory = os.path.abspath(os.path.dirname(__file__))
files_in_directory = os.listdir(directory)
files_txt = [file for file in files_in_directory if file.endswith('.txt')]

if (len(files_txt) == 1):
    # Read the file name from the list of files in the directory 
    file_name = os.path.abspath(os.path.dirname(__file__)) + "/" + files_txt[0]
elif (len(sys.argv) == 2): 
	# Read the file name from the command line argument
	file_name = sys.argv[1]
else:
    print("Usage: python sample_standard_deviation.py <file_name>")
    exit()

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
