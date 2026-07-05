import os

# Clear the terminal screen based on the operating system
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Dictionary used to store all books
# Key   : ISBN
# Value : Book information (title, author, availability)
catalog = {}


# Add a new book to the catalog
def add_book():
    while True:

        # Collect book information from the user
        isbn = input("Enter ISBN: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")

        # Store the book information in the catalog
        catalog[isbn] = {
            'title': title,
            'author': author,
            'Available': True,
        }

        print(f"Book '{title}' by {author} added to the catalog with ISBN {isbn}.")

        # Ask the user if they want to add another book
        add_another = input("Do you want to add another book? (Y/N): ").lower()

        if add_another != "y":
            break

        # Clear the screen before adding another book
        clear_screen()


# Check out a book from the catalog
def check_out_book():
    while True:

        # Clear the screen for a cleaner interface
        clear_screen()

        # Get the ISBN of the book to check out
        isbn = input("Enter ISBN to check out: ")

        # Verify that the book exists in the catalog
        if isbn in catalog:

            # Check if the book is currently available
            if catalog[isbn]['Available']:
                catalog[isbn]['Available'] = False
                print(f"\nBook {catalog[isbn]['title']} checked out successfully!")
            else:
                print("\nSorry, the book is currently checked out.")
        else:
            print("\nBook not found!")

        # Ask the user if they want to check out another book
        choose = input("\nDo you want to check out another book (Y/N): ").lower()

        if choose != "y":
            break

        # Clear the screen before the next operation
        clear_screen()


# Return a checked-out book to the catalog
def check_in_book():
    while True:

        # Get the ISBN of the book to check in
        isbn = input("Enter ISBN to check in: ")

        # Verify that the book exists in the catalog
        if isbn in catalog:

            # Ensure the book is currently checked out
            if not catalog[isbn]['Available']:
                catalog[isbn]['Available'] = True
                print(f"\nBook {catalog[isbn]['title']} checked in successfully!")
            else:
                print("\nBook is not checked out!")
        else:
            print("\nBook not found!")

        # Ask the user if they want to check in another book
        choose = input("\nDo you want to check in another book? (Y/N): ").lower()

        # Clear the screen before the next operation
        clear_screen()

        if choose != 'y':
            break

        clear_screen()


# Display all books stored in the catalog
def list_books():
    while True:

        print("--- LIST BOOKS ---")

        # Display the details of each book
        for isbn in catalog:
            book_info = catalog[isbn]
            print(f"ISBN {isbn}, Title: {book_info['title']}, Author: {book_info['author']}, Available: {book_info['Available']}")

            # Ask the user whether to return to the main menu
            choose = input("Do you want to go back to the main menu? (Y/N): ").lower()

            if choose == 'y':
                break

            clear_screen()


# Main program loop
while True:

    # Display the main menu
    print("\n--- MAIN MENU ---")
    print("1. Add Book")
    print("2. Check Out Book")
    print("3. Check In Book")
    print("4. List Books")
    print("5. Exit")

    # Get the user's menu selection
    choice = input("Enter your choice (1-5): ")

    # Clear the screen before executing the selected option
    clear_screen()

    if choice == '1':
        add_book()

    elif choice == '2':
        check_out_book()

    elif choice == '3':
        check_in_book()

    elif choice == '4':
        list_books()

    elif choice == '5':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Try again")
        input("\nPress Enter to continue...")

        # Clear the screen before returning to the menu
        clear_screen()

