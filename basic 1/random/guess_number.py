import random 
class GuessNumber:
    def getNum(self):
        self.num=int(input("enter number:"))
    
    def getRandom(self):
        self.random_num=random.randint(1, 100)

    def guessNum(self):
        i=3
        self.getRandom()
        # print(self.random_num)
        while(i>=1):
            self.getNum()
            if self.num==self.random_num:
                print("you guessed right!")
                break
            else:
                i-=1
                if self.num<self.random_num:
                    print("your guess was too low!")
                else:
                    print("your guess was too high!")
                print(f"you guessed wrong! you have only {i} chanse left")

obj=GuessNumber()
obj.guessNum()
            