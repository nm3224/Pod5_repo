from book_class import *


class Booklist():
	def __init__(self):
		self.books = []
	
"""Add a Book object with the given title and author to the book list"""
def add(self, title, author):
		book = Book(title, author)
		self.books.append(book)
	
"""Return the number of books currently in the booklist"""
def count_books(self):
		return len(self.books)

"""Remove a book from the book list"""
def remove_title(self, title):
		for book in self.books:
			if book.title == title:
				self.books.remove(book)

"""Print out all titles currently in the book list"""
def display_titles(self):
	book_titles = []
	for book in self.books:
		book_titles.append(book.title)
		book_titles.sort()

	for book in book_titles:
		print(book)


