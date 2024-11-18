'''A Set in Python programming is an unordered collection data type that is iterable and has no duplicate elements. While sets are mutable, meaning you can add or remove elements after their creation '''
set_a={5,8,67,3,6} 
print (set_a) 
set_b=(6,9,5,6) 
print(set_b) #set does not allow I

set_c={7,9,78,4}
print (set_c) 
#set union operation 
set_d=set_a.union(set_b) 
print("The union of both the sets are:", set_d) 

set_e =set_a.union (set_b,set_c) 
print("The union of all the sets are", set_e)

#using union operator | 
result= set_a |set_b|set_c
print("The union of all is", result)

#using union operator | result-set a set biset c 
print("The union of all is", result) 
#WAP to find intersection of two sets using intersection() function and & operator 
result=set_a&set_b 
print("the intersection is", result) 
#set difference(-) 
result=set_a-set_b 
#=set_a-set_b 
print("The difference is", result) 
#set difference using difference () method 
result=set_a.difference (set_b) 
print("the difference is", result)

#WAP to get symmetric difference (elements which are not in both the sets) 
result=set_a|set_b 
print("The symmetric difference is", result)