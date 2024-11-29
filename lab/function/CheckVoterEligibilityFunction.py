#Q.3)WAP to check whether person can vote or not using function
def check_voting_eligibility(age):
    #Check if a person is eligible to vote based on their age.
    if(age>=18):
        print("You are eligible for vote")
    else:
        print("you are not eligible for vote")

#Take age input from user
age=int(input(" Enter your age: "))
# Check voting eligibility
check_voting_eligibility(age)