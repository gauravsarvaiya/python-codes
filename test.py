
# i=0
# while(i<=10):
#     print(i)
#     i=i+1

# 


# for i in range(0,10):
#     print(i)                   #  (start:stop:-1(ending))

# for i in range(1,11):
#     print(i)

# number=(1,2,3,4,5,)
# print(number[::-1])

# s = "gaurav"
# print(s[::-1])



# for i in range(1,10):
#    if i%2==0:
#       print(f"{i:} even number!!")
#    else:
#       print(f"{i:} odd number...")
        

# a=80
# b=20
# c=40
# if a>b and  a>c:
#     print(a) 
# elif b>c and b>a:
#     print (b) 
# else:
#     print (c)

# a = int(input("enter number"))
# b = int(input("enter number"))
# c = int(input("enter number"))

# if a>b and a>c:
#     print(a)
# elif b>c and b>a:
#     print(b)
# else:
#     print(c)




# def equl (l1 , l2):
#      output=[]
#      for i in l1:
#         if i in l2:
#             output.append(i)
#      return output
# # lol=[1,2,3,4], [1,2,5,6]
# print(equl([1,2,3,4], [1,2,5,6]))


# def odd_even(l):
#     even_num=[]
#     odd_num=[]
#     for i in l:
#         if i % 2 == 0:
#            even_num.append(i)
#         else:
#            odd_num.append(i)              #(fuction odd even list)
#     output=[even_num, odd_num]
#     return output

# def e_d(l1):
#     even_num = []
#     odd_num = []
#     for i in l1:
#         if i % 2 == 0:
#            even_num.append(i)
#         else:
#            odd_num.append(i)
#     output=[even_num, odd_num]
#     return output
# number =[1,2,3,4,5]
# print(e_d(number))

i= int(input("enter number"))
if i % 2 == 0:
   print(f"{i:}even" )
else: 
   print(f"{i:}odd")







# number=[10,80,7]
# print(min(number))
# print(max (number))
# def greatest(l):
#     return  max(l)-min(l)
# print(greatest(number))



# def coc(l):
#     output=[]
#     count=0                                   #(type)
#     for i in l:
#         if type(i)==list:
#             count += 1
#             output.append(i)
#             game=([count,output])
#     return game

# mixed=[1,2,3,[4,4],[3,3]]
# print(coc(mixed))

        



