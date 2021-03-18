# square={i:i**2 for i in range(1,10)}
# print(square)

# square={}
# for i in range(1,11):
#     square[i]=i**2            dict.comprehension simple
# print(square)


# string='gaurav'
# name={i:string.count(i) for i in string}
# print(name)                                   for loop in dict_comprehension

# string='gaurav'
# h1={}
# for i in string:
#     h1[i]=string.count(i)
# print(h1)


# { 1:odd,2:even }
# odd_even={i:('even' if i%2==0 else 'odd')for i in range (1,11)}
# print(odd_even)

# d1={}
# for i in range (1,11):
#     if i%2==0:              if else dict_com
#         d1[i]="even"
#         # print('even')
#     else:
#         d1[i]="odd"
# print(d1)

# def getsum(n):
#     sum = 0
#     for i  in str(n):
#         sum += int(digit)
#     return sum
# n = 12345
# print(getsum(n))

def dic(l):
    a1 = {}
    for i in l:
        a1[i]=i**2
        print(a1)
l1 = {1,2,3,4}
print(dic(l1))
