from abc import ABC, abstractmethod

# 1. Abstract Class: Member (Abstraction and Encapsulation)
class Member(ABC):
    def __init__(self, member_id, name):
        self._member_id = member_id  # Encapsulation
        self._name = name
        self.borrowed_books = []

    @abstractmethod
    def borrow_book(self, book):
        pass

    @abstractmethod
    def return_book(self, book):
        pass

    def __str__(self):
        return f"Member ID: {self._member_id}, Name: {self._name}, Borrowed Books: {[book.title for book in self.borrowed_books]}"

# 2. Subclasses: RegularMember and PremiumMember (Inheritance and Polymorphism)
class RegularMember(Member):
    def borrow_book(self, book):
        if len(self.borrowed_books) < 2:
            self.borrowed_books.append(book)
            print(f"{self._name} borrowed '{book.title}'.")
        else:
            print("Regular members can borrow only 2 books at a time.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self._name} returned '{book.title}'.")
        else:
            print("This book was not borrowed by the regular member.")

class PremiumMember(Member):
    def borrow_book(self, book):
        if len(self.borrowed_books) < 5:
            self.borrowed_books.append(book)
            print(f"{self._name} borrowed '{book.title}'.")
        else:
            print("Premium members can borrow only 5 books at a time.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self._name} returned '{book.title}'.")
        else:
            print("This book was not borrowed by the premium member.")

# 3. Book Class
class Book:
    def __init__(self, isbn, title, author, is_borrowed=False):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def __str__(self):
        return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Available: {'No' if self.is_borrowed else 'Yes'}"

# 4. Library Class (Encapsulating books and members)
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title}")

    def add_member(self, member):
        self.members.append(member)
        print(f"Added member: {member._name}")

    def borrow_book(self, member, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.is_borrowed:
                book.is_borrowed = True
                member.borrow_book(book)
                return
        print("Book is either unavailable or does not exist.")

    def return_book(self, member, isbn):
        for book in self.books:
            if book.isbn == isbn and book.is_borrowed:
                book.is_borrowed = False
                member.return_book(book)
                return
        print("This book was not borrowed or does not exist.")

    def list_books(self):
        for book in self.books:
            print(book)

    def list_members(self):
        for member in self.members:
            print(member)

# 5. Main System with Interaction
def main():
    print("Welcome to BRUMA'S Library System")
    library = Library()

    # Adding books
    library.add_book(Book("978", "Clean Code", "Wannabee Saka"))
    library.add_book(Book("979", "Design Patterns", "Cole Palmer"))
    library.add_book(Book("976", "Refactoring", "Martin Luther"))

    # Adding members
    member1 = RegularMember("M001", "Alice")
    member2 = PremiumMember("M002", "Bob")
    library.add_member(member1)
    library.add_member(member2)

    while True:
        print("\nChoose an action:")
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. List All Books")
        print("4. List All Members")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN to borrow: ")
            member = next((m for m in library.members if m._member_id == member_id), None)
            if member:
                library.borrow_book(member, isbn)
            else:
                print("Member not found.")
        elif choice == '2':
            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN to return: ")
            member = next((m for m in library.members if m._member_id == member_id), None)
            if member:
                library.return_book(member, isbn)
            else:
                print("Member not found.")
        elif choice == '3':
            library.list_books()
        elif choice == '4':
            library.list_members()
        elif choice == '5':
            print("Thank you for using BRUMA'S Library System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
