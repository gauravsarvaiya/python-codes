# **PADK**

# parameters
# *args                         fuction in parameter how to  use and how to oderwise can be print 
# defult parameters
# **kwargs


# def func(name, *args,age='unkown',**kwargs):
#        print(name)
#        print(args)
#        print(age)
#        print(kwargs)
# func('gaurav', 1,2,3,age='25',name1='gaurav',surname='sarvaiya')


# exercise

# name=[gaurav,mansi]
# output=[Gaurav,Mansi]


def func(l,*args):
    # if kwargs.get('reverse_str')==True:
    #     return[name[::-1].title()for name in l]
    # else:

        print(*args)                             # how to use camel letter best learn it
        return[i.title()for i in l]
names =['gaurav','mohit']
print(func(names))
