import string
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase

while True:
    clear_screen()
    print("=== Caesar Cipher Program ===")
    
    # استقبال المدخلات من المستخدم
    message = input("Please type a message: ")
    number_shift = int(input("Enter a shift number: "))
    
    encrypted_message = ""
    
    # عملية التشفير
    for letter in message:
        if letter in alphabet_lower:
            original_position = alphabet_lower.index(letter)
            new_position = (original_position + number_shift) % 26
            encrypted_message += alphabet_lower[new_position]
        elif letter in alphabet_upper: 
            original_position = alphabet_upper.index(letter)
            new_position = (original_position + number_shift) % 26    
            encrypted_message += alphabet_upper[new_position]
        else:
            encrypted_message += letter
            
    # طباعة النتيجة
    print(f"\nHere is the encrypted message:\n*****\n{encrypted_message}\n*****\n")
    
    # سؤال المستخدم لو حابب يكمل أو يخرج
    restart = input("Do you want to encrypt another message? (yes/no): ").lower().strip()
    if restart != 'yes':
        print("\nThank you for using Caesar Cipher. Goodbye!")
        break