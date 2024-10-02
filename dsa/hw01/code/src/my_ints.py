"""
This code will be used to read files from sample_inputs
then write the numbers in another file making sure no number is repeated
"""
from pathlib import Path

# Defining the base directory as the current directory where the script is running
base_dir = Path(__file__).parent.parent.parent

# Input and output files
input_file = base_dir / "sample_inputs" / "sample_02.txt"
output_file = base_dir / "sample_results" / "results_02.txt"

max_int = 1023
min_int = -1023

# initialise an empty set to ensure uniqueness of the numbers
numbers = set()

# Read the numbers from the input file and add them to the set if they are within the range and not already present
with open(input_file, "r") as f:
    for line in f:
        stripped_line = line.strip()
        if stripped_line:
            try:
                number = int(stripped_line)  # Try converting to int
            except ValueError:
                number = float(stripped_line)
        if max_int >= number >= min_int and number not in numbers:
            numbers.add(number)

# Write the unique numbers to the output file in ascending order
with open(output_file, "w") as f:
    for number in sorted(numbers):
        f.write(f"{number}\n")
