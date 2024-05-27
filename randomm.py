import random

a = random.random()  # ----> random number between 0 and 1

print(a)

b = random.uniform(10, 20)  # ----> random number between (a, b)

print(b)

c = random.randint(0, 10)  # ----.random integer between 0 and 10

print(c)

d = random.normalvariate(0, 1)  # ---->(mean, sigma)

print(d)

e = random.randrange(1, 10)

print(e)

my_list = ['abcdefghijklmnop']
aa = random.choice(my_list)  # ----->returns a random single choice from the list
print(aa)

bb = random.sample(my_list, 5)  # ------>returns a sample of 5 random choices from the list
print(bb)

random.shuffle(my_list)
print(my_list)  # ----.shuffles the list

# ===================SEED==================#

import random

random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))

random.seed(3)
print(random.random())
print(random.randint(1, 10))

random.seed(4)
print(random.random())
print(random.randint(1, 10))

#####same outputs

random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))

random.seed(3)
print(random.random())
print(random.randint(1, 10))

random.seed(4)
print(random.random())
print(random.randint(1, 10))

#############################################################################################################

import secrets
a = secrets.randbelow(10) #---> random integer between 0 and 10...10 excluded
print(a)

b = secrets.randbits(4) #---> returns bite binary number
print(b)

my_list2 = ['ABCDEFGHIJKL']

aaa = secrets.choice(my_list2)
print(aaa)

####################################

import numpy as np

arr = np.random.rand(3) #---. forms a 1D array with 3 elements which are float data type
print(arr)

arr2 = np.random.randint(0, 10, 3) #----> forms a 1D array of  3 integers between 0 and 10
print(arr2)

arr3 = np.random.randint(0, 10, (2,4)) #---> forms a 2 by 4 array of integers between 0 and 10
print(arr3)


######################
ara = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
np.random.shuffle(ara)
print(ara)
##################
np.random.seed(1)
print(np.random.rand(2, 3))
np.random.seed(2)
print(np.random.rand(3, 3))
np.random.seed(3)
print(np.random.rand(4, 3))


np.random.seed(1)
print(np.random.rand(2, 3))
np.random.seed(2)
print(np.random.rand(3, 3))
np.random.seed(3)
print(np.random.rand(4, 3))

##########################################################################