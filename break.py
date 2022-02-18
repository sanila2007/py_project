# Break in while loop
one = 0
while (one < 6):
    one = one + 1
    if (one == 2):
        break
    print(one)

print("--------------------------------------------------")

# Break in for loop

yes = 1, 2, 3, 4, 5, 6
for yes in range(1, 6):
    if (yes == 5):
        break
    print(yes)

print("--------------------------------------------------")

hello = 10, 20, 30, 40, 50, 60

for hello in range(10, 60):
    if (hello == 40):
        break
    print(hello)

print("----------------------------------------------------")

guy = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13

for guy in range(1, 11):
    if (guy == 8):
        break
    print(guy)

print("--------------------------------------------------")

name = 90, 1000, 10, 900, 40, 80, 66

for name in range(1, 1000):
    if (name == 560):
        break
    print(name)
