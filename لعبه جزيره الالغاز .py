import os

def clear_screen():
    """
    دالة لمسح الشاشة في الـ Terminal لتنظيم العرض.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

# حلقة التكرار الرئيسية للعبة كاملة
while True:
    clear_screen()
    print("""
██╗    ██╗███████╗██╗      ██████╗  ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗     ███╗   ███╗██╗   ██╗
██║    ██║██╔════╝██║     ██╔════╝ ██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗    ████╗ ████║╚██╗ ██╔╝
██║ █╗ ██║█████╗  ██║     ██║      ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║    ██╔████╔██║ ╚████╔╝ 
██║███╗██║██╔══╝  ██║     ██║      ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║    ██║╚██╔╝██║  ╚██╔╝  
╚███╔███╔╝███████╗███████╗╚██████╗ ╚██████╔╝██║ ╚═╝ ██║███████╗        ██║   ╚██████╔╝    ██║ ╚═╝ ██║   ██║   
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚══════╝        ╚═╝    ╚═════╝     ╚═╝     ╚═╝   ╚═╝   
""")
    print("You must find the lost treasure, hero! 💪\n")

    # --- الخطوة الأولى: اختيار الباب ---
    door = input("You have two doors 🚪🚪: [White] and [Black]\nWhat do you choose? -> ").strip().lower()

    if door == "white":
        clear_screen()
        print("🔥 GOOOOD CHOICE! You passed the first test.\n")
        
        # --- الخطوة الثانية: اختيار الصندوق ---
        box = input("Now you have three boxes 🎁 in front of you: [Red], [Green], and [Blue]\nWhich box do you choose? -> ").strip().lower()
        
        clear_screen()
        print("====================================")
        if box == "red":
            print("🕷️ Oops! You opened a box full of spiders!\n💀 GAME OVER.")
            input("\nPress Enter to try again... 🔄") # بتثبت الشاشة عشان يلحق يقرأ سبب الخسارة
        elif box == "green":
            print("🐍 Oh no! You opened a box full of venomous snakes!\n💀 GAME OVER.")
            input("\nPress Enter to try again... 🔄")
        elif box == "blue":
            print("💰 CONGRATULATIONS! The lost treasure has been found! 🎉")
            print("🏆 You win, hero!")
            print("====================================")
            break # هنا الفوز! بنقفل الـ loop واللعبة بتنتهي بنجاح
        else:
            print(f"💁 That choice '{box}' is not available.\n❌ Please stick to the available choices.")
            input("\nPress Enter to try again... 🔄")
        print("====================================")

    elif door == "black":
        clear_screen()
        print("====================================")
        print("🐊 Oh my God! You opened a door full of hungry crocodiles!\n💀 GAME OVER.")
        print("====================================")
        input("\nPress Enter to try again... 🔄")
    else:
        clear_screen()
        print("====================================")
        print(f"💁 That choice '{door}' is not available.\n❌ Please stick to the available choices.")
        print("====================================")
        input("\nPress Enter to try again... 🔄")