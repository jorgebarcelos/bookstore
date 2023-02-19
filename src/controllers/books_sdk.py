import sqlite3
from src.models.books import Book


def cursor():
    return sqlite3.connect('books.db').cursor()

db_cursor = cursor()
db_cursor.execute('CREATE TABLE IF NOT EXISTS books (title TEXT, pages INTEGER)')
db_cursor.connection.close()


def add_book(book):
    db_cursor = cursor()

    with db_cursor.connection:
        db_cursor.execute('INSERT INTO books VALUES (?, ?)', (book.title, book.pages))

    return db_cursor.lastrowid

def get_all_books():
    db_cursor = cursor()
    books_list = []

    with db_cursor.connection:
        for book in db_cursor.execute('SELECT * FROM books'):
            books_list.append(Book(book[0], book[1]))

        return books_list
    
def get_book_by_title(title):
    db_cursor = cursor()

    with db_cursor.connection:
        db_cursor.execute('SELECT * FROM books WHERE title=?', (title,))
    book_data = db_cursor.fetchone()
    
    if not book_data:
        return None
    return Book(book_data[0], book_data[1])

def update_book(book, new_title, new_pages):
    db_cursor = cursor()

    with db_cursor.connection:
        db_cursor.execute('UPDATE books SET title=?, pages=? WHERE title=? AND pages=?', (new_title, new_pages, book.title, book.pages))
    book = get_book_by_title(new_title)

    return book

def delete_book(book):
    db_cursor = cursor()

    with db_cursor.connection:
        db_cursor.execute('DELETE FROM books WHERE title=? AND pages=?', (book.title, book.pages))
    rows = db_cursor.rowcount
    
    return rows

