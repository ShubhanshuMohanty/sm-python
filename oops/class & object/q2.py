class Student: 
    def __init__(self, name, age, grade):
        '''
        Initializes the student object. 
        '''
        self.name = name 
        self.age = age 
        self.grade = grade 
    def display_info (self): 
        """ Displays the student's information. """ 
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}") 
        print("Name:",self.name, "Age:",self.age) 
        
#Creating objects 
student1 = Student("Alice", 14, "9th") 
student2 = Student("Bob", 15, "10th") 
#Accessing object methods 
student1.display_info() 
student2.display_info()