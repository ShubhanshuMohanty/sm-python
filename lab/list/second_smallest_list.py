# initialize my_list
my_list = [2,4,6,8,10,1,8,3] 

# Remove duplicates from the list
remove_duplicate = list(set(my_list)) 

# show original list
print("Original List : ",my_list) 

# Show list after removing duplicates
print("Remove Duplicate  : ",remove_duplicate)

# Sort the list in ascending order
remove_duplicate.sort()

# Find the second smallest element 
second_smallest = remove_duplicate[1] 

# Print the second smallest element
print("\nSecond smallest element in the List is : ", second_smallest)