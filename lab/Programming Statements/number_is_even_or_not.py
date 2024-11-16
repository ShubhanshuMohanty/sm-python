#Q.3) WAP to check whether the number is even or not.

#Take input number from user
number=int(input("Enter a number: "))

# Check if the number is even or odd
if(number % 2 == 0):
    print("The number is even.")
else:
    print("The number is odd.")