'''Q.2) find Cube root of even numbers''' 
cubes=[] 
for x in range (11): 
    if x%2==0: 
        cubes.append(x**3) 
print("listing for loops", cubes)  
#using list comprehension 
easy=[x**3 for x in range (10) if x%2==0] 
print("using List Comprehesion", easy)