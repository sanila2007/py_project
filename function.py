# We use def to show that we are gonna create a function

def addition(number1, number2, number3):
    return number1 + number2 + number3


print(addition(10, 15, 40))

print("---------------------------------------")


def square(length, width):
    perimeter = 2 * (length + width)
    area = length * width
    print("Perimeter of your square is = ", perimeter,"cm")
    print("Area of your square is = ", area,"cm")


square(10, 15)
