# numbers=[5,2,5,2,2]
# for i in numbers:
#     print('x'*i)
# numbers=[1,1,1,1,5]
# for i in numbers:
#     print('x'*i)

# numbers=[5,2,5,2,2]
# for i in numbers:
#     output=''
#     for count in range(i):
#         output+='x'
#     print(output)

# numbers=[5,9,7,9,10,35,5]
# large=numbers[0]
# for i in numbers:
#     if(i>large):
#         large=i
# print(f'large is {large}')
# print(50 in numbers)
# print(numbers.index(5))

# for item in numbers:
#     if numbers.count(item)!=1:
#         numbers.remove(item) 
# print(numbers)


# strV="Hello world"
# print(strV[-1:3:-1])
# print(strV[3:0:-1])
# print(strV.split('w'))
# str2="H e l l o w o r l d"
# print(str2.split(' '))
# c= "I love python and I love c++"
# print(c.split(" ",2))
# string = " she is Leen and she is an Engineer"
# print(string.find('Leen'))
# print(string[8])
# print(string.find('she'))
# print(string.find("majd"))
# a = "leen"
# b = a.replace('l','F')
# print(a)
# print(b)
# c = a.replace("leen","Majd")
# print(c)
# print(len(a)) 

#====================================================================================================================
# Strings
# s = "Hello, world!"
# print(s)

# print("This is a string:", s)

# new_s = "This is a string: " + s
# print(new_s)

# print("s[0]:", s[0])
# print("s[1]:", s[1])
# print("s[2]:", s[2])
# print("s[-1]:", s[-1])
# print("s[-2]:", s[-2])
# print("s[-5]:", s[-5])
# # print("s[13]:", s[13]) # error!

# # s[start:end:step] => start up to (but not including) end using step
# print("s[0:5]:", s[0:5]) 
# print("s[:5]:", s[:5]) 
# print("s[7:13]:", s[7:13])   #write it
# print("s[7:]:", s[7:]) 

# print(s.upper())

# s2 = s.replace("world!","Kameel!")
# print("New string:", s)
# print("New string:", s2)

# s3 = s.replace("Hello","Hi")
# # I want s3 to be "Hi, world!"
# print("New string:", s3)

# a = "H e l l o ,   w o r l d"
# print("a[::2]:", a[::2])
# print("a[::4]:", a[::4])
# print("*"*100)
# print("s[::-1]", s[::-1])

# print("s.find('world'):",s.find('world'))
# print("s[7:]",s[7:])

# r = "world world world world"
# print("r.find('world'):",r.find('world'))
# # find() returns the index of the first instance of the string 

# # Lists
# L = [1, 2, 3]
# print(L)
# print("="*10)
# print(L[:])
# print("L[0]:", L[0])
# print("L[1]:", L[1])
# print("L[2]:", L[2])
# print("L[::-1]", L[::-1])
# print(list(s))
# print(s.split(" "))

#==========================================================================================================

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 20:03:23 2023

@author: Leen
"""
#Lists : []
# we can change it later.

#Tuples: ()
# We CAN'T change it. 

# dictionary: {}
#{"a":1, "b":2}

# *List*: 
# s=[]
# m=[1,2,3]
# a=["Leen",1,5.2]
# b=[2,3,[4,5]]

# convert any type to list:
# x="I love python"
# print(type(x))
# print("="*50)
# x= list(x)
# print(type(x))
# print(x)

# list inside list : 
# b=[2,3,[4,5]]
# print(b[2][0])
# print(b[2][1])
# my_string = "Hello world, how are you doing today?"

# my_list = my_string.split(" ")

# print(my_list)

# def solution(n):
#     num_str = str(n)
#     digit_sum=0
#     for char in num_str:
#         digit_sum += int(char)
#     return(digit_sum)
# res=solution(29)
# print(res)

# def century(year):
#     if year % 100 == 0:
#         return year // 100
#     else:
#         return (year // 100) + 1
# print(century(1700))

#make the list empty:there is 2 ways: 
a = [1,2,3,4,["A","B","C"]]
print(a[4][1])
print(a)
# Way N.1:
# a = []
# print(a)
# Way N.2:
del a[0:-1]
print(a)

#Delete a specific item in the list : 
#a = [1,2,3,4,["A","B","C"]]
#del a[3] # I want to delete N.4 in the list and he index for it is 3 
#print(a)

#add list to other:
#a = [1,2,3,4,["A","B","C"]]
#b= [10,11,12]
#m = a+b
#print(m)

#Length of the list: 
# a = ["A","B","C"]
# print(len(a))
# print(max(a))
# print(min(a))

#sorted list:
#c= [1,2,6,7,4,3,5]
# f=sorted(c, reverse= False) #reverse is False by default
# print(f)
# y=sorted(c,reverse= True)
# print(y)

#add an item for the end of the list: 
# c.append("Leen")
# print(c)

#add an item to specific position: 
#c.insert(2,"Leen") # 2 is the index
#print(c)

#the number of repetioin of an item:
#n= [1,1,1,2,3,4,4,5,6]
# v=n.count(1)
# print(v)

#delete the last item:
#n.pop()
#print(n)

#delete a specific item:
#n.pop(4)
#print(n)


# *Tuple*: 
# m = ("Hello","Leen")
# print(type(m))

# f=(1,1,1,2,2,3)
# print(f.count(1))
# print(f[0])


# *dictionary* : 
names_and_ages = {"Leen":'25' , "Shahed":'20', "Zainab":'21'}

#Change the key's value:
# names_and_ages["Leen"] = '70'
# print(names_and_ages)


# print('25' in names_and_ages.values())

# print(names_and_ages.get("Leen"))

# print(names_and_ages.keys())
# print(names_and_ages.values())
# print(names_and_ages)
# print(names_and_ages.items())

# #add an item to dict: there are 2 ways:
# #way N.1
# names_and_ages["majd"] = 27
# print(names_and_ages)

# #way N.2
# names_and_ages.update({"Sarah":24})
# print(names_and_ages)

# #delete the item according to key: 
# del(names_and_ages['Leen'])
# print(names_and_ages)

# #clear all the items:
# # names_and_ages.clear()
# # print(names_and_ages)

# #delete the dict: 
# # del(names_and_ages)
# # print(names_and_ages)

# #length:
# print(len(names_and_ages))

#delete an item from the dict: 
# print(names_and_ages.pop("Shahed"))
# print(names_and_ages)

#make the items of the list as keys:
# list1 = ["a","b","c","d"]
# dic1 = dict.fromkeys(list1)
# print(dic1)
# dic1["a"] = 4
# dic1["b"] = 100
# print(dic1)

#makes a keys and values from 2 varibales:
# My_keys = ["a","b","c","d"]
# My_values = "x"
# dic1= dict.fromkeys(My_keys,My_values)
# print(dic1)


# dic1 = {"a":'leen', "b" :"shahed" , "c":"Zainab"}
# a = list(dic1.keys())
# b = list(dic1.values())
# c = list(dic1.items())
# print(a,"\n",b,"\n",c)



# *lambda*
# x = lambda a : a + 10
# print(x(5))

# b= lambda a,b,c : a*b*c
# print(b(5,6,1))


# def myfunc(n): 
#     return lambda a: a*n
# double = myfunc(2)
# print(type(double))
# print(double(11))

# fifth = myfunc(5)
# print(fifth(20))