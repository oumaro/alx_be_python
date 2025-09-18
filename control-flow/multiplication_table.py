# This script generates a multiplication table for a given number.

# Prompt the user to enter a number and store it as an integer.
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to iterate from 1 to 10.
for i in range(1, 11):
    # Calculate the product of the user's number and the current number in the loop.
    product = number * i
    
    # Print the multiplication table line in the specified format.
    print(f"{number} * {i} = {product}")
