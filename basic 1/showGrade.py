percentage=int(input("enter percentage: "))
if(mark>100):
    print("percentage must be less than 100")
elif(mark>=70):
    print("Grade O")
elif(mark>=60):
    print("Grade A")
elif(mark>=40):
    print("Grade B")
elif(mark>=0):
    print("Fail")
else:
    print("percentage must be positive number")
