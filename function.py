# a=int(input("enter number"))
# b=int(input("enter number"))
# total=a+b
# print(total)

# def user_number(a,b):
#     return (a+b)
# print(user_number(10,2))

# first_name=input("enter first name  ")
# last_name= input("enter last name")
# total=first_name+last_name
# print(total)

# def user_namber(a,b,c):
#     return (a+b+c)
# print(user_namber(5,5,5))

# def last_name(name):
#     return name[-1]
# print(last_name("gaurav"))

# def odd_even(number):
#     if number%2 == 0:
#          return "even"
#
#
#     return "odd"
# print(odd_even(5))


# def is_even(number): #bhracets in this pramiter
#     return number%2 == 0        (must helpfl)
# print(is_even(8))  # in bracets in this argument


# def song():
#     return ("happy birthday")
# print(song())

# def big_small(number):
#     if number < 10:
#         return ("small number")
#
#
#     return ("big number")
# print(big_small(7))


# def big_small(a,b):
#      if a > b:
#          return a
#      return b
#
# num_1=int(input("enter number"))
# num_2=int(input("enter number"))
# bigger= big_small(num_1,num_2)
# print(f"{bigger}is greater")


# def user_num(number):
#     if number%2==0:
#        print(f"{number}is event ")
#     else:
#      print(f"{number}is odd ")
# enrollment=int(input("pls number"))
# total=user_num(enrollment)



# def greater(a,b):
#     if a>b:
#         return a
#     return b
#
# def user_num(a,b,c):
#      if a>b and a>c:
#          return a
#      elif b>a and b>c:
#          return b
#      else:
#          return c
# def new_one (a,b,c):
#     # bigger=greater(a,b)
#     return greater(greater(a,b),c)
# print(new_one(10,20,30))

# def new_num(number):
#     if number%2==0:
#         print(True)
#     else:
#         print(False)
#
#
# print(new_num(10))
#
def plindrome(name):
    reversed=name[::-1]
    if name==reversed:
        return True
    else:
        return False
# def plindrome(name):
#     if name==name[::-1]:
#         return True
#     return False
# def plindrome(name):
#     return name==name[::-1]
# print(plindrome("gaurav"))
# print(plindrome("naman"))

# def pli(name):
#     if name == name[::-1]:
#         return True
#     return False
# print(pli('naman'))

def febonacci(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a, b)
    else:
        print(a ,b,end=" ")
    for i in range(n-2):
         c=a+b
         a=b
         b=c
         print(b,end=" ")
(febonacci(10))


# def factorial(num):
#     fac = 1
#     for i in range (1,num+1):
#         fac = fac*i
#     print(fac)
# print(factorial(5))




# def user_name(first_name,last_name='unkown',age= None):
#     print(f"first name is {first_name}")
#     print(f"last name is {last_name}")
#     print(f"your age {age}")
#                                                       (defult prameter)
# user_name("gaurav")


# x=7     #global scope
# def func():
#     global x
#     x=5   # local scope
#     return x
# print(x)
# print(func())
# print (x)


# x=1
# def fun1():
#     x=5
#     def fun2():
#         global x
#         x=7
#         def fun3():
#             x=9
#     fun2()
# fun1()
# print(x)
# x=1
# def fun1():
# #    global x
#    x=5
#    print(x)
# fun1()
# print(x)

# x=1
# def fun1():
#    global x
#    x=2
#    print(x)
#    def fun2():
#        global x
#        x=3
#        def fun3():        
#             x=5
#        fun3()     
#    fun2()   
# fun1()
# print(x)

# a1 = int(input("enter number"))
# def factorial():
#     fac = 1
#     for i in range(1,a1+1):
#         fac = fac*i
#     return fac
# print(factorial())


num =10
factorial = 1
for i in range(1,num+1):
    factorial = factorial+i
print(factorial)
