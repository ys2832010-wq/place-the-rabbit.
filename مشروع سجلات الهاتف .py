import os

def clear_screen():
    """Clears the terminal screen based on the Operating System."""
    os.system("cls" if os.name == "nt" else "clear")

# High-level dictionary to store all contacts using their ID as a unique key
contacts = {}

# ==========================================
# MAIN APPLICATION LOOP
# ==========================================
while True:
    print("========== Contact Management ==========")
    print("1) Add a contact")
    print("2) View all contacts")
    print("3) Edit a contact")
    print("4) Exit")
    print("========================================")
    
    # Kept as string to prevent crashing if user presses Enter or types letters
    choice = input("\nPlease choose an option (1-4): ").strip()
    clear_screen() 
    
    # ------------------------------------------
    # OPTION 1: ADD A CONTACT
    # ------------------------------------------
    if choice == "1":
        print("--- Add a New Contact ---")
        user_id = input("Enter the contact ID: ").strip()
        
        # Check if ID already exists to prevent overwriting
        if user_id in contacts:
            print(f"\nNotice: ID '{user_id}' already exists. Use edit option to change it.")
        else:
            user_name = input("Please type a name: ").strip()
            phone_number = input("Please type a phone number: ").strip()
            
            # Using Nested Dictionary to store multiple details per ID
            contacts[user_id] = {
                "name": user_name,
                "phone": phone_number
            }
            print(f"\nMessage: '{user_name}' was added successfully...")
            
        input("\nPress Enter to return to menu...")
        clear_screen()

    # ------------------------------------------
    # OPTION 2: VIEW ALL CONTACTS
    # ------------------------------------------
    elif choice == "2":
        print("--- View All Contacts ---")
        if not contacts:
            print("Your contact list is currently empty.")
        else:
            # Loop through the dictionary and print beautifully
            for cid, info in contacts.items():
                print(f"ID: {cid} | Name: {info['name']} | Phone: {info['phone']}")
                
        input("\nPress Enter to continue...")
        clear_screen()        

    # ------------------------------------------
    # OPTION 3: EDIT A CONTACT
    # ------------------------------------------
    elif choice == "3":
        print("--- Edit an Existing Contact ---")
        id_to_edit = input("Please enter the ID to edit: ").strip()
        
        # Look for the ID key directly in the main contacts dictionary
        if id_to_edit in contacts:
            new_name = input("Please type a new name: ").strip()
            new_phone_number = input("Please type a new phone number: ").strip()
            
            # Update the sub-dictionary values directly
            contacts[id_to_edit]["name"] = new_name
            contacts[id_to_edit]["phone"] = new_phone_number
            
            print(f"\nMessage: ID '{id_to_edit}' was updated successfully to '{new_name}'...")
        else:
            print(f"\nSorry, ID '{id_to_edit}' was not found.")    
            
        input("\nPress Enter to return to menu...")
        clear_screen()

    # ------------------------------------------
    # OPTION 4: EXIT
    # ------------------------------------------
    elif choice == "4":
        print("Thank you for using Contact Management. Goodbye!")
        break
        
    else:
        print("Invalid selection. Please choose a number from 1 to 4.")
        input("\nPress Enter to try again...")
        clear_screen()