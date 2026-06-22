nums = [1,2,3]

i_nums = iter(nums)
print(i_nums)
print(dir(i_nums))

print(next(i_nums))
print(next(i_nums))
print(next(i_nums))

while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break


class MyRange:
    def __init__(self,start,stop):
        self.value = start
        self.end = stop

#if we want to make our class iterable than
#we must have dunder method
    def  __iter__(self):
        return self
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current
        

values = MyRange(1,10)
# for value in values:
#     print(value)
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))

print(values)
#python have a built in yield thing for this whole mess

def my_range(start,stop):
    current1 = start
    while current1 <stop:
        yield current1
        current1 +=1

muns = my_range(1,10)

print(next(muns))
print(next(muns))
print(next(muns))
print(next(muns))

def fib_gen(n):
    a,b = 0,1
    for n in range(n):
        yield a
        a,b = b,a+b

for num in fib_gen(8):
    print(num, end=" ")