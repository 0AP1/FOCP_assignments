def average(values):
    """ Calculates the average of the given list. """
    total = 0;
    for n in values:        	# total the given values
        total += float(n)   	 
    return total/len(values)	# return calculated average

# initialisation statement
print("Welcome, utils module has been imported and initialised!")


import my_utils

print("Average is", my_utils.average([10, 23, 30]) )

print("Another average is", my_utils.average([10.2, 8.8, 2.6]) )

# import statement explicitly imports the average() function directly into the program’s symbol table, allowing the prefix to be removed from the later function calls.

from my_utils import average 

print("Average is", average([10, 23, 30]) )

print("Another average is", average([10.2, 8.8, 2.6]) )
