#Build an OOP-based system to manage books, members, and borrowing

class Book:
    def __init__(self , title , author , book_id , status):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.status = status

    def __str__(self):
        return f"Book Name: {self.title}, Author: {self.author}, ID: {self.book_id}, Status: {self.status}"
    

class Member:
    def __init__(self , membername  , member_id , book_borrow ):
        self.membername = membername
        self.member_id = member_id
        self.book_borrow = book_borrow

    def __str__(self):
        return f"Member Name: {self.membername}, ID: {self.member_id}, Status: {self.book_borrow}"


class Borrow:
    def __init__(self):
        self.book = []
        self.member = []

    #B O O K
    def add_book(self , title , author , book_id , status):
        book = Book( title , author , book_id , status)
        self.book.append(book)
        print("---Book Added In a Library---")

    def display_book(self):
        for book in self.book:
            print(book)
        else:
            print("---No Book Found!!---")

    # M E M B E R
        
    def add_member(self , membername , member_id , book_borrow ):
        member = Member( membername , member_id , book_borrow)
        self.member.append(member)
        print("---Member Added In a Library---")
        
    def display_member(self):
        for member in self.member:
                print(member)
        else:
                print("---No Member Found---")

    def borrowbook(self , title):
        for book in self.book:
            if book.title.lower() == title.lower():
                if book.status.lower() == 'available':
                    book.status == 'Borrowed'
                    print(f"---{book.title} You borrow this book---")
                else:
                    print(f"---sorry {book.title} is not available---")   
                return
        print("---Book not found---")



library = Borrow()

while True:

    choice = input(
    """Enter your choice:
     'addbook' , 
     'displaybook' ,
     'addmember' , 
     'displaymember' ,
     'borrowbook'
     """)

    if choice == 'addbook':
        title = input("Enter title for Book:")
        author = input("Enter author of Book:")
        book_id = int(input("Enter Book ID:"))
        status = input("Enter Status for Book like Available or Borrowed:")
        library.add_book(title , author , book_id , status)


    elif choice == 'displaybook':
        library.display_book()


    elif choice == 'addmember':
        membername = input("Enter member name :")
        member_id = int(input("Enter member ID :"))
        book_borrow = (input("Enter status that he can borrow:"))
        library.add_member(membername , member_id , book_borrow )


    elif choice == 'displaymember':
        library.display_member()


    elif choice == 'borrowbook':
        bookn = input("Enter book Title or Name to borrow:")
        library.borrowbook(bookn)
        
    else:
        print("Invalid operator! please try again...")

