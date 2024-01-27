# Import the sys module
import sys

# Get the number of arguments
count = len(sys.argv)

# Check if no arguments were provided
if count == 1:
    print("No arguments were provided")
else:
    # Calculate the total
    total = 0
    for i in range(1, count):
        total += float(sys.argv[i])

    # Calculate the average
    average = total / (count - 1)

    # Print the total and average
    print("Total is", total)
    print("Average is", average)
