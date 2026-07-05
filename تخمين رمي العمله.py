import os
import random

def clear_screen():
    """
    دالة لمسح الشاشة في الـ Terminal لتنظيم العرض.
    تعمل على جميع الأنظمة (Windows, Mac, Linux).
    """
    os.system('cls' if os.name == 'nt' else 'clear')

# --- بداية اللعبة الرئيسي ---
clear_screen()
print("====================================")
print("  Welcome to Coin Guessing Game!    ")
print("====================================\n")

# حلقة تكرار لضمان إدخال خيار صحيح (1 أو 2)
while True:
    print("Choose a method to toss the coin:")
    print("1. Using random.random()")
    print("2. Using random.randint()")
    
    choose_random = input("\nEnter your choice (1 or 2): ").strip()
    
    if choose_random in ["1", "2"]:
        break  # الخيار صحيح، اخرج من اللوب وابدأ اللعبة
    else:
        clear_screen()
        print("❌ Invalid choice. Please select either 1 or 2.\n")

# مسح الشاشة بعد اختيار الطريقة لبدء التخمين بشكل منظم
clear_screen()

# --- منطق رمي العملة (Coin Toss Logic) ---
if choose_random == "1":
    # random() تعطي رقم بين 0.0 و 1.0
    choose_1 = random.random()
    if choose_1 >= 0.5:
        computer_result = "heads"
    else:
        computer_result = "tails"    
else:
    # randint(0, 1) تعطي إما 0 أو 1
    choose_2 = random.randint(0, 1)
    if choose_2 == 0:
        computer_result = "heads"
    else:
        computer_result = "tails"   

# --- مرحلة التخمين (Guessing Phase) ---
print("The coin has been tossed! 🪙\n")

while True:
    guess = input("Enter your Guess (Heads or Tails): ").strip().lower()
    if guess in ["heads", "tails"]:
        break
    print("❌ Please enter a valid guess ('Heads' or 'Tails').")

print("\n====================================")
# المقارنة (النتيجة محولة لـ lower تلقائياً لمنع الأخطاء)
if guess == computer_result:
    print("🎉 Congratulations! You Win! 🎉") 
else:
    print(f"😢 You lost! The computer's result was: {computer_result.capitalize()}")
print("====================================")