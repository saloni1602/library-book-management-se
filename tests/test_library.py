import unittest
from src.library import Library

class TestSprint1(unittest.TestCase):

    def test_add_book_success(self):
        lib = Library()
        lib.add_book("B1", "Clean Code", "Robert Martin")
        self.assertIn("B1", lib.books)

    def test_add_duplicate_book_raises_error(self):
        lib = Library()
        lib.add_book("B1", "Clean Code", "Robert Martin")
        with self.assertRaises(ValueError):
            lib.add_book("B1", "Refactoring", "Martin Fowler")



class TestSprint2(unittest.TestCase):

    def test_borrow_available_book(self):
        lib = Library()
        lib.add_book("B2", "Design Patterns", "GoF")
        lib.borrow_book("B2")
        self.assertEqual(lib.books["B2"]["status"], "Borrowed")

    def test_borrow_unavailable_book_raises_error(self):
        lib = Library()
        lib.add_book("B2", "Design Patterns", "GoF")
        lib.borrow_book("B2")
        with self.assertRaises(ValueError):
            lib.borrow_book("B2")

    def test_return_book(self):
        lib = Library()
        lib.add_book("B3", "Refactoring", "Martin Fowler")
        lib.borrow_book("B3")
        lib.return_book("B3")
        self.assertEqual(lib.books["B3"]["status"], "Available")
        
class TestSprint3(unittest.TestCase):

    def test_generate_report_contains_header(self):
        lib = Library()
        report = lib.generate_report()
        self.assertIn("Book ID", report)
        self.assertIn("Title", report)
        self.assertIn("Author", report)
        self.assertIn("Status", report)

    def test_generate_report_contains_book_entry(self):
        lib = Library()
        lib.add_book("B10", "Clean Architecture", "Robert Martin")
        report = lib.generate_report()
        self.assertIn("B10", report)
        self.assertIn("Clean Architecture", report)
        self.assertIn("Robert Martin", report)
        self.assertIn("Available", report)

if __name__ == "__main__":
    unittest.main()
