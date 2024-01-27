# Get user input as a string
number = input("Enter a number: ")

# Convert input string to integer  
number = int(number)

# Print back number entered  
print("The number entered was", number)

# Check if remainder of number divided by 2 is 0
# If so it is an even number, otherwise odd number
if (number % 2) == 0:
  print("That is an even number") 
else:
  print("That is an odd number")

# Add code to check if number is divisible by 10
if (number % 10) == 0:
  print("The number is divisible by 10")