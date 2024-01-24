# Write a function that has a single string as its parameter, and returns the number of uppercase letters, and the number of lowercase letters in the string. Test the function with a short program

def single_string(string):
    upper_count = lower_count = 0
    for i in string:
        if i.isupper():
            upper_count += 1
        if i.islower():
            lower_count +=1
    return upper_count, lower_count

up, low = single_string("Aanchal")
print("The number of uppercase char is {}, and lowercase char is {}.".format(*single_string("Aanchal")))
