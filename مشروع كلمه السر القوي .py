import random  
import string
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# اللوب هنا عشان نضمن إن الإدخال صحيح
while True:
    clear_screen()
    print("*** Welcome to the Password Generator! ***\n")
    
    len_password = int(input("Enter the total number of characters in the password: "))
    len_password_letters = int(input("Enter the number of letters in the password: "))
    len_password_numbers = int(input("Enter the number of numbers in the password: "))
    len_password_symbols = int(input("Enter the number of symbols in the password: "))
    
    total_password = len_password_letters + len_password_numbers + len_password_symbols
    
    # لو الأرقام غلط، البرنامج مش هيقفل، هيمسح الشاشة ويخليه يصلح غلطته
    if len_password != total_password: 
        print("\n[!] Invalid input. The sum of letters, numbers, and symbols doesn't match the total length.")
        input("\nPress Enter to try again...")
        continue # يرجع يعيد الإدخال من الأول
        
    # طالما وصل هنا.. يبقى الأرقام صحيحة 100%، نولد الباسورد ونقفل علطول
    password_letters = random.choices(string.ascii_letters, k=len_password_letters)
    password_numbers = random.choices(string.digits, k=len_password_numbers)
    password_symbols = random.choices(string.punctuation, k=len_password_symbols)
    
    password = password_letters + password_numbers + password_symbols
    random.shuffle(password)
    
    final_password = "".join(password)
    
    print("\n-----------------------------------")
    print(f"Generated password: {final_password}")
    print("-----------------------------------")
    print("\nThank you for using Password Generator. Goodbye!")
    
    break # الخروج التلقائي فوراً لأن المهمة تمت بنجاح!