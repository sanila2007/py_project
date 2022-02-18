def addition(number1, number2, number3):
    return number1 + number2 + number3


print(addition(10, 15, 40))

print("---------------------------------------")


def square(length, width):
    perimeter = 2 * (length + width)
    area = length * width
    print("Perimeter of your square is = ", perimeter, "cm")
    print("Area of your square is = ", area, "cm")


square(10, 15)

print("----------------------------")

baage = 0.5
hh = int(input("h = "))
aa = int(input("a = "))


def triangle(half, h, a):
    area = half * h * a
    print("Area of your triangle is", area,"cm")


triangle(baage, hh, aa)
