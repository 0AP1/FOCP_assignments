upper = lower = special = num = False
char_lst = ['@','#','!']
num_lst = '0,1,2,3,4,5,6,7,8,9'
while True:
    pw = input("Enter password")
    if pw in BAD_PASSWORDS:
        print("Sorry very weak password, try again!")
        continue

    if 8 <= len(pw) >=8 and len(pw) <=16:
        for i in pw:
            if i.isupper():
                upper = True
            if i.islower():
                lower = True
            if i in char_lst:
                special = True
            if i in num_lst:
                num = True
        if upper and lower and special and num:
            print("Succesfully registerd.")
            break
        else:
           print("PW doesnot meet criteria.")
    else:
        print("Check password length!")
