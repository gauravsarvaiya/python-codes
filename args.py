# make flexible function
# *opreter 
# *args (argument) is many argument are lunch 
# *args are convernt in truple

# def hey(a,b):
#     return a+b
# print(hey(10,20))  

def hey(*args):
    total=0
    for i in args:
        total += i
    return total
print(hey(10,20,30))    

def parameter_1(*args):
    multiply = 1
    for i in args:
       multiply *= i
    return multiply                #how to use args in programe

                                        #and in program to call how to use argument in this
number=[1,2,3,4]
print(parameter_1(number))    #when i do call number then output is get a list like a[1,2,3,4]
# #                                then i do call*number in value used..tat are so impornat
# def n1 (num ,*args):
#    square=[[i**num if args  else "you didn't pass any args"] for i in args]

# num=[1,2,3]
# print(n1(2,*num))

# exercise:- list readom[1,2,3] to output[1,4,9]
# def n1(num,*args):
#     if args:
#        return [i**num for i in args]
#     else:
#        return "you didn't pass any args"
# nums=[1,2,3]
# print(n1(2,*nums))

#  def name(*args):


# **kwargs

# kwargs(keyword argument)
# **kwargs(double star operater)
# kwargs are create dict 

# def kword(**kwargs):
#     print(kwargs)                           example in kwargs
# kword(name= 'gaurav',age='19')
 

def func (**kwargs):
   for k ,v in kwargs.items():                 #for loop in kwargs
      print(f"{k}:{v}")
func(first_name='gaurav',last_name='sarvaiya')
         
         
def func (**kwargs):
   for k,v in kwargs.items():        #unpacking  in kwargs
      print(f"{k}:{v}")
d={'first_name':'gaurav','last_name':'sarvaiya'}
func(**d)



