class bookData:
    def __init__(self,title,year,author):
        self.title = title
        self.year = year
        self.author = author
    
    def display_details(self):
        print(f"title: {self.title} year: {self.year} author:{self.author}")

# Create instances of the BookData class

book1 = bookData("To Kill a Mockingbird", 1960, "Harper Lee")
book2 = bookData("1984", 1949, "George Orwell")
book3 = bookData("Animal Farm", 1945, "George Orwell")

# Display details of each book

book1.display_details()
book2.display_details()
book3.display_details()