# We can use loops to do a same statement many times
# Eg: While loop
# Eg: for loop

while (1 < 6):
    print("hello")
# This condition is always tru so this will never end. We need to false that condition to stop that.

# Print hello world for 10 times

x = 0;
while (x < 11):
    print("hello world")
    x = x + 1

# Get five numbers from a user and add them

i=0;
while(i<5):
    y = int(input("Enter a number = "))
    i = i+1
    print("Your entered number is ",y)


print("The addition of your numbers is ", y+y+y+y+y)