class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise ValueError("Book ID already exists")

        self.books[book_id] = {
            "title": title,
            "author": author,
            "status": "Available"
        }
    def borrow_book(self, book_id):
        if book_id not in self.books:
            raise KeyError("Book not found")

        if self.books[book_id]["status"] == "Borrowed":
            raise ValueError("Book already borrowed")

        self.books[book_id]["status"] = "Borrowed"

    def return_book(self, book_id):
        if book_id not in self.books:
            raise KeyError("Book not found")

        self.books[book_id]["status"] = "Available"
        
    def generate_report(self):
        lines = []
        header = "Book ID | Title | Author | Status"
        lines.append(header)

        for book_id, details in self.books.items():
            line = f"{book_id} | {details['title']} | {details['author']} | {details['status']}"
            lines.append(line)

        return "\n".join(lines)
