# enumerate function our string ,list elc postion can be serch and use it.
# enumerate postion tracking
# enumerate are use when will take list , string etc in before use enumerate fuction then after get listname,strig name etc
# name=['abc','gdv','gaurav']
# pos=0
# for i in name:
#     print(f"{pos} --> {i}")
#     pos+=1

# for pos,i in enumerate(names):
#     print(f"{pos}-->{i}")         enumerate

# def find_1(l,target):
#     for pos,i in enumerate (l):
#         if i==target:
#             return pos
#     return -1
# print(find_1(l,'gaurav'))



# map function
# map function use to direct function and varaible in map function used automatic in run this logic

# example
# number=(1,2,3,4)
# def func(a):
#     return a**2                          #map function use
# h1=list(map(func,number))
# print(h1)

# s1=list(map(lambda a: a**2,number))
# print(s1)                                   #map fuction in lambda function use

# sqaure=[i**2 for i in number]          #list comprehension
# print(sqaure)

# number =[1,2,3,4]
# s1=list(map(lambda a: a**2,number))
# print(s1)

# l=[]
# for i in number:
#     l.append(i**2)                      simple program in sqaure
# print(l)



# **filter function
# def func(a):
#    return a%2==0
# number=[1,2,3,4,5,6]
# f1=tuple(filter(func,number))     #simple filter function used
# print(f1)

# number=(1,2,4,5,6,7,8,9,8,66)
# h1=list(filter(lambda a: a%2==0,number))
# print(h1)                                   filter in lambda function use

# h1=[i for i in number if i%2==0]
# print(set(h1))



# iterator & iterables diffrent between
# number=[1,2,3,4]     #--->iterables
# sqaure=map(lambda a: a**2,number)#---->iterator

# for i in sqaure:
#     print(i)
# j1=iter(number)
# print(next(iter(sqaure)))
# print(next(iter(sqaure)))
# print(next(iter(number)))
# print(next(iter(sqaure)))
# # print(next(iter(sqaure)))
# print(next(iter(j1)))
# print(next(iter(j1)))
# print(next(iter(j1)))

# simple things that are you direct to do iter(number) and then you 
# (print(next(iter(number)))) only for 1 number can fecth okay!!
# but when you iter(number) to store in vairable can do and then used 
# in print in enter the create varaible store and then value can be fetch 
# 1 by 1 okay


# # zip function
# zip function use to relation can combain 
# users=['user1','user2','user3']
# name=['gaurav','guru','mansi']
# print(list(zip(users,name)))

# l1=[1,3,5,7]
# l2=[2,4,6,8]
# new_list=[]                       zip function
# for pair in zip(l1,l2):
#    new_list.append(max(l1,l2))
# print(new_list)


# EXERCISE
# output:-[1,2,3],[2,3,4]-->[1+2]/2,all are calculate

# def jeery(l1,l2):
#      avrage=[]
#      for pair in zip(l1,l2):
#         avrage.append(sum(pair)/len(pair))   programe to other lies use
#      return avrage
# print(jeery())


# avrage_list=lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
# print(avrage_list([1,2,3],[1,2,3],[2,3,4]))                             lambda ,zip sunc usedin its


# ****any, all function****

# number1=[2,4,9,8]   #---> in odd number add-->all function use--->false
# number2=[1,3,4,7]   #---> in even number add-->any function use--->true
# print(all([num%2==0 for num in number1])) #list in a number not even all list are false
# print(any([num%2==0 for num in number2])) #list in a number even all list are true!!

# practice
# def func(*args):
    
#    if all([(type(arg) == int or type(arg) == float) for arg in args]):
#       total=0
#       for num in args:
#           total += num
#       return total
#    else:
#       return "worng input"
# print(func(1,3,4,5.4,3))

# min , max function practice
# name=['gaurav','guru','dhaiwat']
# print(min(name, key=lambda item:len(item)))
# print(max(name, key=lambda item:len(item)))

# student={
#     'guru':{'score':90,'age':18},
#     'meet':{'score':70,'age':19},
#     'jeery':{'score':60,'age':15}
# }                                                   
# print(max(student,key=lambda item :student[item]['age']))
# print(min(student,key=lambda item :student[item]['age']))

# student=[
#     {'name':'guru','score':90,'age':18},
#     {'name':'meet','score':70,'age':19},
#     {'name':'jeery','score':60,'age':15}
# ]
# print(max(student,key= lambda item: item.get('score'))['name'])

# SHORT METHOD***********

# fruits=['apple','grayps','banana']
# fruits.sort()                     simple sorted 
# print(fruits)

# fruits=('apple','grayps','banana')
# print(sorted(fruits))                 tuple shorted

# fruits={'apple','grayps','banana'}
# print(sorted(fruits))

# student=[
#    {'name':'guarav', 'marks':70},
#    {'name':'mohit' ,'marks':80},
#    {'name':'harsh', 'marks':60}           dictnory
# ]
# print(sorted(student,key=lambda d:d['name']))


# DOC******
# doc function a got massege there use in programe(len ,sum,)
# a=input()
# b=input()

# a=int(input(''))
# b=int(input(''))
# sum(a,b)
# print(sum.__doc__)
# print(len.__doc__)
print(help(sum))
# help(sum)
# print(help)

# def add(a,b):
#    return a+5,b+5
# result=add(3,2)
# print(result)





