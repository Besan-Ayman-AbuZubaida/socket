#string methods
x="\nhello, how are you today"
# print(x)
# newx=x.strip().capitalize()
# print(newx)
# print(newx)
# print(x.upper().startswith("HELLO"))
# z='valn 10'
# print(z.strip('vlan').strip())
# y="hello how are you are you good"
# print(y.count('you'))
# q="11111552"
# print(q.count('111'))
# age=20
# gpa=3.5

# print("Besan is ", age," years old and gpa is ",gpa)
# #formatted string
# print(f" Besan is {age} years old and gpa is {gpa}")
# print("Besan is {} years old and gpa is {}".format(age,gpa))
# newText="Besan is %s years old and gpa is %s" %(20,3.5)
# print(newText)

# ipadd=['10','0','0','1']  #"10.0.0.1"
# n='*'.join(ipadd)
# print(type(n))

# ipadd2="10.0.0.1"  
# print(ipadd2.split('.'))

# print('='*100)

##lists  []
mylist=[1,2,3,4,"Besan",['a','b','c']]
# print(mylist)
#2Dlist
# print(len(mylist))
# strv="Besan"
# print(len(strv))
# mylist.append(12.5)
# print(mylist)
# mylist.insert(2,"hello")
# print(mylist[-2])
# print(dir(mylist))
# vendors=[]
# vendors.append('cisco')
# vendors.append('juniper')
# vendors.append('cisco')
# print(vendors.count("cisco"))
# p=[1,2,3]
# print(p.index(2))
# print(p.pop(p.index(2)))
# print(p)


# o=[5,9,7,6]
# a=[1,2,3]
# print(a+o)
# o[4]=10
#ascending sort
# o.sort()  #sort the original method
# o.reverse()
# print(o)
# m=sorted(o)# doesn't sort original method it returns a new list
# print(m)


#dictionaries  key value pairs {key: value, }
# names_and_ages={"Besan": "20","Majd": "25"}
names_and_ages=dict(Besan="20", Majd="25")
# print(type(names_and_ages))
names_and_ages['Huda']="30"
# print(names_and_ages)
# print(dir(names_and_ages))
# newnames={"Heba": "35"}
# names_and_ages.update(newnames)
# print(names_and_ages)
# print(newnames)
# print(names_and_ages.get("Besan"))
# print(names_and_ages.pop("Majd"))
# print(names_and_ages)
# print(list(names_and_ages.values()))
# # print(names_and_ages["maryam"])
name="Besan"
# print(list(name))
# mylist2=[1,2,3]
# for index, value in enumerate(mylist2):  #(index, item)
#     print('index', index, "  ",item)

# for key, value in names_and_ages.items():
#     print(key+":  "+value)


#sets  {} set([]) unique unorder can be modified
# vendors={"cisco", "Dell","cisco"}
# print(type(vendors))
# print(len(vendors))
# vendors.add("HP")
# vendors.add("juniper")
# vendors.remove("cisco")
# vendors.pop()    #remove an arbitrary element
# # print(vendors)
# print(vendors)
# vendors.update({"arista"})
# print(vendors)
# myset=set([1,2,3])
# print(type(myset))
# print(myset)
#set([]) sict(key=value)   list [] set {} tuples()
#tuples  () tuple([]) can't be modified
# mytuple=(1,2,3,4)
# mytuple=tuple([1,2,3,4])
# print(mytuple) 
# print(type(mytuple)) 
# print(dir(mytuple))
# mytuple.append(5)  #error

# x=0
# while x<5:
#     x+=1
#     if(x==3):
#        break 
#     print(x)




# def getcommand(id,name):
#     commands=[]
#     commands.append('vlan '+id)  #['vlan 10']
#     commands.append('name '+name)#['vlan 10', 'name users']
#     return commands

# def pushcommand(device, commands):
#     print('connecting to device ',device)
#     for cmd in commands:  #['vlan 10', 'name users']
#         print('sending command: ',cmd)

# devices=['switch1', 'switch2', 'switch3']
# vlans=[{'id':'10', 'name':'USERS'},{'id':'20', 'name':'VOICE'},{'id':'30', 'name':'WLAN'}]  
# for vlan in vlans:  #{'id':'10', 'name':'USERS'}
#     id= vlan.get('id')
#     name= vlan.get('name')
#     # print('configuring vlan '+id)
#     command=getcommand(id,name)
#     for device in devices:
#        pushcommand(device, command)
#        print('\n')


# f=open("myfile.txt","a")
# f.write("\nWelcome")
# print(f.readlines())
# myfileread=f.read()
# mylist=myfileread.splitlines()
# # print(mylist)
# for item in mylist:
#     print(item)
# f.seek(4)
# readmyfile=f.read()
# print(readmyfile)
# print(f.mode)

# f.close()

# with open("D:\\hello.txt","r") as myfile2:   #absolute path
#     print(myfile2.read())

#     #relative path

# with open("..\\hello.txt","r") as myfile2:   #absolute path
#     print(myfile2.read())


# with open("vlans.txt","r") as myvlan:
#     vlanlist=myvlan.readlines()    #[{'id':'10','name': 'users'},{'id':'20','name': 'voice'}]....
#     mylist=[]
#     for vlans in vlanlist:
#         if 'vlan' in vlans:
#             temp={}
#             id=vlans.strip().strip('vlan').strip()
#             temp['id']=id
#         elif 'name' in vlans:
#             name=vlans.strip().strip('name').strip()
#             temp['name']=id
#             mylist.append(temp)
#     print(mylist)
#     add_vlan={'id': '70', 'name': 'MISC'}
#     mylist.append(add_vlan)
#     print(mylist)
    
# mylist3= [{'id': '10', 'name': '10'}, {'id': '20', 'name': '20'}, {'id': '30', 'name': '30'}, 
#           {'id': '40', 'name': '40'}, {'id': '50', 'name': '50'}, {'id': '60', 'name': '60'}]
# [{'id': '10', 'name': '10'}, {'id': '20', 'name': '20'}, {'id': '30', 'name': '30'}, 
#  {'id': '40', 'name': '40'}, {'id': '50', 'name': '50'}, {'id': '60', 'name': '60'}, 
#  {'id': '70', 'name': 'MISC'}]

# with open("writevlan.txt","w") as wvlan:
#     for item in mylist3:
#          id=item.get('id')
#          name=item.get('name')
#          wvlan.write('vlan '+id+'\n')
#          wvlan.write('    name '+name+'\n')


name="Besan"
try:
    print(name[20])
except:
    print("index out of bound")

































