# filter

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def even_number(a):
    return a % 2 == 0


y = list(filter(even_number, number))
print(y)

print("---------------------")

# Filter function in lambda

no = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

d = list(filter(lambda x: x % 2 == 0, no))
print(d)

print("--------------------------------")

# Map function

l = list(map(lambda h: h*2, no))
print(l)

# Reduce

from functools import reduce

sum = reduce(lambda n,m: n+m,no)
print(sum)
