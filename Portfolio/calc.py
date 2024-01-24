import sys

op = sys.argv[1]
Values = sys.argv[2:]

def mysum(*nums):
    s = 0
    for i in nums:
        s += i
        return s
    
def myproduct(*nums):
    p = 1
    for i in nums:
        p *= i
    return p
    
if op == "s":
    ans = mysum(Values)
elif op == "p":
    ans = myproduct(Values)
else:
    ans = "Invalid Input!"
    
print(ans)