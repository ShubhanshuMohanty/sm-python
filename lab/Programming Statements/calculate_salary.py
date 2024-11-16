#Q.4) WAP to accept basic salary from user and Give 10% of DA on basic salary ,12% 
# HRA on basic salary  to employee if the salary is more than 50000 .calculate total salary.

# take input of basic salary from user
basic_salary=float(input("Enter Your Basic Salary : "))

# Initialize da and hra
da=basic_salary*0.10   
hra=basic_salary*0.12 

# Calculate total salary
if(basic_salary > 50000):
    total_salary=hra+da+basic_salary 
else:
    total_salary=basic_salary    

#show total salary
print("Total salary : ",total_salary)
    
