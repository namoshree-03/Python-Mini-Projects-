class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity
    def display_book_info(self):
        print(f"ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Available Quantity: {self.quantity}")
    def check_availability(self):
        return self.quantity > 0
    def update_quantity(self, quantity):
        self.quantity += quantity
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []
    def display_user_info(self):
        print(f"User ID: {self.user_id}")
        print(f"Name: {self.name}")
    def borrow_book(self, book):
        if book.check_availability():
            book.update_quantity(-1)
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is not available.")
    def return_book(self, book):
        if book in self.borrowed_books:
            book.update_quantity(1)
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")
    def view_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f" - {book.title}")
        else:
            print(f"{self.name} has not borrowed any books.")
class Library:
    def __init__(self):
        self.books = []
        self.users = []
    def add_book(self, book):
        self.books.append(book)
    def register_user(self, user):
        if any(curr_user.user_id == user.user_id for curr_user in self.users):
            print(f"User with ID {user.user_id} is already registered.")
        else:
            self.users.append(user)
            print(f"User '{user.name}' registered successfully.")
    def search_book_by_title(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if found_books:
            print(f"Books found with title '{title}':")
            for book in found_books:
                book.display_book_info()
        else:
            print(f"No books found with title '{title}'.")
    def search_book_by_author(self, author):
        found_books = [book for book in self.books if book.author.lower() == author.lower()]
        if found_books:
            print(f"Books found by author '{author}':")
            for book in found_books:
                book.display_book_info()
        else:
            print(f"No books found by author '{author}'.")
    def list_all_books(self):
        if self.books:
            print("List of all books in the library:")
            for book in self.books:
                book.display_book_info()
        else:
            print("No books available in the library.")
    def add_new_book(self):
        book_id = int(input("Enter book ID: "))
        if any(book.book_id == book_id for book in self.books):
            print(f"Book with ID {book_id} already exists.")
            return
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        quantity = int(input("Enter book quantity: "))
        new_book = Book(book_id, title, author, quantity)
        self.add_book(new_book)
        print(f"New book '{title}' added to the library.")
    def main():
        library = Library()
        book1 = Book(1, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 5)
        book2 = Book(2, "The Hobbit", "J.R.R. Tolkien", 3)
        book3 = Book(3, "1984", "George Orwell", 4)
        library.add_book(book1)
        library.add_book(book2)
        library.add_book(book3)

        while True:
            print("\n Welcome to the Library Management System")
            print("1. Register User")
            print("2. Add New Book")
            print("3. Search Book by Title")
            print("4. Search Book by Author")
            print("5. List All Books")
            print("6. Borrow Book")
            print("7. Return Book")
            print("8. View Borrowed Books")
            print("9. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                user_id = int(input("Enter User ID: "))
                name = input("Enter User Name: ")
                new_user = User(user_id, name)
                library.register_user(new_user)
            elif choice == '2':
                library.add_new_book()
            elif choice == '3':
                title = input("Enter book title to search: ")
                library.search_book_by_title(title)
            elif choice == '4':
                author = input("Enter author name to search: ")
                library.search_book_by_author(author)
            elif choice == '5':
                library.list_all_books()
            elif choice == '6':
                user_id = int(input("Enter your User ID: "))
                user = next((u for u in library.users if u.user_id == user_id), None)
                if user:
                    book_title = input("Enter book title to borrow: ")
                    book = next((b for b in library.books if b.title.lower() == book_title.lower()), None)
                    if book:
                        user.borrow_book(book)
                    else:
                        print(f"Book '{book_title}' not found.")
                else:
                    print("User not registered.")
            elif choice == '7':
                user_id = int(input("Enter your User ID: "))
                user = next((u for u in library.users if u.user_id == user_id), None)
                if user:
                    book_title = input("Enter book title to return: ")
                    book = next((b for b in user.borrowed_books if b.title.lower() == book_title.lower()), None)
                    if book:
                        user.return_book(book)
                    else:
                        print(f"You did not borrow '{book_title}'.")
                else:
                    print("User not registered.")
            elif choice == '8':
                user_id = int(input("Enter your User ID: "))
                user = next((u for u in library.users if u.user_id == user_id), None)
                if user:
                    user.view_borrowed_books()
                else:
                    print("User not registered.")
            elif choice == '9':
                print("Exiting the Library Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
if __name__ == "__main__":
    Library.main()



