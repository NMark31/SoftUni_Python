favourite_book = input()
book_counter = 0

while True:
    book_name = input()
  
    if book_name == favourite_book:
        print(f"You checked {book_counter} books and found it.")
        break

    if book_name == 'No More Books':
        print(f'The book you search is not here!\nYou checked {book_counter} books.')
        break
    
    book_counter += 1