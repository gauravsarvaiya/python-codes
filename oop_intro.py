# **encapsulation:- that's means data to functinalty are used.that is a encapsulation.
                # :- in this __init__ all method , and functions that is a encapsulation


# **abstraction:-this are complexity can do hide..
# **mean:- l1=[3,4,2,5,1]
#        l1.sort()  {tim sort method that is a abstraction}
#        print(l1)

# l1 = [3,4,2,5,1,6]
# l1.sort()
# print(l1)

# naming convention: that is #_name <-- this is private means condtion apply pls can not be changea 
#                   and all method all are  public

                  #_name = this is convention of private name
                  #__name__ = called dunder/magic method

  # class Person:
#     def __init__(self,first_name,last_name,age):
#           print("hello This  is my first oop programe")
#           self.first_name=first_name
#           self.last_name=last_name
#           self.age=age
# p1=Person('gaurav','sarvaiya','20')
# print(p1.first_name)
# print(p1.last_name)
# print(p1.age)


# class Laptop:
#     def __init__(self, brand_name, model_name,prize):
#           print('This is leptop future')
#           self.brand=brand_name
#           self.model=model_name
#           self.prize=prize
# l1=Laptop('lenovo','b60','35,000')
# l2=Laptop('del','d70','40,000')
# print(l1.brand)
# print(l1.model)
# print(l1.prize) 

# print(l2.brand)
# print(l2.model)
# print(l2.prize)

# # object create

# class Person:
#     def __init__(self,first_name,last_name,age):
#         self.first=first_name
#         self.last=last_name
#         self.age=age
#     def full_name(self):
#         return f"{self.first} {self.last}"
    
#     def age_above(self):
#         return self.age>18

# p1=Person('gaurav','sarvaiya',15)
# p2=Person('bhavik','sarvaiya',24)
# print(p1.first)
# print(p2.full_name())
# print(p1.age_above())

# # exresice
# class Leptop:
#     def __init__(self,brand_name,model_name,prize):
#         self.brand=brand_name
#         self.model=model_name
#         self.prize=prize
    
#     def persentage (self,num):
#         off_prize=(num/100)*self.prize
#         return self.prize-off_prize
    
#     def addition (self,number):
#         return (number+self.prize)
    
# l1=Leptop('gaurav','sarvaiya',60000)
# print(l1.persentage(30))
# print(l1.addition(100))


# class variable
# class(name).class variable


# class Circle:
#     pi=3.14
#     def __init__(self,radius):
#         self.radius=radius
    
#     def cal_circumfernce(self):        
#         return 2*Circle.pi*self.radius

# c1=Circle(10)
# c2=Circle(15)
# print(c1.cal_circumfernce())
# print(c2.cal_circumfernce())


# class Person:
#     discount=10
#     def __init__(self,brand_name,prize):
#         self.brand_name=brand_name
#         self.prize=prize
    
#     def persentage(self):
#          return (Person.discount/100)*self.prize  # class variable

# p1= Person('puma',110000)
# print(p1.persentage())

# class Student:
#     Student_counter=0
#     def __init__(self,name,student_id,subject):
#         Student.Student_counter+=1
#         self.name=name
#         self.id=student_id
#         self.subject=subject
# s1=Student('gaurav',123,'python')
# s2=Student('gaurav',123,'python')
# s3=Student('gaurav',123,'python')
# print(Student.Student_counter)
 

# oop class method



# class Person:
#     instances_count=0
#     discount=10
#     def __init__(self,brand_name,prize):
#         Person.instances_count += 1
#         self.brand_name=brand_name
#         self.prize=prize
    
#     @classmethod
#     def count_instance(cls):
#         return f"you have{cls.instances_count}objects of person class"
    
#     def persentage(self):
#          return (Person.discount/100)*self.prize  # class variable

# p1= Person('puma',110000)
# print(p1.persentage())
# print(Person.count_instance())

# example

# class Version:
#     def __init__(self,full_name,last_name,age): 
#         self.full_name=full_name
#         self.last_name=last_name
#         self.age=age
    
#     def f_name(self):
#         return f"My name is {self.full_name}{self.last_name}"

# v1=Version('Gaurav','sarvaiya',30)
# v2=Version('yash','makwana',30)
# print(v1.full_name)
# print(v2.f_name())


# # classmethod programe

# class Person:
#     count_instance=0
#     def __init__(self,first_name,last_name):
#         Person.count_instance += 1
#         self.first_name=first_name
#         self.last_name=last_name
    
#     @classmethod
#     def instances_count(cls):
#         return f"you have create {cls.count_instance} intance class"
    
#     @classmethod
#     def couns_method(cls,string):
#         first,last= string.split(',')
#         return cls(first,last)  

#     @staticmethod
#     def hello():
#         print('this is a static method')     
         
   
#     def Full_name(self):
#         return f"my name is{self.first_name}{self.last_name}"

# p1=Person('gaurav','sarvaiya')
# p2=Person.couns_method('yash,makwana')
# print(p1.Full_name())
# print(Person.instances_count())
# print(Person.hello())


# x =4
# # y = ["rad","yellow","green"]
# for j in range(x):
#    for i in range(x):
#      print(i)


                                       # inheritance
# inheritance allows us to define a class that inherits all the method and
# # properties from another class
# MRO -> METHOD RESOLUTION ORDER

# __init__ method this is constructor
# init method vagar be biju kaik lakhi sakai
 
# class Phone:
#   def __init__(self, brand,model_name ,price):
#      self.brand = brand
#      self.model_name = model_name
#      self.price = max(price,0)
  
#   def full_name(self):
#     return f"{self.brand}  {self.model_name}"
  
#   def make_a_call(self,number):
#     return f"calling{number}..."

# class Smartphone(Phone):
#   def __init__(self ,brand, model_name, price , ram ,memory_internal ,rear_camera):
#     super(). __init__(brand,model_name,price)
#     self.ram = ram
#     self.memory_internal = memory_internal
#     self.rear_camera = rear_camera


# phone = Phone ('nokia','1100',1000)
# smartphone = Smartphone ('oneplus','5', 3000 ,'6 GB','64 GB','20 mp')
# print(phone.full_name())
# print(smartphone.full_name() + f" a price is {smartphone.price}")




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


# class A:
#   def __init__(self,firstname ,lastname):
#     self.firstname = firstname
#     self.lastname = lastname
  
#   def full_name(self):        
#     return f"{self.firstname} {self.lastname}"

# class B(A):                                      #multi inheritencce , overriading(full_name)2 time use tha is overradding
#   def __init__(self,firstname ,lastname,age):
#     super().__init__(firstname ,lastname)
#     self.age = age

#   def full_name(self):
#       return f"{self.firstname} {self.lastname} {self.age}"

  
#   # def year(self):
#   #   return f"{self.age}"

# class C(B):
#   def __init__(self,firstname ,lastname ,age ,subject):
#     super().__init__(firstname ,lastname,age)  
#     self.subject = subject

# new = A("gaurva","sarvaiya")
# new2 = B("yash","makwana",20)
# new3 = C("parth","vora",21,"android")
# print(new3.subject)
# print(new3.full_name())
# print(new2.full_name())
# print(isinstance(new2,B))  ---> object are create that is same class object? that check are used isintance
                                  #  and ans made boolean value(true,or false)

# class A:
#   def __init__(self,fullname,lastname):
#     self.fullname = fullname
#     self.lastname = lastname
  
#   def full_name(self):
#     return f"{self.fullname} {self.lastname}"

# class B(A):
#   def __init__(self,fullname,lastname,age):
#     super().__init__(fullname,lastname)
#     self.age = age

# new = A('gaurav','sarvaiya')
# new2 = B('yash','makwana',20)
# print(new.full_name())
# print(new2.full_name())
# print(new2.age)


# class A:
#   def __init__(self,color,dimcolor):
#     self.color = color
#     self.dimcolor = dimcolor

#   def add_color(self):
#     return f"{self.color} {self.dimcolor}"

#   def hello(self):
#     return "hey class A"

# class B:
#   def hello(self):
#     return "hey class B"

# class C(B,A):
#   pass

# newC = C('yellow','brown')
# newB = B()
# newA = A('black', 'white')
# print(newA.add_color())
# print(newB.hello())
# print(newC.add_color())
# print(help(C))


# class Student:
#   def __init__(self,name):
#     self.name = name

#   def __init__(self,name,age):
#     self.name = name
#     self.age = age                 

# s1 = Student('gaurav',20)
# s2 = Student('yash',20)
# print(s2.name)
# print(s2.age)
# print(s1.age)
  
class animal:
  def __init__(self,name,breed):
    self.name = name
    self.breed = breed

  def sound(self):
    raise NotImplementedError("pls create method in subclass")

class Dog(animal):
  def __init__(self, name, breed):
      super().__init__(name, breed)
  
  def sound(self):
    return f"bow...boww"
  
class cat(animal):
  def __init__(self, name, breed):
    super().__init__(name, breed)
  
  def sound(self):
    return f"meooo meoo"

d1=Dog('lll','bee')
print(d1.sound())
    
