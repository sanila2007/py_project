# We can use continue function to skip some data
# Continue in for loop
for tute in range(1,7):
    if(tute==3):
        continue
    print(tute)


print("-----------------------------------")
# Continue in while loop

a = 0
while(a<10):
    a = a+1
    if (a == 3):
        continue
    print(a)