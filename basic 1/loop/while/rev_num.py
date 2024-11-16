num=int(input("Enter number:"))
copyNum=num
rev=0
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10

if copyNum==rev:
    print("the number is pelindrome")
else:
    print("the number is not pelindrome")