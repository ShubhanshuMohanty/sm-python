import random
random_num=random.randint(1, 100)
i=3
# print(random_num)
while(i>=1):
    num=int(input("enter number:"))
    if num==random_num:
        print("you guessed right!")
        break
    else:
        i-=1
        if num<random_num:
            print("your guess was too low!")
        else:
            print("your guess was too high!")
        print(f"you guessed wrong! you have only {i} chanse left")
if i==0:
    print(f"you lost! the correct number was {random_num}")