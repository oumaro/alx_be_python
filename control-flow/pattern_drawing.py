# This script draws a square pattern of asterisks based on user input.

# Prompt the user to enter a positive integer for the size of the pattern.
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the rows.
row_counter = 0

# Use a while loop to iterate through each row.
while row_counter < size:
    # Use a for loop to print asterisks for the current row.
    for i in range(size):
        print("*", end="")
    
    # Print a newline character to move to the next row.
    print()
    
    # Increment the row counter.
    row_counter += 1
