# list muteable
# list in symbol [squre braket use]

# number=[1,2,3,4]
# print(number)

# name=["gaurav,,guru"]
# print(name)

# name = ['gaurav','yash']
# print(name)


mixed=[1,2,"gaurav",1,3]
mixed[1:]=["three","four"]
print(mixed)
# 
# name=[]
# name.append("guru")       #append method
# print(name)

# name1=['gaurav','guru']
# name2=['yash','ritik']
# name1.insert(1,'viru')
# print(name1)
# print(name2)
# name1.extend(name2)
# print(name1)

# name1.append(name2)
# print(name1)             #insert,extend,append

# name1=['gaurav','guru','banana','greps','guru']
# name1.pop(0)
# name1.remove('guru')
# del name1[0]             #del,pop,remove
# print(name1)


# name=['gaurav','guru']
# if 'yash' in name:                     (in keyword list)
#     print("yash in present")
# else:
#     print("not a present")


# number=[8,6,8,7,3,1]
# print(number.count(8))

# number.sort()
# print(number)

#print(sorted(number))

# number.clear()
# print(number)
#                                 (count,copy,sort,sorted,clear,)
# number_copy=number.copy()
# print(number_copy)

# num1=[1,2,3,4]
# num2=[1,2,3,4]
# num3=[3,5,7,8]
# print(num1==num3)
# print(num1 is num1)


# name_age='gaurav 20'.split()
# print(name_age)
#                                               (split, join list)
# user_join=['gaurav','20']
# print('_ '.join(user_join))
# print('_ '.join(user_join))

#
# s = "string"
# t=s.title()
# # print(t)                 string is immutable
#
# l=['guru','yash']
# l.append("ritik")
# print(l)                   list is muttable


# name=['gaurav','yash','rohan','akki','ritik']

# for i in name:
#     print(i)                                            list in for loop

# i=0
# while i<len(name):
#     print(name[i])
#     i=i+1


# matrix=[[1,2,3], [4,5,6], [7,8,9]]
# for i in matrix:
#     for j in i:
#         print(j)

# print(matrix[2][1])
# print(matrix[0][2])
#
# s= "string"
# print(type(s))                  type is a cracter define which is type
# print(type(matrix))

# number= list(range(1,11))
# print(number)

# poped=number.pop()
# print(number)

# print(number.index(5))

# number=[1,2,3,4,5,6,7,8,9,10]
# def negative(l):
#     n_1=[]
#     for i in l:
#         print(n_1.append(-i))
#     return n_1
# print(negative(number))

#
# def squre_list(l):
#     number=[]
#     for i in l:
#         number.append(i**2)
#     return number

# def all(l):
#     a = []
#     for i in l :
#         a.append(i**2)
#     print(a)
# num = [1,2,3,4,5]
# print(all(num))

#                                                         exercise
# num=list(range(1,11))
# print(squre_list(num))
#
# def squre_list(num):
#     squre=[]
#     for i in num:
#        squre.append(i**2)
#     return squre
#
# number=list(range(1,11))
# print(squre_list(num))



#
# def reversed_list(l):
#     test=[]
#     for i in l:
#         test.append(reversed(test[::-1]))
#     return test
# num=list(range(1,11))
# print(reversed_list(num)) 



# def number(n):
#        m1=[]
#        for i in range(n+1):
#         # list.append(i)
#         # i+=1
#         m1.append(i)
#         print(m1)
    
        
# print(number(20))       
  

# def number(n) :
#     g1=[]
#     cube=[]
#     for i in range(1,n+1):
#         cube.append(i**3)
#         g1.append(cube)
#     print(g1)
# print(number(3))

# def cube_master(n):
#     cube={}
#     for i in range(1,n+1):
#        cube[i]=i**3
#     return(cube)
# print(type(cube_master(4)))

# def cube(d):
#     d1 = {}
#     for i in range(d):
#         d1[i]= i**3
#     return(d1)
# print(cube(4))


# def cube_list(n):
#     y=[]
#     g=[]
#     for i in range(1,n+1):                    most useful
#        g.append(i)
#        y.append(i**3)
#        print(f"{g}:{y} are cube")
#     return g,y
# print(cube_list(4))


# num = 5
# factorial = 1
# if num < 0:
#     print('sorry, factorial does not exist negative number')
# if num == 0:
#     print('factorial of 0,1')
# else:
# for i in range(1,num + 1):
#     factorial =factorial*i
#     print (factorial)

# num = 5
# factorial = 1
# for i in range (1,num+1):
#    factorial=factorial*i
# print(factorial)

# num = 10
# factorial = 1
# for i in range(1,num+1):
#     factorial = factorial*i
# print(factorial)