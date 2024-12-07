'''
To present list in concise and easy way we use List Comprehension.
As size of the code is less, performance will be increased  
'''
marks=[20,35,50,78,40] 
new_marks=[] #Empty list
for x in marks:  
    new_marks.append(x+2) 
    print(new_marks)  
#code using List Comprehension 
marks=[20,35,50,78,40] 
new_marks=[x+2 for x in marks] 
print(new_marks)