import sys
import math

# Read the file name from the command line argument
if len(sys.argv) != 2:
    print("Usage: python sample_standard_deviation.py <file_name>")
    exit()
file_name = sys.argv[1]

# Read the numbers from the file
with open(file_name, 'r') as f:
    numbers = f.read().split()
    numbers = [float(x) for x in numbers if x != '']

# Check if there are at least 1000 numbers
if len(numbers) < 1000:
    print("Error: The file must contain at least 1000 numbers.")
    exit()

# Calculate the sample mean
mean = sum(numbers) / len(numbers)

# Calculate the sum of squares of differences from the mean
squares = sum([(x - mean) ** 2 for x in numbers])

# Calculate the sample standard deviation
stdev = math.sqrt(squares / (len(numbers) - 1))

print("The sample standard deviation is:", stdev)
