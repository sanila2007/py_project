area = lambda a: a * a

print(area(5))

print("-----------------------")

area_2 = lambda c, d: c * d

print(area_2(10, 5))

print("---------------------------")


def apple(price):
    return lambda no_of_apples: price * no_of_apples


x = apple(40)
print(x(8))

print("------------------------------")


def orange(price):
    return lambda no_of_orange: no_of_orange * price


b = orange(40)
print(b(10))
