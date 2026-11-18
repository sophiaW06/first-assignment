# Creating an empty list to store all the books for the database
books = []
# Keeps programme running until user inputs exit
# Menu to reappear after every action to allow for quicker and easier user interaction
while True:
    # DISPLAYING MAIN MENU
    print("\n======= GREENWOOD LIBRARY MANAGEMENT SYSTEM =======")
    print("1. ADD BOOK")
    print("2. BORROW BOOK")
    print("3. RETURN BOOK")
    print("4. SHOW AVAILABLE BOOKS")
    print("5. SEARCH BOOK BY TITLE")
    print("6. EXIT")
    # User query
    option = input("Select an option: ")
    #Checking which option user inputs 
    if option == "1":
        # ADD BOOK LOGIC HERE. 
        print("ADD BOOK")
        book_id = input("Enter book ID: ")  #stores ID entered by user
        title = input("Enter book title: ") #stores book title
        author = input("Enter author name: ") #stores author name
        #input used, rather than print, so that user can provide selective information, rather than providing limit variety of hardwired options
        #creating dictionary:
        book = {
            "id": book_id,
            "title": title,
            "author": author,
            "status": "AVAILABLE"   #will be automatically set to available until book is borrowed
        }
        # Adding books to the 'books' list from earlier
        books.append(book)
        # CONFIRMATION THAT BOOK WAS ADDED
        print("Book added successfully!")
    elif option == "2":
        # BORROW BOOK LOGIC HERE
        print("BORROW BOOK")
        book_id = input("Enter book ID: ") #requesting book ID 
        found = False 
        for book in books:
            if book["id"] == book_id:
                found = True 
                if book["status"] == "AVAILABLE": # == marks comparison of values
                    book["status"] = "BORROWED"      #changing book status  # singular = to assign new value upon book being borrowed 
                    print("Book borrowed successfully, enjoy!")
                else:
                    print("This book is unavailable.")

                break 
            if found == False:
                print("Book not found.")
    elif option == "3":
        # RETURN BOOK LOGIC HERE
        print("RETURN BOOK")
        book_id = input("Enter book ID: ") # user asked for book id 
        found = False #Boolean variable to check if the book exists 
        for book in books: #for loop begins #searches through book list
            if book["id"] == book_id:
                found = True 
                if book["status"] == "BORROWED":
                    book["status"] = "AVAILABLE"  #returning status of book back to available 
                    print("Successfully returned book!")
                else:
                    print("This book has not been borrowed from the library. Take out book for attempting again.")
                break #ending for loop
        if found == False:
                print("Book not found. Try again?")
    elif option == "4":
        # SHOW AVAILABLE BOOK LOGIC HERE
        print("SHOW AVAILABLE BOOKS")
        found = False             #Boolean variable created
        for book in books:            #for loop implemented
            if book["status"] == "AVAILABLE":    # == checks matching value to "AVAILABLE"
                print("Book ID:", book["id"]) #using print to display values to user, clear display for interface
                print("Title:", book["title"])
                print("Author:", book["author"])
                found = True 
        if found == False:
            print("Sorry, no books are currently available.")   # In case of scenario where books aren't added to the system by user
    elif option == "5":
        print("SEARCH BOOK BY TITLE")
        search_title = input("Enter book title:")
        found = False  #system assumes a book has not yet been found
        for book in books:
            #.lower() makes the search case-insensitive so users can input any variation of the title
            if search_title.lower() in book["title"].lower():
                 #to record that a matching book was identified
                 found = True

                 #to display book information
                 print("Book found!")
                 print("Book ID;", book["id"])
                 print("Title:", book["title"])
                 print("Author:", book["author"])
                 print("Status:", book["status"])
                # to display message if no matching books exist / are found
            if found == False:
                 print("Unable to find books matching that title. Try again?")
        
   
    elif option == "6":
        # TO DISPLAY EXIT MESSAGE
        print("EXITING LIBRARY.")
        # TO STOP WHILE LOOP
        break   
    else:
        # INVALID MENU SELECTIONS
        # To prevent users from inputting random cmds
        print("Invalid option. Please try again.")