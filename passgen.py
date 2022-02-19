import string
import random as ran
#getting lists of characters possiblities
l1 = list(string.ascii_lowercase)
l2 = list(string.ascii_uppercase)
l3 = list(string.punctuation)
l4 = list(string.digits)
#taking user password length
inpt = input("Please enter password length : ")
#validating user input
while True:
    try:
        inpt  = int(inpt)
        if inpt < 6 :
            print("Password length must be 6 or more...")
            inpt = input("Please enter password length : ")
        else:
            break
    except:
        print("Please enter only numbers.")
        inpt = input("Please enter password length : ")
#shuffeling lists
ran.shuffle(l1)
ran.shuffle(l2)
ran.shuffle(l3)
ran.shuffle(l4)

#part length for 30% lower , 30% upper
p1 = round(inpt * (30/100))

#part length for 20% punctuats, 20% digits
p2 = round(inpt * (20/100))

password = []
for i in range(p1):
    password.append(l1[i])
    password.append(l2[i])

for i in range(p2):
    password.append(l3[i])
    password.append(l4[i])

print("".join(password[0:]))