from book_class import Book


class Booklist():
	def __init__(self):
		"""Initialize the empty book list"""
		self.books = [] # initialize the books attribute as an empty list

	def add(self, title, author):
		"""Add a Book object with the given title and author to the book list"""
		book = Book(title, author) # create a Book object
		self.books.append(book) # add the book to the book list

	def count_books(self):
		"""Return the number of books currently in the booklist"""
		return len(self.books) # pass the books[] list to the len() function to get the number of books in the list

	def remove_title(self, title):
		"""Remove a book from the book from the booklist by its title"""
		# this method must remove any books matching the input title, therefore, you must loop through the books list
		for book in self.books:
			if book.title == title:
				self.books.remove(book)
		return
		
		    
	def display_titles(self):
		"""Print out all titles currently in the book list"""
		book_titles = [] # initialize an empty list to store the titles of the books
		for book in self.books:
				book_titles.append(book.title) # append the title of each book to the book_titles list
		book_titles.sort() # sort the book_titles list
		for book in book_titles:
			print(book)
	def is_empty(self):
		"""Return True if the book list is empty, False if not"""
		pass
