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

if __name__ == "__main__":
    unittest.main()
