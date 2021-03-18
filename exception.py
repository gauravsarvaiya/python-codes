# raise error main not are a diffirent print . but print are user gave error display..
# NotImplementedError: - define error  that is implement of used for this fuction ,method and


# def add(a,b):
#     if (type(a) is int) and (type(b) is int):
#         return a+b
#     raise TypeError('oops you are passing worng data type to function')
# print(add('gu','ru'))


# def add(a,b):
#     if (type(a) is int) and (type(b) is int):
#         return a+b
#     raise TypeError('pls enter interger numbers')
# print(add('two','tt'))


# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def sound(self):
#         raise NotImplementedError ("you have to define this method in subclasses ")
    
# class dog(Animal):
#     def __init__(self, name ,breed):
#         super().__init__(name)
#         self.breed = breed

#     def sound(self):
#         return" Dog are sound bhooowww.....bhoooww"


# class cat(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed
    
    # def sound(self):
    #     return "cat sound are meooow meooow"


# d1= dog('lebra','xxx')
# c1 = cat('meoo','xx2')
# print(d1.sound())
# print(c1.sound())



# Exception :- execution have  time given that error called exception.

# while True:
#     try:
#         age = int(input("enter your age"))
        

#     except ValueError:
#        print("try again, right value cover it")

#     except:
#         print("unexpected error")

#     else:
#         print(f"user input{age}")                  except ValueError discraibe for value KeyError
#                                                    and except exception error means biji koi error that is except
#                                                    else use when try in this function work and not create value and 
#                                                    that time use else.
#                                                    finally all time given ouput that not error and not error,
#         break

#     finally:
#         print("finally block....... ")
 


# def divide():
#         try:
#             a = int(input("enter a number"))
#             b =  int(input("enter a number"))
#             return a/b
#         except ValueError:                          # self make
#            print("pls enter integer value")
#         except:
#             print("pls don't divide by zero")
#         finally:
#             print(" end.....")
# d1= divide()
# print(d1)

# def divide(a,b):
#     try: 
#         return a/b
#     except ZeroDivisionError as err:
#         print(err)
#     except TypeError as err:
#         print(err)
#     except:
#         print("unexcepted error")
#     finally:
#         print("end.....")
# print(divide(10,'2'))

# def divide(a,b):
    
# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as err:
#         print(err)
#     except TypeError as err:
#         print(err)
#     except:
#         print('unexpected err')
# print(divide(10,yy))

# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as err:
#         print(err)                         # must used and read
#     except TypeError as err:
#         print(err)
#     except:
#         print('unexpeted error')
# d1= divide(1,1)
# print(d1)



# custom_exception

# class NameToShortError(ValueError):
#     pass

# def validation(name):
#     if len(name) < 8:
#         raise NameToShortError("name is too short")
# username =input('enter your name')

# validation(username)
# print(f"hello{username}")


# class animal:
#    def __init__(self,name):
#        self.name = name 
  
#    def sound(self):
#        raise NotImplementedError("pls define subclass in method")

# class dog(animal):
#     def __init__(self, name,breed):
#         super().__init__(name)
#         self.breed = breed

#     def sound(self):
#         return ("boww....bow...")

# class cat(animal):
#     def __init__(self, name,breed):          #polymorphism  and inheritance also multiinheritance and raise error not implementerror alsp
#         super().__init__(name)
#         self.breed = breed

#     def sound(self):
#         return ("meoo meoo")

# d1 = dog('dexu','uuuu')
# print(d1.sound())


    
      
        
    