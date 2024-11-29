#Q.1)WAP to get factorial of a number using function
def calculate_factorial(number):
    if number < 0:
        print("\nFactorial is not defined for negative numbers.")
    elif number == 0:
            print(f"\nThe factorial of {number} is: 1")
    else:
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        print(f"\nThe factorial of {number} is: {factorial}")

user_input = int(input("Enter a number to calculate its factorial: "))
calculate_factorial(user_input)