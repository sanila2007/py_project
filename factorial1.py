result = 1

for i in range(1, 5):
    result = result * i

print(result)

print("-----------------------------")

b = int(input("Enter number = "))

for a in range(1, b):
    b = b * a

print(b)

print("------------------------------")

c = int(input("your number = "))

for d in range(1, c):
    c = c * d

print(c)

print("----------------------------")


def factorial_test(n):
    if n == 0:
        return 1
    else:
        return n * factorial_test(n - 1)


print(factorial_test(4))

print("----------------------------")

h = int(input("Enter number = "))


def fact(n_):
    if n_ == 0:
        return 1
    else:
        return n_ * fact(n_ - 1)


print(fact(h))
