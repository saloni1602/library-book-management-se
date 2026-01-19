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

if __name__ == "__main__":
    unittest.main()
