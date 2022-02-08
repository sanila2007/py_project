h = input("Enter the name of the product = ")
l = input("How many stuff are there in that product = ")
m = input("Enter the rate of that product = ")

print("-------------------------------------------")
print("Data of your stock...")


def stock(Name, QTY, Rate):
    print("Item name =", Name)
    print("Quantity = ", QTY)
    print("Rate = ", "Rs.", Rate)


stock(h, l, m)
