#Write and test a function that converts a temperature measured in degrees centigrade into the equivalent in fahrenheit, and another that does the reverse conversion. Test both functions. (Google will find you the formulae).

def celsius_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
    
celsius = 25
fahrenheit = celsius_fahrenheit(celsius)
print("Fahrenheit=", fahrenheit)

fahrenheit = 79
celsius = fahrenheit_celsius(fahrenheit)
print("Celsius=",celsius)