#Q.1)WAP to calculate simple interest.

# Define the rate of interest
rate_of_interest=7

#Take input for number of years from users
number_of_years=int(input("Enter the number of years: "))

#Take input for principal amount from users
principal_amount=float(input("Enter the principal amount: "))

#Calculate simple interest
simple_interest=(principal_amount * rate_of_interest * number_of_years) / 100

#Print the calculated simple interest
print("The simple interest is: ", simple_interest)