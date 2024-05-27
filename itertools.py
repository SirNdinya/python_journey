#    PRODUCT      #

from itertools import product

a = [1, 2]
b = [3, 4]
prod = product(a, b)  # prod = product(a, b, repeat = 2)

print(prod)

#               PERMUTATIONS                #

from itertools import permutations

a = [1, 2, 3, ]
perm = permutations(a)  # perm = permutations(a,2)
print(list(perm))

#               COMBINATIONS                #


from itertools import combinations, combinations_with_replacement

a = [1, 2, 3, 4, 5]
comb = combinations(a, 2)
print(list(comb))

comb_wr = combinations_with_replacement(a, 2)
print(comb_wr)

#               ACCUMULATE          #

from itertools import accumulate
import operator

a = [1, 2, 3, 4, 5]
acc = accumulate(a)
print(list(a))

ap = [1, 2, 3, 4, 5]
accp = accumulate(a, func=operator.mul())

#           GROUPBY    #

from itertools import groupby


def smaller_than_3(x):
    return x < 3


a = [1, 2, 3, 4, 5]

group_obj = groupby(a, key=smaller_than_3)  # ----->group_obj = groupby(a,key=lambda X: X<3)

for key, value in group_obj:
    print(key, list(value))

students = [{'name': 'Tom', 'age': '20'}, {'name': 'Tim', 'age': '16'}, {'name': 'Temi', 'age': '16'},
            {'name': 'Tony', 'age': '17'}, {'name': 'Tam', 'age': '16'},
            {'name': 'Timo', 'age': '20'}, {'name': 'Teny', 'age': '17'},
            {'name': 'Taby', 'age': '23'}, {'name': 'Tady', 'age': '27'}]

group_student = groupby(students, key=lambda x: x['age'])
for key, value in group_student:
    print(key, list(value))

#           INFINITE ITERATORS(COUNT, CYCLE, REPEAT)            #

from itertools import count, cycle, repeat

a = [1, 2, 3]
for i in cycle(a):
    print(i)

a = [1, 2, 3]
for i in repeat(1): #----->for i in repeat(1, 10):---->repeats 1 10 times
    print(i)

for i in count(10):
    print(i)
    if i == 100:
        break  #---->prints numbers from 10 - 100
