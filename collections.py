#       COUNTER    #

from collections import Counter

a = "aaaaggggjkkiiejhnbbbbbddddddccccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.keys)
print(my_counter.values)
print(my_counter.most_common(1))


#       NAMEDTUPLE    #


from collections import namedtuple

Point = namedtuple('Point', 'x, y')
pt = Point(2, 8)
print(pt)


#           ORDEREDDICT      #


from collections import  OrderedDict

ordered_dict = OrderedDict()    # ordered_dict = {}
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

print(ordered_dict)



#           DEFAULTDICT    #


from collections import defaultdict

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

print(d)

print(d['a'])

print(d['f']) # returns default integer value that is a zero...since the default defined type is integer



#       DEQUE               #

from collections import deque

d = deque()
d.appednd(1)
d.appednd(2)
d.appednd(3)
d.appednd(4)
d.appednd(5)

print(d)

d.appendleft(10)
d.appendleft(20)

print(d)
d.pop()

d.popleft()


d.extend([100,200,300,400])

d.extendleft([1000,2000,3000,4000])

d.rotate(1)
d.rotate(2)

d.rotate(-1)
d.rotate(-2)

print(d)


d.clear()