tuple1=("Aditya", 78, "O grade", 56000, "navi mumbai") 
print (tuple1) 
print (type (tuple1)) 
#slicing a tuple 
print (tuple1 [1:4]) 
print (tuple1 [2:]) 
print (tuple1[:5]) 
#negative indexing 
print (tuple1[-2]) 
print (tuple1[-1]) 

#Note: 
#List is a collection which is ordered and changeable.
#List Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable.
#Tuple Allows duplicate members.

t2=list(tuple1) 
print (t2) 
t2[2]="A in sports" 
print (t2) 
for i in t2: 
    print(i)