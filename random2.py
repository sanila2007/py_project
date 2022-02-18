import random

lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
symbol = "!@#$%^&*({}"
number = "123456789"

all = lower + upper + symbol + number
length = 8

password = "".join(random.sample(all, length))
password2 = "".join(random.sample(all, length))

print("Generated password is ", password,"\n\n ")

f = input("Do you like this password? tell yes or no = ")

if f == "no":
    print("Try this", password)
else:
    print("Nice to hear that!")

