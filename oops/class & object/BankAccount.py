class BankAccount:
    def __init__(self,balance,name):
        self.balance = balance
        self.name = name
        print(f"account created for {name} with balance {balance}")
    
    def getData(self):
        print(f"name={self.name} \n balance={self.balance}")

    def deposite(self,amt):
        self.balance+=amt
        print(f"Deposited {amt} into account. New balance is {self.balance}")

    def withdraw(self,amt):
        if self.balance >= amt:
            self.balance-=amt
            print(f"Withdrew {amt} from account. New balance is {self.balance}")
        else:
            print("Insufficient balance")
