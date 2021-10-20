#loop
from types import TracebackType


for i in range(10):
    print(i)

#iteration function
print(range(0,20,2))

#iteration vs generator->1. default iterator function 2. custom iterator function
#range cara o loop cole bt loop cara range colena
def my_range(endpoint):
    for i in range(endpoint):
        yield i

for i in my_range(10):
    print(i, end="  ")

#yeild=i er value jotokkon porjnto 10 teke boro na hobe totokkon porjnto se value return korte Takbe(iterable)
#return= 1 bar ekta value print kore ber hoa jabe loopteke(iterable na)
#map(func,iter),reduce,filter
#(single single value dore jodi kaj korte cai taile map dorkar)
print('-'*100)
number=lambda x:x
print(number([10,20,30,40,50]))
print(list(map(number,[10,20,30,40,50])))

print('-'*100)
numbers=[10,20,30,40,50]
result=map(lambda x:x,numbers)
print(result)

for i in result:
    print(i, end="")
print()
# reduce sequence follow kore=functions=sum kore protita value kore iterate kore
#reduce sequenceonuja e kaj kore(like series)

#parameter sequence thake
# filter true false return kore

from functools import reduce
print(reduce(lambda x,y:x+y,[10,20,30,40,50]))
print(reduce(lambda x,y:x if x>y else y,[20,30,40,10,50]))
print(reduce(lambda x,y:x if x<y else y,[20,30,40,10,50]))
#filter function
print("--filter--"*10)

def even_number(number):
    if number%2==0:
        return True
    return False

#object showing
print(filter(even_number, [1,2,3,4,5,6,11]))

#even number showing
print(list(filter(even_number, [1,2,3,4,5,6,11])))

#even number showing
res= filter(even_number, [1,2,3,4,5,6,11])
print(list(res))