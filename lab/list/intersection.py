#Q.4) Perform Intersection operation on list
# initialize two list
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Display lists
print("List 1:", list1)
print("List 2:", list2)

# Convert the lists to sets and perform the intersection
intersection = list(set(list1) & set(list2))

# Display intersection result
print("\nIntersection of List 1 and List 2:", intersection)
