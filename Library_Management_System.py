class Library :
    def __init__(self,listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in the library are : ")
        for book in self.books:
            print("* " + book)

    def borrowBook(self,bookname):
        if bookname in self.books:
            print(f"You have issued {bookname}. please keep it safe and return it within 30 days.")
            self.books.remove(bookname)
            return True
        
        else:
            print(f"sorry this {bookname} book is either not available or has already been issued to someone else. Please wait until the book is available.")
            return False

    def returnBook(self,bookname):
        self.books.append(bookname)
        print(f"Thanks for returning this {bookname} book! Hope you enjoyed reading it . Have a great day!")

class Student :
    def requestBook(self):
        self.book = input("Enter the name of the book You want to borrow :")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return :")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["Algorithms","Django","C","C++","Java"])
    student = Student()
    # centralLibrary.displayAvailableBooks()
    while(True):
        WelcomeMsg = '''\n**** Welcome to central library ****
        Please choose an option:
        1.List all the books
        2.Request a book
        3.Add\Return a book
        4.Exit the library
        '''
        print(WelcomeMsg)
        a = int(input("Enter a choice :"))  
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing the central library . Have a great day a head!")
            exit()
        else:
            print("Invalid Choice..")