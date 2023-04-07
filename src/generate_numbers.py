import os
import random

# Get the directory path of the Python script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Generate 1000 random numbers
random_numbers = [random.randint(1, 10000) for i in range(1010)]

# Open file for writing in the same directory as the script
with open(os.path.join(script_dir, "numbers_for_profiling.txt"), "w") as f:
    # Write each number to file separated by a space
    for num in random_numbers:
        f.write(str(num) + " "+"\n")
