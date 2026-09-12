from book import Book


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def view_books(self):

        if len(self.books) == 0:
            print("No books available.")
            return

        for book in self.books:
            book.display()
            print("--------------------")

    def search_book(self, title):

        for book in self.books:

            if title.lower() in book.title.lower():
                return book

        return None

    def issue_book(self, title):

        book = self.search_book(title)

        if book is None:
            print("Book not found.")
            return

        if book.available:
            book.available = False
            print("Book issued successfully.")
        else:
            print("Book is already issued.")

    def return_book(self, title):

        book = self.search_book(title)

        if book is None:
            print("Book not found.")
            return

        if not book.available:
            book.available = True
            print("Book returned successfully.")
        else:
            print("Book is already available.")

    def delete_book(self, title):

        book = self.search_book(title)

        if book is None:
            print("Book not found.")
            return

        self.books.remove(book)

        print("Book deleted successfully.")

    def save_books(self):

        with open("books.txt", "w") as file:

            for book in self.books:

                status = "1" if book.available else "0"

                file.write(
                    book.title + "|" +
                    book.author + "|" +
                    str(book.price) + "|" +
                    status + "\n"
                )

    def load_books(self):

        try:

            with open("books.txt", "r") as file:

                for line in file:

                    line = line.strip()

                    if line == "":
                        continue

                    parts = line.split("|")

                    title = parts[0]
                    author = parts[1]
                    price = float(parts[2])
                    available = parts[3] == "1"

                    book = Book(
                        title,
                        author,
                        price,
                        available
                    )

                    self.books.append(book)

        except FileNotFoundError:

            pass