# dictionary is unoderlist..
# dictionary in this key : value pair used
# dictionary in index not in their in that are key to use and value get it....
# dictionary in {} used.....

# user_info = dict(name="gaurav",age=20)
# print(user_info)                         # method

# user_info1={
#      'name2' : "gaurav",
#       'age':'20' ,
#      'movie': "big bro",
# }
# print(user_info1['age']
d= {"abc":40,"xyz":45},
b1=["pqr"]
print(b1)


# info={
#     'name' : 'gaurav',
#     'age' : '20',
# }
# # print(info['name'])
# info1= info.keys()
# info1= info.items()
# info1= info.values()
# print(info1)


# if 'name2' in user_info1:
#     print("present")
# else:
#     print("not present")


# for i in user_info1:
#     print(i)                                   # value method in dictnoray(method name are always in value)
# user_info1_value= user_info1.values()
# print(user_info1_value)
# print(type(user_info1_value))


# user_info1_key= user_info1.keys()
# print(user_info1_key)                     #key method in name is key 
# print(type(user_info1_key))

# user_items= user_info1.items()
# print(user_items)                              items method all are key : value in list generating
# print(type(user_items))

# for i ,j in user_info1.items():                  for loop in method items() you can used all  key:value
#     print(f"key is {i} and value is {j}")

# user_info1['fav song']=['song 1','song 2']
# print(user_info1)                                   dict in adding

# user_popped=user_info1.pop('age')
# print(f"popped iteam {user_popped}")         pop method (delete in dict)used
# print(user_info1)

# user_popped=user_info1.popitem()
# print(user_popped)                             popitem method (rendomly in data tu delete with key and values)
# print(user_info1)
# print(type(user_popped))


# more_info={'state':{'Gujarat','rajkot','mumbai'}}
# user_info1.update(more_info)
# print(user_info1)                                     update method in this used
# print(type(more_info))

# G =dict.fromkeys(['name','age'],'unkown')
# print(G)                                                  #formkey used



# memo={'name':'gaurav','age':'20'}
# # print(memo.get('name'))
 
# if memo.get('name'):                          get method used
# # if 'names'in (memo):
#     print('present')
# else:
#     print('not present')

# memo.clear()                                        clear method 
# print(memo)

# m1=memo.copy()
# print(m1)
# m2=m1.popitem()
# print(m2)                                   copy methd( memo=m1 is not a copy)
# print(memo)

# memo=m1         <- this is memo  and m1 is same .these are same side reason.
# print(memo is m1) <- this is describe memo and m1 is not same means dictnoray are  diffrent


# memo={'name':'gaurav','age':'20','age':'30'}
# print(memo.get('age'))


# def cube_finder(n):
#     cubes={}
#     for i in range(1,n+1):
#        cubes[i]=i**3
#     return cubes

# print(cube_finder(3))

# def cube_master(n):
#     cube={}
#     for i in range(n+1):
#        cube[i]=i**3
#     return(cube)
    
# print(cube_master(4))
# # print(type(list_1))  
val = [1,2,3,4,5]
def info(n):
    add = {}
    for i in val:
        add[i]=i**2
    print(add)
print(info(val))

val = [1,2,3,4,5]
def info(n):
    add = []
    for i in val:
        add.append(i**2)
    print(add)
print(info(val))

add =[i**2 for i in val if i%2==0]
print(add)

add =lambda a:a**2
print(add(4))

# def cube_m1(n):
#     # cube_list=[]
#     for i in range (1,n+1):
#         cube_list(range[[i], i**3]
    
#     return cube_list

# print(cube_m1(3))


# def word_counter(s):
#      count={}
#      for char in s:
#         count[char]= s.count(char)            #word_counter must used
#      return count
# print(word_counter('nayan'))
  
# user={}
# name=input('what is your name :')
# age=input('what is your age')
# movie=input('what is your fav movie').split(',')
# song=input('what is your fav song').split(',')

# user['name']=name
# user['age']=age
# user['movie']=movie
# user['song']=song
# for key,value in user.items():
#     print(f"{key}:{value}")
#     print(type(movie))

# some_dict={}
# some_dict[5]="python"
# some_dict[5.0]="java script"
# some_dict[5.00]="java"
# print(some_dict[5])
# print(type(some_dict[5.00]))
# print(type(some_dict[5]))


# some_dict1 = {5:"python",5.00:"java",5.00:"guru"}
# print(some_dict1[5])

arr=[1,2,3,4,5]
print(arr[-3:-6:-1])