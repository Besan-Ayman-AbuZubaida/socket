# vlans=[{'id':'10','name':'Users'},{'id':'20','name':'voice'},{'id':'30','name':'wlan'}]
# devices=['switch1','switch2','switch3']

# #Configuring Vlan: 10
# #connecting to device: switch1
# #sending command: vlan 10
# #sending command: name Users

# #connecting to device: switch2
# #sending command: vlan 10
# #sending command: name Users

# #connecting to device: switch3
# #sending command: vlan 10
# #sending command: name Users

# def get_command(id,name):
#     command=[]
#     command.append('vlan '+id)
#     command.append('name '+name)
#     return command

# def push_command(device,command):
#     print('connecting to device '+device)
#     for cmd in command:
#         print('sending command: '+cmd)
#     print('\n')


# for vlan in vlans:
#     id=vlan.get('id')
#     name=vlan.get('name')
#     command=get_command(id,name)
#     print('\n')
#     print('configuring vlan '+id)
#     for device in devices:
#         push_command(device, command)

# with open("instructors.csv","r")as f:
#     for row in f:
#         print(row.strip())
#         fields=row.strip().split(',') 
#         fName=fields[0]
#         lName=fields[1]
#         email=fields[2]
#         print("{}{}'s email is {}\n".format(fName,lName,email))
#***********************************************************************


# x= 5
# y = 6
# # print(not(x<3 and x>10))

# z = x
# z=10
# print(x, z)
# w=[1,2,3]
# d=w
# d=[1,1,4]
# print(w,d)
# if (z is x): print("true")
# if ( z is not y): print("false")

# print("-"*60)

# def childnames(child3, child2, child1):
#   print("The youngest child is " + child3)
# childnames(child1 = "Shahd", child2 = "Majd", child3 = "Leen")
# # childnames("Shahd"," Leen" , "majd")
#================================================================================================

#sorted list:
# c= [1,2,6,7,4,3,5]
# f=sorted(c, reverse= False) #reverse is False by default
# print(f)
# y=sorted(c,reverse= True)
# print(y)



#the number of repetioin of an item:
# n= [1,1,1,2,3,4,4,5,6]
# v=n.count(1)
# print(v)

# *Tuple*: 
# m = ("Hello","Leen")
# print(type(m))

# f=(1,1,1,2,2,3)
# print(f.count(1))
# print(f[0])


# *dictionary* : 
# names_and_ages = {"Leen":'25' , "Shahed":'20', "Zainab":'21'}




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
# names_and_ages.clear()
# print(names_and_ages)

# #delete the dict: 
# del(names_and_ages)
# print(names_and_ages)

# #length:
# print(len(names_and_ages))

#delete an item from the dict: 
# print(names_and_ages.pop("Shahed"))
# print(names_and_ages)

#make the items of the list as keys:
# list1 = ["a","b","c","d"]
# dic1 = dict.fromkeys(list1)
# print(dic1)
# # dic1["a"] = 4
# # dic1["b"] = 100
# print(dic1)

# makes a keys and values from 2 varibales:
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
#=====================================================================================
# lesson 5


f=open("besan.txt","r")
y=f.read()
vlan_list=y.splitlines()   #list [vlan 10, name users]
vlans=[]   #[{'id' :10, 'name' :'users'}]
for item in vlan_list:
    if 'vlan' in item:
        temp={}
        id=item.strip().strip('vlan').strip()
        temp['id']=id
    elif 'name' in item:
        name=item.strip().strip('name').strip()
        temp['name']=name
        vlans.append(temp)
# print(vlans)
# add_vlan={'id': '70', 'name': 'MISC'}
# vlans.append(add_vlan)
# print(vlans)
# vlans=[{'id': '10', 'name': 'USERS'}, {'id': '20', 'name': 'VOICE'}, {'id': '30', 'name': 'WLAN'}, {'id': '40', 'name': 'APP'}, {'id': '50', 
# 'name': 'WEB'}, {'id': '60', 'name': 'DB'}]
# f.close()
# write_file=open("besan.txt","w")
# for vlan in vlans:
#     id=vlan.get('id')
#     name=vlan.get('name')
#     write_file.write('vlan '+id+'\n')
#     write_file.write('\t name '+name+'\n')
# 
strV="Bisan 10"
# try:
print(strV.strip('Bisan').strip())
# except:
#     print("out of bound")


    


        



# text = b.readlines()
# print(text)
# b.close()


# f = open("leen.txt","w")
# f.write("Hi Leen")
# f.close()

# x = open("E:\\Leen1.txt","w")
# x.write("Hi Shahed, and Hello Majd\n")
# x.close()


# x=open("E:\\Leen1.txt","a")
# x.write("Hi")
# x.close()

# b=open("E:\\Leenfile\\Test.txt")
# y= b.read()
# print(y)
# # print(b.name)
# # print(b.mode)
# text = b.readlines()
# print(text)
# b.close()

# b=open("E:\\Leenfile\\Test.txt")
# # print(b.name)
# # print(b.mode)
# text = b.readlines()
# print(text)
# b.close()


# b= open("E:\\Leenfile\\Test.txt")
# text1 = b.readline()
# text2 = b.readline()
# print(type(text1))
# print(text2)
# b.close()



# b= open("E:\\Leenfile\\Test.txt","r")
# t = b.read()
# b.seek(0)
# tx = b.readlines()
# print(tx)
# b.close()

# b= open("E:\\Leenfile\\Test.txt","w")
# mylines = ["Hi Leen,Majd,Zainab"]
# b.writelines(mylines)
# b.close()



# Capitalize() method
# s ="hello, how are you?"
# x = s.capitalize()
# t = s.upper()
# print(x)
# print(t)

# s =" hello, how are you?"
# x = s.strip().capitalize()
# print (x) # doesn't work because of space so use s.strip().capitalize()

# casefold() Method
# s =" HELLO, HOW ARE YOU?"
# x = s.casefold()
# t = s.lower()
# print(t)


# x = [i for i in range(1,10)]
# print(x[5])



    










#*********************************************************************************************************
# def get_commands(vlan,name):
#     commands=[]
#     commands.append('vlan '+vlan)
#     commands.append('name '+name)  #comands=[vlan 10,name users]
#     return commands

# def push_command(device,command):
#     print('connecting to device: '+device)
#     for cmd in command:
#         print('sending command: '+cmd)
#     print('\n')

# for vlan in vlans:  #{'id':10,'name': 'users'}
#     id=vlan.get('id')
#     name=vlan.get('name')
#     command=get_commands(id,name)
#     print('\n')
#     print('confiugring vlan ',id)
#     for device in devices:
#         push_command(device,command)











#lists >>  [,,,]
#set >>unique /can't be indexed set([,,,])
#tuple >>immutable tuple([,,,])
#dic  dict('key'='value') {'key':'val}



