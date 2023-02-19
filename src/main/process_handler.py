from .constructor.introduction_process import introduction_process
from src.controllers import books_sdk
from src.models.books import Book 

def start():
    while True:
        command = introduction_process()

        if command == 1:
            for book in books_sdk.get_all_books():
                print(book)

        elif command == 2:
            print('Enter the book title: \n')
            title = input()
            print('Enter the numbet of pages: \n')
            pages = int(input())

            book = Book(title, pages)
            books_sdk.add_book(book)

        elif command == 3:
            print('What is the current title?: ')
            title = input()

            print('What is the current number of pages?: ')
            pages = input()

            book = Book(title, pages)

            print('What is the new title?: ')
            new_title = input()

            print('What is the new pages?: ')
            new_pages = input()

            books_sdk.update_book(book, new_title, new_pages)

        elif command == 4:
            print('What is the current title?: ')
            title = input()

            print('What is the current number of pages?: ')
            pages = input()

            book = Book(title, pages)
            books_sdk.delete_book(book)
            
        elif command == 5:
            exit()
        else:
            print(f'Command {command} not found')