class Book:
    def __init__(self,author="",title=""):
        self.author=author
        self.title=title
    def display(self):
        print(f"'{self.title}, written by {self.author}'")
obj1 = Book("J.K. Rowling", "Harry Potter and the Goblet of Fire")
obj2 = Book("Walter Scott", "Ivanhoe: A Romance")
obj1.display()
obj2.display()
