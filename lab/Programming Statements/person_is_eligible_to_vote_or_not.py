#Q.2)WAP to find whether person is eligible to vote or not.

# Take input age from user
age=int(input("Enter your age : "))

#check eligibility 
if(age>=18):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")