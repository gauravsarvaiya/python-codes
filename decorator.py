
# decorators in use best learn program undersatding
# enhance the functionally of other function

# def square(a):
#     return a**2
# s=square(10)      simple program decorator
# print(s)

def squre(a):
    return a**2
s1 = squre(2)
print(s1)

 
# l=[1,2,3,4]
# def new_map(func,l):
#    h1=[]
#    for item in l:
#        h1.append(func(item))         
#    return h1
# print(new_map(lambda a:a**3,l))


# def map_2(func ,l):          function as argumrnt
#     # return[func(item) for item in l]    decorate in listcomprahension and lambda expression use
# print(map_2(lambda a:a**2,l))



# def outer_func():
#     def inner_func():    
#        print('hello')
#     return inner_func
# var=outer_func()
# var()
                                    #    function return function
# def body(word):
#     def maind():
#         print(f'hello{word}')
#     return maind
# var2=body('word')
# var2()

# def power(x):
#     def to_power(n):
#         # return n**x       closure function returning
#     return to_power
# var=power(3)
# print(var(5))

# def func1(another_func):
#     def func2():
#         print("this is awosame line")
#         another_func()
#     return func2
# @func1
# def two_func():
#    print("this is second function")
# two_func()
# var1=func1(one_func)
# var1()
# var2=func1(two_func)
# # var2()
# def hand(another_func):
#     def wrapper():
#         print("this is awesome page")
#         another_func()
#     return wrapper
#                                 # decorator function
# @hand
# def fingure_2():
#     print("this is fingure two")


# fingure_2()
# fingure_2=hand(fingure_2)
# fingure_2()


# def test(another_func):
#     def new_1(*args):
#        print ('this is awesome func')
#        return(another_func(*args))
#     return new_1
# @test
# def new_2(a):
#     print(f"this a new function{a}")
# new_2(5)    

# @test
# def new_3(a,b):
#     return a+b
# print(new_3(2,3))


# from functools import wraps
# def test(another_func):
#    #  @wraps(anoter_func)
#     def new_1(*args):
#        '''this is wrap func'''
#        print ('this is awesome func')
#        return(another_func(*args))
#     return new_1
# @test    
# def test_1(a,b):
#     ''' this add func'''            this most decorates fuction we added
#     return a+b
# print(test_1.__doc__)
# print(test_1.__name__)

# from functools import wraps
# def func1(another_func):
#      @wraps(another_func)
#      def func2():
#          print("this is function")
#          return another_func()           # function tool use and import wraps
#      return func2()
# @func1
# def n1():
#    print("this is a new function")
# print(n1)


# from functools import wraps
# def func1 (another_func):
#     @wraps (another_func)
#     def add(*args,**kwargs):
#        print(f"this are used {another_func.__name__}function")
#        print(f"{another_func.__doc__}")
#        return another_func(*args,**kwargs)
#     return add

# @func1
# def addition(a,b):
#      return a+b
# print(addition(10,20))

# from functools import wraps
# def set_1(func):
#     @wraps(func)
#     def set_2():
#       print("hello !!!!! gaurav..")
#       func()
#     return set_2

# def set_3():
#     print("hello... heandsome")

# set_1=set_1(set_3)
# set_1()

# def fun1(func):
#     print("yooo")
#     def func2():
#         print("hello world")
#         return func()
#     return func2
# def final():
#     print("hey guru")
# final=fun1(final)
# final()


# from functools import wraps
# import time
# def func1(another_func):
#     @wraps(another_func)
#     def func2(*args,**kwargs):
#        print(f"executing {another_func.__name__}")
#        t1=time.time()
#        return_func=another_func(*args,**kwargs)
#        t2=time.time()
#        t3=t2-t1
#        print(f"this function took{t3}second")
#     return func2
# @func1
# def func3(n):
#     return [i**2 for i in range(1,n+1)]
# print(func3(100))



# from functools import wraps
# def func1(function):
#     wraps(function)
#     def func2(*args):
#        if all([type(arg)==int for arg in args]):
#            return function(*args)                 list comprehention
#        print("invlid argument")   
 

        # data_type=[]
        # for arg in args:
        #     data_type.append(type(arg)==int)    create long coding
        # if all(data_type):
        #     return function(*args)
        # else:
#         #     print("invlid argument")
#     return func2
# @func1    
# def test(*args):
#    total=0
#    for i in args:
#       total+=i
#    return total
# print(test(1,2,3,4,[1,2,3,4]))


# decorates function with argurment

# from functools import wraps
# def dec_with_argument(data_type):
#     def func1(function):
#         wraps(function)
#         def func2(*args,**kwargs):
#             if all([type(arg)==data_type for arg in args]):
#                 return function(*args,**kwargs)
#             print("invlid value")
#         return func2
#     return func1
# @dec_with_argument(str)
# def test(*args):                       functions withs argument
#   string=''
#   for i in args:
#       string+=i
#   return string
# print(test('gaurav','is','fine')) 

            





