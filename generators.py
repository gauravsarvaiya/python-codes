# iterator and generator are same


# iter  --> in iter means to convert iterators to use next function to use and call next function
#           l=[1,2,3] --->iterable
#           i=iter(l)  --->iterators
#           print(next(i)) --->next function use to list to end time to print one by one 

# l = [1,2,3,4]
# i = iter(l)
# print(next(i))
# print(next(i))
# print(next(i))
# iterable
# l=[1,2,3,4]
# iterators
# for num in map(lambda a:a**2,l):
#    print(num)                       this map function python define iterators to direct call and create answer

# create first generator with generator function
# 1. generator function
# 2.generator comprehenction
# what is a generator
# ---> generator is a used menory usesbly and then generator to create when demind generator()


# def func(n):
#    for i in range (1,n+1):
#       yield(i)
# number=func(10)
# for i in number:
#     print(i)
# for i in number:
#     print(i)


def func(n):
    for i in range(2,n+1,2):
          yield(i)
for i in func(10):     #genrator function define even number
    print(i)              

# square=(i**2 for i in range (1,11))
# # print(square)                                  generator comprehension in use  closing bracket
#  for i in square:
#     print(i)

# list comprehension ---> this are squnce in use and data insert ,delete
# Generator comprehension ---> this genrator  memory reusebly then mean memory that can not return time to data use then used genrator

import time
# t1=time.time()
# square=[i**2 for i in range (1000000)]      list comprehension
# t2=time.time()-t1
# print(t2)

# t1=time.time()
# square=(i**2 for i in range (1000000))      #genrator comprehension
# t2=time.time()-t1
# print(t2)


def square(n):
    return n**2
print(square(2))



