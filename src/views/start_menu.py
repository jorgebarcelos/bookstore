def print_menu():
    message = '''
        [1] Show all books
        [2] Add a book
        [3] Update a book
        [4] Detele a book
        [5] Exit
    '''
    print(message)
    command = int(input('Command: '))
    return command
