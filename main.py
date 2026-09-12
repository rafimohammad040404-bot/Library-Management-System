from book import Book
from library import Library


library = Library()

library.load_books()


while True:

    print("\n================================")
    print("     LIBRARY MANAGEMENT SYSTEM")
    print("================================")

    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":

        title = input("Enter book title: ")
        author = input("Enter author: ")

        try:
            price = float(input("Enter price: "))
        except ValueError:
            print("Please enter a valid price.")
            continue

        book = Book(title, author, price)

        library.add_book(book)

        library.save_books()

        print("Book added successfully.")


    elif choice == "2":

        library.view_books()


    elif choice == "3":

        title = input("Enter book title: ")

        book = library.search_book(title)

        if book:
            book.display()
        else:
            print("Book not found.")


    elif choice == "4":

        title = input("Enter book title: ")

        library.issue_book(title)

        library.save_books()


    elif choice == "5":

        title = input("Enter book title: ")

        library.return_book(title)

        library.save_books()


    elif choice == "6":

        title = input("Enter book title: ")

        library.delete_book(title)

        library.save_books()


    elif choice == "7":

        library.save_books()

        print("Thank you for using the Library Management System.")
        break


    else:

        print("Invalid choice. Please try again.")