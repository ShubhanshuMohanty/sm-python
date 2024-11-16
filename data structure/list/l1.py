#List is a collection which is ordered and changeable. 
#Allows duplicate members. 
my_list=["Soap", "Oil", "Maggie", "Tea", 345, "buiscuits", "rice"] 
print(my_list) 
for i in my_list: 
    print(i)

my_list.append("Dalia") 
print(my_list)

#list element is recognized by its index value 
#first element my list [0] 
print(my_list[0]) 

#there is concept of negative indexing 
print(my_list[-1]) 

#slicing 
print(my_list[1:4]) 
print(my_list[:]) 
print(my_list[2:]) 
print(my_list[:5]) 
print(my_list[::-1]) #reverse