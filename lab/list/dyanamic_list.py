#Q.1)Create dynamic list where you will ask user to enter 5 elements in it and perform insert new element and delete an element operation on it.
# Create an empty list
dynamic_list = []

#Take 5 elements from users for list
print("enter 5 elements to add to the list:")
for i in range(5):
    element = input(f"Enter element {i+1}: ")
    dynamic_list.append(element)

#show current list
print("Current List:", dynamic_list)

# Insert a new element at a specific position
insert_position = int(input("\nEnter the index position to insert a new element:"))
new_element = input("Enter the element: ")

# Insert the new element at the specified position
dynamic_list.insert(insert_position, new_element)

# Display the list after insertion
print("\nList after insertion:", dynamic_list)

# Delete an element by value
element_to_delete = input("\nEnter the element to delete from the list: ")

# Check if the element exists in the list
if element_to_delete in dynamic_list:
    dynamic_list.remove(element_to_delete)
    print(f"\n{element_to_delete} has been deleted.")
else:
    print(f"\n{element_to_delete} is not in the list.")

# Display the final list
print("\nFinal List:", dynamic_list)
