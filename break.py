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
