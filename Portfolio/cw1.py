x = 5
y = 1
def yelp(x,y):
    print(x)
    x = 7
    print(x)
    y = x
    print(y)
    return y

a = yelp(x,y)
print(x)
print(y)