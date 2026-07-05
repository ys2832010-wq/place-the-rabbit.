import os

# Initialize empty lists for owned books and future wishlist
library = []
wishlist = []

def clear_screen():
    """Clears the terminal screen based on the Operating System."""
    os.system("cls" if os.name == "nt" else "clear")

# ==========================================
# MAIN APPLICATION LOOP
# ==========================================
while True:
    clear_screen()
    print("========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1) View Library & Wishlist")
    print("2) Add Books to your Library")
    print("3) Add Books to your Wishlist")
    print("4) Move a Book from Wishlist to Library")
    print("5) Donate a Book from your Library")
    print("6) Exit Program")
    print("===============================================")
    
    choice = input("Select an option (1-6): ").strip()

    # Option 1: View Current Status
    if choice == "1":
        clear_screen()
        print("--- Current Status ---")
        print(f"Your Library: {library}")
        print(f"Your Wishlist: {wishlist}")
        input("\nPress Enter to return to menu...")

    # Option 2: Add Owned Books
    elif choice == "2":
        clear_screen()
        print("--- Add Books to Library ---")
        first_book = input("Write the name of a book you own: ").strip().lower()
        if first_book:
            library.append(first_book)
            
        second_book = input("Type another book title (or press Enter to skip): ").strip().lower()
        if second_book:
            library.append(second_book)
        
        print(f"\nUpdated Library: {library}")
        input("\nPress Enter to return to menu...")

    # Option 3: Add to Wishlist
    elif choice == "3":
        clear_screen()
        print("--- Add Books to Wishlist ---")
        future_first_book = input("Is there a book you would like to own in the future? ").strip().lower()
        if future_first_book:
            wishlist.append(future_first_book)
            
        future_second_book = input("Is there another book? (or press Enter to skip): ").strip().lower()
        if future_second_book:
            wishlist.append(future_second_book)
            
        print(f"\nUpdated Wishlist: {wishlist}")
        input("\nPress Enter to return to menu...")

    # Option 4: Transfer Acquired Book
    elif choice == "4":
        clear_screen()
        print("--- Wishlist to Library Transfer ---")
        if not wishlist:
            print("Your wishlist is currently empty!")
        else:
            print(f"Current Wishlist: {wishlist}")
            wishlist_done = input("Which book have you acquired? ").strip().lower()
            
            if wishlist_done in wishlist:
                wishlist.remove(wishlist_done)
                library.append(wishlist_done)
                print(f"\nSuccess! '{wishlist_done}' moved to your Library.")
            else:
                print(f"\nNotice: '{wishlist_done}' was not found in your wishlist.")
        input("\nPress Enter to return to menu...")

    # Option 5: Donate a Book
    elif choice == "5":
        clear_screen()
        print("--- Donate a Book ---")
        if not library:
            print("Your library is currently empty!")
        else:
            print(f"Current Library: {library}")
            donate = input("Which book would you like to donate? ").strip().lower()
            
            if donate in library:
                library.remove(donate)
                print(f"\nThank you! '{donate}' has been successfully donated.")
            else:
                print(f"\nNotice: '{donate}' was not found in your library.")
        input("\nPress Enter to return to menu...")

    # Option 6: Exit
    elif choice == "6":
        clear_screen()
        print("Thank you for using Library Management System. Goodbye!")
        break

    # Handle invalid menu choice
    else:
        print("\nInvalid choice. Please select a number between 1 and 6.")
        input("\nPress Enter to try again...")