

# tuple is a unmutable
# tuple is a data stracture

# number=(1,2,3,4,5.0)
# print(type(number))
# print(min(number))
# print(max(number))
# print(sum(number)) 


# name= 'gaurav','yash','guru'
# print(type(name))

# name=('gaurav',['yash','guru'])
# print(type(name))
# name[1].pop()
# print(name)
# name[1].append('harsh')
# print(name)


# def func(int1,int2):
#          add=int1 + int2
#          multiply=int1 * int2                        #  two return value in tuple
#         return add, multiply
# # print(func(2,3))
# add,multiply=func(2,3)
# print(add)
# print(multiply)

l = [1,2,3,4,5]
t = (1,2,3,4,5)

b = ('guru','yash')
l[2]=b
print(l)

# add = list(t)
# add.append(6)
# t = tuple(add)
# print(t)

add= list(t)
add.append(2)
t = tuple(add)
print(t)

