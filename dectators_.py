def divide(c, d):
    if d == 0:
        c, d = d, c
    return c / d


print(divide(5, 0))

print("-------------------------")


# By using a decorators

def new(func):
    def dec(c, d):
        if b == 0:
            c, d = d, c

    return dec

divide = new(divide)
print(divide(5, 0))

