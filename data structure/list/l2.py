marks=[34,56,23,89,54] 
print(min (marks)) 
print("The maximum value is", max(marks)) 
#WAP to find second largest element 

#marks.sort();
#print(marks[-2])

#WAP to find second largest element 
for i in range(0,5): 
    for j in range(i+1,5): 
        if marks[j]>marks[i]: 
            temp=marks[i] 
            marks[i]=marks[j] 
            marks[j]=temp  

print(marks) 
print(marks[1])