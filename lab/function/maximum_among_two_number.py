#Q.2)WAP to find maximum among two number
def check_maximum_number(number1, number2):
    #Check which of the two numbers is greater or if they are equal.
    if(number1>number2):
        print(f"{number1} is maximum number ")
    elif(number1==number2):
        print("Both Numbers are Equal")
    else:
        print(f"{number2} is maximum number ")

#take input from user       
number1=int(input("Enter Number 1:"))
number2=int(input("Enter Number 2 :"))
check_maximum_number(number1, number2)