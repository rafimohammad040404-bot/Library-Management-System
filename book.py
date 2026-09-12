class Book:

    def __init__(self, title, author, price, available=True):
        self.title = title
        self.author = author
        self.price = price
        self.available = available

    def display(self):

        if self.available:
            status = "Available"
        else:
            status = "Issued"

        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Status:", status)