from book_class import *

class Booklist():
	def __init__(self):
		self.books = []

#Add a Book object with the given title and author to the book list			
	def add(self,title,author):
		book = Book(title, author)
		self.books.append(book)

# Method counts the book object and returns the total
	def count_books(self):
		return (len(self.books))

# Method loop through book object and removes the matching title

	def remove_title(self, title):
		for book in self.books:
			if book.title == title:
				self.books.remove(book)
	
# Method creates a blank list, loop through book object and add populates those titles in alphabetical order, prints

	def display_titles(self):	
			alpha_titles = []
			for book in self.books:
				alpha_titles.append(book.title)
				alpha_titles.sort()
			print(alpha_titles)