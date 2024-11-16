#A dictionary is a built-in data structure in Python that allows you to store a collection of key-value pairs.
# #dictionary is mutable and it is unordered 
my_dict={ "std id":1233, "std name": "Sanjana", "course": "BCA"}
print(my_dict) 
#Accessing Elements 
x=my_dict ["course"] 
print(x) 
x=my_dict.get("std_name")
print(x) 
#find all the keys present in the dictionary 
print(my_dict.keys())
y=my_dict.keys()
print("The keys present are:",y) 
#To update dictionary element 
my_dict.update({"std name":"Sameer"}) 
print (my_dict) 
#To add new element in the dictionary 
my_dict ["fees"]=76000 
print(my_dict) 
my_dict ["std Addr"]="Navi Mumbai" 
print (my_dict) 
#To remove certain element from the dictionary 
my_dict.popitem() 
print (my_dict)

#looping over dictionary 
for i in my_dict: 
    print(i) 
#to GET keys from the dictionary 
for i in my_dict.keys(): 
    print(i) 
#To get values from the list 
for i in my_dict.values(): 
    print(i) 
for x,y in my_dict.items(): 
    print(x,y)