# USER
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = self.address
        print('The email {} has been changed to {}'.format(self.email, self.address))
    def __repr__(self):
        print('User {}, email: {}, books read: {}'.format(self.name, self.email, self.books))

    def __eq__(self, User):
        if self.name == User.name and self.email == User.email:
          self = User

    def read_book(self, book, rating=None):
      self.books[book] = rating
    
    def get_average_rating(self):
      x = 0
      y = 0
      for bugs in self.books.values:
        x += bugs
        y += 1
      return x/y

# BOOK
class Book(object):
  def __init__(self, title, isbn):
    self.title = title
    self.isbn = isbn
    self.rating = []
  def get_title(self):
    return self.title
  def get_isbn(self):
    return self.isbn
  def set_isbn(self, new_isbn):
    self.isbn == new_isbn
    print('This book\'s({}) ISBN has been updated').format(self.name)
  def add_rating(self, rating):
    if rating <= 4 and rating >= 0:
      (self.rating).append(rating)
    else:
      print('Invalid Rating')
  def __eq__(self, Book):
    if self.title == Book.title and self.isbn == Book.isbn:
      self = Book
  def get_average_rating(self):
    a = 0
    b = 0
    for big_bois in self.rating:
      a += big_bois
      b += 1
    return a/b
  def __hash__(self):
    return hash((self.title, self.isbn))

# BOOK-SUBCLASS 'FICTION'
class Fiction(Book):
  def __init__(self, title, isbn, author):
    self.author = author
  def get_author(self):
    return self.author
  def __repr__(self):
    return '{} by {}'.format(self.title, self.author)
# BOOK-SUBCLASS 'NON FICTION'
class Non_Fiction(Book):
  def __init__(self, title, isbn, subject, level):
    self.subject = subject
    self.level = level
  def get_subject(self):
    return self.subject
  def get_level(self):
    return self.level
  def __repr__(self):
    return '{}, a {} manual on {}'.format(self.title, self.level, self.subject)
# THE TOMERATER
class TomeRater():
  def __init__(self):
    self.user = {}
    self.books = {}
  
  # CHECK**
  def create_book(self, title, isbn):
    cow = Book.__init__(self, title, isbn)
    return cow

  def create_novel(self, title, isbn, author):
    sugoi = Fiction.__init__(self, title, isbn, author)
    return sugoi
  
  def create_non_fiction(self, title, isbn, subject, level):
    cacoi = Non_Fiction.__init__(self,title,isbn,subject,level)
    return cacoi
  def add_book_to_user(self, book, email, rating=None):
    if self.users[email] == None:
      print('No user with email {}'.format(email))
    else:
      User.read_book(self, book, rating=None)
      Book.add_rating(self, rating=None)
      if book in self.books:
        self.books[book] += 1
      else:
        self.book[book] = 1
  def add_user(self, name, email, books=None):
    User.__init__(self,name, email)
    for caca in books:
      add_book_to_user(self, caca, email, rating=None)
  # ANALYSIS AND STUFF

  def print_catalog(self):
    for c in self.books.keys:
      print(c)
  def print_users(self):
    for d in self.users:
      print(d)
  def most_read_book(self):
    max(self.books, key=self.books.get)
  def highest_rated_book(self):
    f = 0
    for e in self.books:
      g = Book.get_average_rating(e)
      if g > f:
        f = g
    print(f)
  def most_positive_user(self):
    h = 0
    for j in self.users:
      i = User.get_average_rating(j)
      if i > h:
        h = i
# HAD A SUPER TIGHT SCHEDULE SO HAD TO RUSH THROUGH THIS CODE COULDN'T TEST HOPE THIS IS ENOUGH
