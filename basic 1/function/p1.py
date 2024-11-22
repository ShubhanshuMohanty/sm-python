#Q.1) Write a function to reverse a list without using 
#the built-in reverse() method.
def rev_lst(l): 
    return l[::-1]
l=[98,87,45,78] 
print("The reverse is", rev_lst(l))

#Q.2) find second largest element  
l2=[23,24,23,18,19,45,7]
remove_dup=(list (set(l2))) 
print("The final list is", remove_dup) 
sorted_list=sorted(remove_dup) 
print("the sorted list is", sorted_list)

print("second largest element:",sorted_list[-2])