# A one line statement function

# lambda argument:expression

add100 = lambda x: x + 10

square = lambda x: pow(x, 2)

points2D = [(-2, 7), (1, 8), (14, 8), (-2, 4)]
points2D_sorted = sorted(points2D)

print(points2D_sorted)
print(points2D_sorted)

points2D_sorted = sorted(points2D, key=lambda x: x[1])  # ----->sort by y-axis

# map(function, sequence)

a = [1, 2, 3, 4, 5, 6]
b = map(lambda x: x * 2, a)  #
print(list(b))

c = [x * 2 for x in a]  # -----> by use of list comprehension

print(c)

# filter(function,sequence)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = filter(lambda x: x % 2 == 0, a)
print(list(a))

c_f = [x for x in a if x % 2 == 0]
print(c_f)

# reduce(function, sequence)
from functools import reduce

a = [1, 2, 3, 4, 5, 6]
product_a= reduce(lambda x, y: x * y, a)
print(product_a)
