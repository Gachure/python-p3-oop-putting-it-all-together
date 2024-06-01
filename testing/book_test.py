# testing/book_test.py
import pytest
from lib.book import Book

def test_book_creation():
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", 180, 10.99)
    assert book.title == "The Great Gatsby"
    assert book.author == "F. Scott Fitzgerald"
    assert book.pages == 180
    assert book.price == 10.99

def test_book_price_positive():
    book = Book("1984", "George Orwell", 328, 15.99)
    with pytest.raises(ValueError):
        book.price = -5

def test_book_summary():
    book = Book("The Catcher in the Rye", "J.D. Salinger", 214, 7.99)
    assert book.summary() == "'The Catcher in the Rye' by J.D. Salinger, 214 pages - $7.99"
