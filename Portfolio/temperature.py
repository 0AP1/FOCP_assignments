#Write a program that reads 6 temperatures (in the same format as before), and displays the maximum, minimum, and mean of the values. Hint: You should know there are built-in functions for max and min. If you hunt, you might also find one for the mean.

count = 0
store_temp = []
while count<2:
    temp = input("Enter a value:")
    store_temp.append(float(temp[:-1]))
    count = count + 1
max(store_temp)
    
import statistics as s
def values_summary():
    count=0
    store_temp=[]
    while True:
        temp =input("enter temp value:")
        if not temp:
            break
    #or use, if temp=="":
                #break
    
        store_temp.append(float(temp[:-1]))
        count= count+1
    if store_temp:
        maximum= max(store_temp)
        minimum= min(store_temp)
        mean= s.mean(store_temp)
        return maximum, minimum, mean
    return 0,0,0

mx,mn,avg= values_summary()
print(f"the max value:{mx}, min value:{mn}, and avg value:{avg}")
