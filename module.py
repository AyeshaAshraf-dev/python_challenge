from collections import Counter,namedtuple, defaultdict,deque

# user = namedtuple('user', ['name','role','active'], defaults=['Member',True])

# u = user('alice')

# print(u)

#counter is a container that stores element as diictioary keys


# a = "ayaaaeeewwweoiw"

# my_counter = Counter(a)
# # print(my_counter)
# print(my_counter.items())
# print(my_counter.keys())
# print(my_counter.values())
# print(my_counter.most_common(1)[0])
# print(list(my_counter.elements()))

# point = namedtuple('point','x,y')
# #class with field x and y

# pt = point(1,-4)
# print(pt)
# print(pt.x)
# print(pt.y)

d = defaultdict(int)#defaoult value set like float for 0.0
d['a'] = 1
d['b'] = 3
print(d)
print(d['a'])
print(d['c']) #defoult value 0 its benifit


#deque

d = deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3)
d.pop()#remove
print(d)
d.popleft()
print(d)
d.clear()
print(d)
d.extend([5,6,7,8])
print(d)
d.rotate(4)

