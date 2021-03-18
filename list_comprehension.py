# number=[]
# for i in range (1,11):    simple list create
#     number.append(i)
# print(number)


# new_number=[i**3 for i in range(1,11)]
# print(new_number)

                                        #  list comrehension   l

# new_one=[-i for i in range (1,11)]
# print(new_one)

name=['guru','yash','harsh']
# names=[]
# for i in name:
#     names.append(i[0])
# print(names)
# new_love=[j[0] for j in name]
# print(new_love)

# def new (l):
#    return[i[::-1] for i in name]
# print(new(['guru','yash','harsh']))
# name=['guru','dudu','ruty']
# def new(l):
#     add = []
#     for i in name:
#         add.append(i[::-1])
#     print(add)
# print(new(['guru','dudu','ruty']))

n1=[]
for i in range (1,11):
    if i%2 !=0: 
       n1.append(i)
print(n1)

# odd_number=[i for i in range(1,11) if i%2 !=0]
# print(odd_number)
                                                         #   if use in lc
# even_number=[i  for i in range (1,11) if i%2==0]
# print(even_number)

# def all_n1(l1):
#    return str(i) for i in l1 if(type(i)==int or type(i)==float or type(i)==list)
# print(all_n1([True,False,[1,2,3,4,5],1,1.0,1]))

# def all_n(l):
#    b1=[]
#    for i in l:
#       if type(i)==int or type(i)==float:
#          b1.append(str(i))
#    print(b1)
# print(all_n([True,False,[1,2,3,4,5],1,1.0,1]))

#
def prime(l):
    a = []
    for i in l:
        if i%2 != 0:
          a.append(i)
        else:
            pass
    return a
number = [1,2,3,4,5]
print(prime(number))

l=[1,2,3,4,5,6]
h1=[]
for i in l:
   if i%2==0:
      h1.append(i*2) 
   else:
      h1.append(-i)
print(h1)                               # if ,else lc

# def new_list(l1):
#    return[i*2 if i%2==0 else -i for i in l1]
# print(new_list([1,2,3,4,5,6]))


# nested_ex=[[1,2,3],[1,2,3],[1,2,3]]
# nested_ex =[[ i for i in range(1,4)]for j in range(3)]
# print(nested_ex)
# c1=[]
# for   i in range(3):                        #nested ic used
#     c1.append([1,2,3]) 
# print(c1)

# x=100
# y=50
# if (x**2>100 and y<100):
#     print(True)
# else:
#     print(False)

# l1 = [1,2,3,4,5]
# s1 = [i for i in l1 if i%2 != 0]
# print(s1)

# def star(l):
#     a1 = []
#     for i in l:
#         a1.append(i**2)
#     print(a1)
# s1 = [1,2,3,4,5]
# print(star(s1))

