"""
Created on Mon Mar 6, 2017

author: Amon Millner
To discuss inheritance using an example of selling my kids old books
"""


class Book(object):
    """A system for selling used books

    Attributes:
        title: A string representing the title of the book.
        author: A string containing the name of the author.
        pages: An integer representing the pages the book has.
        type: A string describing the type of book (comic, talking, coloring).
        language: A dictionary showing the book's language as a string.
        year: The year that the book was published.
        previous_owners: An integer representing the # of previous owners.
    """

    base_price = 0
    language_bonus = {'english': 0, 'spanish': 5, 'french': 5, 'multi': 7}

    def __init__(self, title, author, pages, language, previous_owners):
        """Return a new Book object."""
        self.title = title
        self.author = author
        self.pages = pages
        self.language = language
        self.previous_owners = previous_owners

    def sale_price(self):
        """Return the sale price for this book as a float amount."""
        return (self.base_price + self.pages / 5 +
                self.language_bonus.get(self.language, 0) -
                self.previous_owners * 2)


class ComicBook(Book):  # inherits from the Book class

    def __init__(self, title, author, pages, language, previous_owners):
        """Return a new ComicBook object."""
        self.title = title
        self.author = author
        self.pages = pages
        self.language = language
        self.previous_owners = previous_owners
        self.base_price = 2


class TalkingBook(Book):  # inherits from the Book class

    def __init__(self, title, author, pages, language, previous_owners):
        """Return a new ComicBook object."""
        self.title = title
        self.author = author
        self.pages = pages
        self.language = language
        self.previous_owners = previous_owners
        self.base_price = 6

class TalkingBook(Book):  # inherits from the Book class

    def __init__(self, title, author, pages, language, previous_owners):
        """Return a new ComicBook object."""
        self.title = title
        self.author = author
        self.pages = pages
        self.language = language
        self.previous_owners = previous_owners
        self.base_price = 6

    def sale_price(self):
        """Return the sale price for this book as a float amount."""
        if self.author == 'Dr. Seuss':
            return (10 + self.base_price +
                     self.language_bonus.get(self.language, 0))
        else:
            return (self.base_price + self.pages / 5 +
                    self.language_bonus.get(self.language, 0) -
                    self.previous_owners * 2)


if __name__ == '__main__':
    CB = Book('five monkeys', 'Oliver Steele', 10, 'english', 0)
    TB = Book('cinco monos', 'Amon Millner', 10, 'spanish', 0)
    DS = Book('One Fish', 'Dr. Seuss', 15, 'english', 100)
    # print(CB.sale_price())
    # print(TB.sale_price())
    print(DS.sale_price())
