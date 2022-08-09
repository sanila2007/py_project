x = [1, 2, 3, 4, 5, 6]
print(5 in x)  # 5 is in the x variable so this condition is true

# Access to a tuple using for loop

for num in x:
    print(num)  # we can access to a tuple using for loop too.

print("----------------------------------------")

# Access to a dictionary using for loop

dic = {"Name": "Sanila",
       "Age": 14,
       "Roll": "Student",
       "Gender": "Male"}

for about in dic.keys():
    print(about)  # This only prints the keys of this dictionary.If we want to access to values, we can use
    # dic.values():

print("----------------------------------------")

for about, description in dic.items():
    print(dic)  # This prints all items

print("----------------------------------------")

# Range functions in For loop
# Print 1 to 5 numbers using a range

i = 1, 2, 3, 4, 5, 6, 7, 8

for i in range(1, 6):
    print(i)

# Range

y = 50,60,70,80,90,100

for y in range(50, 90):
    print(y)

print("----------------------------------------")

c = ["Sanila","Male",14,"student"]

for h in c:
    print(h)

   
print("---------------------------------------")

