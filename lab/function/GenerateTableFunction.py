#Q.4)WAP to get table of a number using function

def print_table(number):
    #Print table for the given number.
    for i in range(1,11):
        print(f"\t{number} x {i} = {number*i}")

# Take input from user for printing table
number=int(input("Enter a number :"))

# Print the  table
print_table(number)