#Write a program that takes a centigrade temperature and displays the equivalent in fahrenheit. The input should be a number followed by a letter C. The output should be in the same format.

def celsius_fahrenheit(celsius):
    
    return (celsius * 9/5) + 32

def fahrenheit_celsius(fahrenheit):
    
    return (fahrenheit - 32) * 5/9
    
celsius = float(input('Enter temperature in celsius'))
print("Fahrenheit=", celsius_fahrenheit(celsius))

fahrenheit = float(input('Enter temperature in fahrenheit'))
celsius = fahrenheit_celsius(fahrenheit)
print("Celsius=", celsius)


def temp_conversion():
    temp = input("Enter temp value:")

    
    if temp[-1].lower()=="c":
        out = celsius_fahrenheit(float(temp[:-1]))
    elif temp[-1].lower() =="f":
        out = fahrenheit_celsius(float(temp[:-1]))
    else:
        out = "Invalid Input!"
    return out

    
temp_conversion()

def celsius_fahrenheit(celsius):
    return(celsius*9/5)+32
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit-32)*5/9


def temp_conversion():
    temp= input("enter temp value")

    if temp[-1].lower()=="c":
        out = f"{celsius_fahrenheit(float(temp[:-1]))}F"
    elif temp[-1].lower()=="f":
        out = f"{fahrenheit_celsius(float(temp[:-1]))}C"
    else :
        out="invalid input!"
    return out


temp_conversion()