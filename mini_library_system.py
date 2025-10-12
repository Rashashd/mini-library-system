class Book:
    def __init__(self, title: str, author: str, availability = True):
        self.title = title
        self.author = author
        self.availability = availability

    def display_info(self):
        if self.availability == True:
            print(self.title, "by", self.author, " - Available")
        else:
            print(self.title, "by", self.author, " - Not Available")

class Library:
    def __init__(self, books: list):
        self.books = books
    
    def show_books(self):
        print("\nThe books in this library are:\n")
        for book in self.books:
            book.display_info()

def borrow_book(library, title):
    found = False
    for book in library.books:
        if book.title.lower() == title.lower():
            found = True
            if book.availability == True:
                print("You borrowed", book.title, "!")
                book.availability = False

            else:
                print("This book is not available right now! Come back Later.")
    
    if found == False:
        print("There is no such book in our Library!")
            

def return_book(library, title):
    found = False
    for book in library.books:
        if book.title.lower() == title.lower():
            found = True
            if book.availability == False:
                book.availability = True
                print("You returned", title, "!")

            else:
                print("This book is already returned.")

    if found == False:
        print("This book is not from our Library!")



book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("Scattered Minds", "Gabor Mate")
book3 = Book("Start with why", "Simon Sinek")
book4 = Book("The Hobbit", "J.R.R Tolkien")
book5 = Book("Game of Thrones", "George R.R. Martin")
book6 = Book("Good Inside", "Becky Kennedy")

my_books = [book1, book2, book3, book4, book5, book6]

library = Library (my_books)

print("\nWelcome to the Library :)\n")

while True:

    print("\nPlease choose an option:")
    print("1. Show all books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit\n")

    option = input("Enter a number from 1 to 4: ")

    if option == "1":
        library.show_books()
    
    elif option == "2":
        title = input("Enter book title you want to borrow: ")
        borrow_book(library, title)

    elif option == "3":
        title = input("Enter book title you want to return: ")
        return_book(library, title)

    elif option == "4":
        print("Thank you for visiting our library\nSee you Soon!")
        break

    else:
        print("Invalid option. Please choose between 1 and 4:")