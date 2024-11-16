num=int(input("Enter number:"))
sum=0
cp_num=num

while(num>0):
    rem=num%10
    sum+=rem*rem*rem
    num=num//10

if cp_num==sum:
    print("the number is Armstrong")
else:
    print("the number is not Armstrong")