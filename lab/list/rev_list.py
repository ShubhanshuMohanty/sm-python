# initialize my_list
my_list = [2,4,6,8,10]

# Display my_list
print("Original List:", my_list)

# Reverse the list using slicing
reversed_list = my_list[::-1]

# Display the reversed list
print("\nReversed List:", reversed_list)

# Reverse the list using the reverse() method
my_list.reverse()  # In-place reversal of the original list

# Display the reversed list
print(f"Reversed list with method : {my_list}")