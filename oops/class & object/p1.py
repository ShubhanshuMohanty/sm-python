class UserInfo: 
    def putData(self): 
        self.name=input("Enter your Name") 
        self.id=int(input("Enter your id")) 
        self.salary=float(input("Enter your salary")) 
    
    def display(self): 
        print("UserName:",self.name) 
        print("User Id:", self.id) 
        print("User Salary:",self.salary) 
        
obj=UserInfo() 
obj.putData() 
obj.display()