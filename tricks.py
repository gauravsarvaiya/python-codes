# def cube(l):
#     test={}
#     for i in l:
#        test[i]=i**3        # tricks are dict 1
#     return test
# number=(1,2,3,4)
# print(cube(number))

# def info(l):
#     a = {}        # dict
#     for i in l:
#         a[i]=i**3
#     return a
# number = (1,2,3,4)
# print(info(number))

# def info(l):
#     a = []
#     for i in l:
#         a.append(i**3)   # list
#     return a
# number = [1,2,3,4]
# print(info(number))



# number =(1,2,3,4)
# test={}
# for i in number:               tricks  dict 2
#     test[i]=i**3
# print(test)

# number=(1,2,3,4)
# store={}
# for i in number:
#     store[i]=i**3
# print(store)


# name=("gaurav")
# test={}
# for i in name:                  tricks dict 3 name count
#     test[i]=name.count(i)
# print(test)


# number=(1,2,3,4,5)
# test=[]
# for i in number:                 trick list
#   test.append(i**3)
# print(test)

# number = (1,2,3,4)
# test=[]
# for i in number:
#     test.append(i**2)
#     print(test)

# def func(n):
#    test=[]                         #trick list 2
#    for i in range(1,n+1):
#       test.append(i**2)
#    return test
# print(func(4))


# def func(*args):
#    test=[i**3 for i in args]    list comprehension with args TRICKS
#    return test
# print(func(1,2,3,4))

# def func(L):
#     test=[i**3 for i in L]    
#     return test                    without list comprehension
# number=[1,2,3,4]
# print(func(number))


# def func1(another_func):
#    def func2(*args):
#       print(args)
#       return another_func(*args)
#    return func2
# @func1
# def func3(a,b):                         decorate function must  read and used program
#    return a*b
# print(func3(10,20))

# decorate function main function name to get object create and then run it

# def func1(a,b):
#      return a+b            simple func
# f=func1(10,20)
# print(f)
     
# for loop pachi if lalhi ne print karva thi badha programe ma problem slove thay jase 
# example

# def func(n):
#     for i in range(1,n+1):
#        if i%2==0:
#           print(i)  #----->   simple to print
#           yield(i)     #---->             genrator use and print
# for i in func(10):
#    print(i)  

# def squre(n):
#     return n**2     simply decorator
# s1 = squre(4)
# print(s1)

# def prime(l):
#     a = []
#     for i in l:
#         if i%2!=0:
#            a.append(i)
#     print(a)
# number = (1,2,3,4,5,6)
# print(prime(number))

# i = int(input("enter number"))
# if i%2==0:
#     print(f"{i} this number even")    odd even check
# else:
#     print(f"{i} this number odd")



# def prime(l):
#     a = []
#     for i in l:
#         if i%2 != 0:
#           a.append(i)
#         else:
#             pass            #prime
#     return a
# number = [1,2,3,4,5]
# print(prime(number))

# even = [2,4,6,8,11,12,14]
# odd = 0
# for i in even:
#     if i%2!=0 :
#         odd = i
#         break
#     print(i)
# print(f"odd value is {odd}")


# rows=5
# for i in range(1,rows+1):    # pattern
#     print("* "*i) 

# row=5 
# for i in range(5,row-1):
#     print("* "*i)

# row =5
# for i in range(1,row+1):
#     print("* "*i)

# row =5
# for i in range (1,row+1):
#    print("* "*i)
# class Employee:
#     def __init__(self, name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary =20000
# e1=Employee('gaurav',20,2000)
# print(e1.name)
# print(e1.age)
# print(e1.salary)

# a = lambda x,y: x*y
# print(a(10,20))

# import array as arr
# my_array = arr.array('i',[1,2,3,4,5])
# print(my_array[::-1])

    
# import array as arr
# my_array = arr.array('f',[0.1,2.0,3.0])
# print(my_array[::-1])

# import array as arr
# my_array= arr.array('i',[1,2,3,4,5])
# print(my_array[::-1])

# a = lambda x,y: x*y
# print(a(10,20))


# winning_number=25
# user_number=int(input(" enter this number 1 to 100"))
# if user_number == winning_number:
#     print(' YOU WIN')
# else:
#     if user_number < winning_number:
#         print('take a low')
#     else:
#         print('take a high')   

# for i in range(1,10):
#     print(i)
 
# def deco(a):
#     return a**2
# d=deco(10)
# print(d)             (decorator)

# t1 = (1,2,3,4)
# s1 = list(t1)      tuple convert list
# print(s1)
   

# a = lambda x,y: x+y
# print(a(10,20))          (lamda)

# class Employee:
#     def __init__(self,name,age):
#         self.name=name
#         self.age =age
# e1=Employee('gaurav',20)
# print(e1.name)                   (insrance key word)
# print(e1.age)

# s1={1,2,3,4,5,5,6,7,7,7}     set
# print(s1)

# num=10
# factorial=1
# for i in range(1,num+1):
#     factorial=factorial*i     (factorial)
#     print(factorial)


# number=(1,2,3,4)
# add=[]
# for i in (number):   list in append method
#     add.append(i)
# print(add)


# odd_number=[i for i in range(1,11) if i%2 !=0]
# print(odd_number)

# add=[]
# for i in range(1,11):
#     if i%2 !=0:
#         add.append(i)
# print(add)

# number=(1,2,3,4)
# add={}
# for i in (number):
#     add[i]=i**2
# print(add)


# for fizzbuzz in range(100): 
 
#     # Number divisible by 15,(divisible 
#     # by both 3 & 5), print 'FizzBuzz' 
#     # in place of the number
#     if fizzbuzz % 15 == 0: 
#         print("FizzBuzz")                                         
#         continue
 
#     # Number divisible by 3, print 'Fizz'
#     # in place of the number
#     elif fizzbuzz % 3 == 0:     
#         print("Fizz")                                         
#         continue
 
#     # Number divisible by 5, 
#     # print 'Buzz' in
#     # place of the number
#     elif fizzbuzz % 5 == 0:         
#         print("Buzz")                                     
#         continue
 
#     # Print numbers
#     print(fizzbuzz)

# number=[1,2,3,4,5]
# for i in number:
#     if i%3 == 0:
#         print(f"{i}fizzbuzz

# number=[1,2,3,4,5]
# for i in number:
#     if i%5 == 0:
#         print(f"{i}fizzbuzz")

# for i in range(100):
#     if i % 15 == 0:
#         print("fizzbazz")
#         continue

#     elif i % 3 == 0:
#         print("fizz")
#         continue

#     elif i % 5 == 0:
#         print("buzz")
#         continue

# print(i)

# row =5
# rows= 6
# for i in range(1,row+1):
#     for j in range(1,rows+1):
#         print(" * "*j)


# def triangle(n):
#     k = n-1
#     for i in range(0,n):
#         for j in range(0,k):
#             print(end=" ")
#         k = k-1
#         for j in range(0, i+1):
#             print("*", end="")
#         print("\r")

# n = 5
# triangle(n)

# num = 5
# factorial = 1
# for i in range(1,num+1):
#     factorial = factorial*i
# print(factorial)

# row = 5
# for i in range(0,row):
    # for j in range (0,row-i-1):
    #     print("*", end =" ")
    # print()
    # for j in range (0,i+1):
    #     print("*",end=" ")
    # print()
       


# class A :
#   def __init__(self,firstname,lastname):
#      self.firstname = firstname
#      self.lastname = lastname
  
#   def full_name(self):
#     return f"{self.firstname}  {self.lastname}"

# class B(A):                                       (easy example inheritance)
#   def __init__(self,firstname,lastname,age):
#    super().__init__(firstname,lastname)
#    self.age = age


# new = A('Gaurav','sarvaiya')
# new2 = B('yash','makwana',20)
# print(new.full_name())
# print(new2.full_name())


# num = int(input('enter number'))
# for i in range(0,num):
#     for j in range(0,num-i-1):
#        print(end=" ")
#     for j in range(0,i+1):
#        print(" * ",end=" ")
#     print()


# num = 5
# for i in range(0,num):#(row)
#     for j in range(0,num-i-1):#(col)
#         print("*",end=" ")
#     for j in range(0,i+1):
#         print(end=" ")
#     print() 

# num = int(input("enter number "))
# for i in range(0,num):
#     for j in range (0,num-i-1):           (piramid)
#         print(end=" ")
#     for j in range (0,i+1):
#         print(" * ",end=" ")
#     print()

# row = 5
# for i in range(0,5):
#     for j in range (0,i+1):
#         print("*",end=" ")                 #  one side peramid
#     print()

# row = 5 
# for i in range(0,row):
#     for j in range (0,row-i-0):          down one side peramid
#         print("*",end = " ")
#     print()


row = 5
# for i in range (0,row):
#     for j in range (0,row-i-1):
#         print(end=" ")
#     for j in range (0,i+1):
#         print(" * ",end=" ")
#     print()

# row =5
# for i in range (0,row):
#     for j in range (0,i+1):        (one side )
#         print(" * ",end=" ")
#     print()
#                                         #    (arrow tringle)
# for i in range(0,row):
#     for j in range(0,row-i-0):
#        print(" * ",end =" ")         (down side)
#     print()


# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as err:
#         print(err)
#     # except TypeError as err:                 (error) 
#     #     print(err)
#     except:
#         print("unextepted error")
# print(divide(10,'3'))

# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def sound(self):
#         raise NotImplementedError("create class to sub class")

# class Dog(Animal):
#     def __init__(self, name , breed):
#         super().__init__(name)
#         self.breed = breed

#     def sound(self):
#         print(" dog sound is boowwwwww.....boowwwwww")
    
# class Cat(Animal):
#     def  __init__(self, name,breed):
#         super().__init__(name)
#         self.breed = breed

# d1 = Dog('kuku','lebra')
# c1 = Cat('lulu','bambu')
# print(d1.sound())

        

# row = 5
# for i in range(0,row):
#     for j in range (0,row-i-1):
#         print(end=" ")
#     for j in range(0,i+1):
#         print(" * ",end=" ")
#     print()


# row = 5
# for i in range (0,row):
#     for j in range (0, row-i-0):
#         print(" * ",end = " ")
#     print()


# class intro:
#     def __init__(self,fullname,lastname):
#         self.fullname = fullname
#         self.lastname = lastname
        
#     def full_name(self):
#         return f"{self.fullname} {self.lastname}"

# class A(intro):
#     def __init__(self, fullname, lastname,age):
#         super().__init__(fullname, lastname)
#         self.age = age

#     def full_age(self):
#         return f"{self.full_name()} {self.age}"
#                                                     #    (inheritance)
# class B(intro):
#     def __init__(self, fullname, lastname, age, moblie):
#         super().__init__(fullname, lastname)
#         self.moblie = moblie

# new = A('gaurav','sarvaiya',20)
# new2 = B('yash','makwana',20,91)
# print(new.full_age())

# class Animal:
#     def __init__(self,name):
#        self.name = name

#     def sound(self):
#        raise NotImplementedError ("create class to sub class")

# class dog(Animal):
#     def __init__(self, name,breed):
#        super().__init__(name)
#        self.breed = breed

#     def full_name(self):
#         return f"{self.name} {self.breed}"

# class Cat(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name
# d1 = dog('kuku','labra')
# c1 = Cat('lili','oili')
# print(d1.full_name())

# row =  5
# for i in range (row):
#     for j in range(0,row-i-1):
#         print(end = " ")
#     for j in range(0,i+1):
#         print(" * ",end = "  ")
#     print()

# class intro:
#     def __init__(self,first_name,last_name):
#         self.first_name = first_name
#         self.last_name = last_name
    
#     def fullname(self):
#         return f"{self.first_name}  {self.last_name}"
    
# class A(intro):
#     def __init__(self, first_name, last_name,age):
#         super().__init__(first_name, last_name)
#         self.age = age
    
#     def full_age(self):
#         return f"{self.first_name}{self.age}"

# class B(intro):
#     def __init__(self, first_name, last_name,age,moblie):
#         super().__init__(first_name, last_name)
#         self.mobile = moblie
    
#     def full_moblie(self):
#         return f"{self.first_name}{self.mobile}"

# i1 = intro('gaurav','sarvaiya')
# print(i1.fullname())
# a1 = A('yash','makwana',20)
# print(a1.full_age())
# b1 = B('bhavik','sarvaiya',21,91)
# print(b1.fullname())


# class info:
#     def __init__(self,first_name,last_name):
#         self.first_name = first_name
#         self.last_name = last_name
    
#     def fullname(self):
#         return f"{self.first_name}{self.last_name}"

# class A(info):
#     def __init__(self, first_name, last_name,age):
#         super().__init__(first_name, last_name)
#         self.age = age
   
#     def msg(self):
#         print("inherit main class")

# class B(A):
#     def __init__(self,first_name,last_name,age,mobile):
#         super().__init__(first_name,last_name,age)
#         self.age = age
#         self.mobile = mobile
    
#     def information(self):
#         return f"{self.first_name}{self.mobile}"
# i1=info('gaurav','sarvaiya')
# a1 = A('yash','makwana',20)
# b1 = B('guru','sarvaiya',20,91)
# print(a1.msg())
# print(b1.msg())


# class animal:
#     def __init__(self,name):
#         self.name = name
    
#     def sound(self):
#         return ("all animals sounds are diffrent")
#         # raise NotImplementedError("pls enter define method in subclass")
# class dog(animal):
#     def __init__(self, name,breed):
#         super().__init__(name)
#         self.breed = breed
    
#     def sound(self):
#         return("bhowww...bhowww")

# class cat(animal):
#     def __init__(self, name,breed):
#         super().__init__(name)
#         self.breed = breed
 
#     def sound(self):
#         return("meooo....meoooo")

# d1=dog("dexu","uuuu")
# print(d1.sound())

# def div(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as err:
#         print(err)
#     except TypeError as err:
#         print(err)
#     except:
#         print("unexpected error")
#     finally:
#         print("end....")
# print(div(10,'t'))

# l1 = [1,2,3,4,5]
# s1 = iter(l1)
# print(next(s1))
# print(next(s1))
# print(next(s1))

# x = 'sarvaiya'
# def myfun():
#    global x
#    print(f"gaurav{x}")         global , local
# myfun()
# print(f"yash{x}")


# row = 5
# for i in range (0,row):
#     for j in range (0,row-i-1):
#         print(end =" ")
#     for j in range (0,i+1):

#         print(" * ",end=" ")
#     print()


# def t(n):
#     add = {}
#     for i in n:
#         add[i]=i**2
#     return add
# b1 = (1,2,3,4,5)
# print(t(b1))

# def t(n):
#     add= []
#     for i in n:
#         add.append(i**2)
#     return add
# b1 = [1,2,3,4,5]
# print(t(b1))

# class animal:
#     def __init__(self,name):
#         self.name  = name 
    
#     def sound(self):
#         # return f"all animal sound are diffrent "
#         raise NotImplementedError('pls define crate method in sub class')
    
# class dog(animal):
#     def __init__(self, name,breed):
#         super().__init__(name)
#         self.breed = breed

#     # def sound(self):
#     #     return f" boww...boww"

# class cat(animal):
#     def __init__(self, name,breed):
#         super().__init__(name)
#         self.breed = breed

#     def sound(self):
#         return f" meooo....meoo"
# d1 = dog('brown','munde')
# c1 = cat('kuku','mumu')
# print(d1.sound())
# print(d1.breed)

# def divide(a,b):
#     try:
#         return a/b
#     except TypeError as err:
#         print(err)
#     except ZeroDivisionError as err:
#         print(err)
#     except:
#         print('unexpected error')
#     finally:
#         print('end of program....')
# print(divide(10,2))


# row = 5
# for i in range(0,row):
#     # for j in range(0,row-i-1):
#     #     print(" * ",end =" ")
#     # print()
#     for j in range(0,i+1):
#         print(" * ",end = " ")
#     print()

# class full:
#     def __init__(self,first_name,last_name):
#         self.first_name = first_name
#         self.last_name = last_name
    
#     def full_name_info(self):
#         return f"{self.first_name} {self.last_name}"

# class B(full):
#     def __init__(self, first_name, last_name,age):
#         super().__init__(first_name, last_name)
#         self.age = age 
    
#     def full_info_age(self):
#         return f"{self.first_name} {self.last_name} {self.age}"
    
# class C(full):
#     def __init__(self, first_name, last_name,moblie):
#         super().__init__(first_name, last_name)
#         self.moblie = moblie
    
#     def info_moblie(self):
#         return f"{self.first_name} {self.moblie}"

# b1 = B('gaurav','sarvaiya',20)
# b2 = B('guru','sarvaiya',22)
# print(b1.full_info_age())
# print(b2.full_
# 
# info_age())

# c1 = C('yash','makwana',999999999)
# print(c1.info_moblie())

# for num in range(2,-5,-1):
#     print(num, end =", ")

# i = int(input("enter number"))
# if i % 2!= 0:
#     print(f"{i:}yes!! that's prime number")
# else:
#     print(f"{i:}this is not prime number")


    
