books_list = input().split("&")

while True:
    line = input()

    if line == "Done":
        print(", ".join(books_list))
        break
    
    args = line.split(" | ")
    command = args[0]

    if command == "Add Book":
        book = args[1]
        if book not in books_list:
            books_list.insert(0, book)

    elif command == "Take Book":
        book = args[1]
        if book in books_list:
            books_list.remove(book)
    
    elif command == "Swap Books":
        book1 = args[1]
        idx_book1 = books_list.index(book1)
        book2 = args[2]
        idx_book2 = books_list.index(book2)

        if book1 in books_list and book2 in books_list:
            books_list[idx_book1], books_list[idx_book2] = books_list[idx_book2], books_list[idx_book1]
            
    elif command == "Insert Book":
        book = args[1]
        if book not in books_list:
            books_list.append(book)
    
    elif command == "Check Book":
        idx = int(args[1])

        if 0 <= idx < len(books_list):
            print(books_list[idx])

