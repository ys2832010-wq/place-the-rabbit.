import os

# دالة لمسح الشاشة
def clear_screen():
    # لنظام ويندوز يستخدم 'cls' ولأنظمة لينكس وماك يستخدم 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

# 1) MAIN MENU - Initialize catalog
catalog = {}
    
# choice = 1 -> A (ADD BOOK)
def add_book():
    while True:
        # 2) ADD BOOK
        isbn = input("Enter ISBN: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")

        # Process: catalog[ISBN] = { ... }
        catalog[isbn] = {
            'title': title,
            'author': author,
            'Available':True,
        }
            
        print(f"Book '{title}' by {author} added to the catalog with ISBN {isbn}.")
        # Decision: Add another book?
        add_another = input("Do you want to add another book? (Y/N): ").lower()            
        if add_another != "y":
            break
        clear_screen() # مسح الشاشة بعد الإجابة
# choice = 2 -> B (CHECK OUT BOOK)
def check_out_book():
    while True:
        clear_screen() # مسح الشاشة للعودة للقائمة نظيفة
        # 3) CHECK OUT BOOK
        isbn = input("Enter ISBN to check out: ")

        # Search ISBN in catalog
        if isbn in catalog:
            # Decision: Status = 'Available'?
            if catalog[isbn]['Available']:
                catalog[isbn]['Available']=False
                print(f"\nBook {catalog[isbn]['title']} checked out successfully!")
            else:
                print("\nSorry, the book is currently checked out.")
        else:
            print("\nBook not found!")
    
        choose=input("\nDo you want to check out another book (Y/N): ").lower()
        if choose != "y":
            break # Return to Main Menu
        clear_screen() # مسح الشاشة بعد الإجابة
# choice = 3 -> C (CHECK IN BOOK)
def check_in_book():
    while True:
        # 4) CHECK IN BOOK
        
        isbn = input("Enter ISBN to check in: ")
        
        # Search ISBN in catalog
        if isbn in catalog:
            # Decision: Status = 'Checked Out'?
            if not catalog[isbn]['Available']:
                catalog[isbn]['Available'] = True
                print(f"\nBook {catalog[isbn]['title']} checked in successfully!")
            else:
                print("\nBook is not checked out!")
        else:
            print("\nBook not found!")
        
        choose=input("\nDo you want to chock in another book? (Y/N): ").lower()
        clear_screen() # مسح الشاشة بعد الإجابة
        if choose != 'y':
            break
        clear_screen() # مسح الشاشة بعد الإجابة
# choice = 4 -> D (LIST BOOKS)
def list_books():
    while True:
        # 5) LIST BOOKS
        print("--- LIST BOOKS ---")
        # For each ISBN in catalog Display: ISBN, Title, Author, Status
        for isbn in catalog:
            book_info=catalog[isbn]
            print(f"ISBN {isbn}, Title: {book_info['title']}, Author: {book_info['author']}, Available: {book_info['Available']}")
            choose=input("Do you want to go back to the main menu? (Y/N): ").lower()    
            if choose=='y':
                break
            clear_screen() # مسح الشاشة بعد الإجابة


while True:
    # Display Menu
    print("\n--- MAIN MENU ---")
    print("1. Add Book")
    print("2. Check Out Book")
    print("3. Check In Book")
    print("4. List Books")
    print("5. Exit")
    
    # Enter choice
    choice = input("Enter your choice (1-5): ")    
    # مسح الشاشة بعد اختيار الأمر وقبل الدخول في تفاصيله
    clear_screen()        
    if choice == '1':
        add_book()
        clear_screen() # مسح الشاشة بعد الإجابة
    elif choice == '2':
        check_out_book()
        clear_screen() # مسح الشاشة بعد الإجابة
    elif choice == '3':
        check_in_book()
        clear_screen() # مسح الشاشة بعد الإجابة
    elif choice == '4':
        list_books()
        clear_screen() # مسح الشاشة بعد الإجابة
    elif choice == '5':
        break
    else :
        print("Invalid choice. Try again")
        input("\nPress Enter to continue...")
        clear_screen()