import os
import random

# مصفوفة رسومات الـ ASCII للعبة Hangman
HANGMAN_ASCII = [
    '''
  +---+
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]

# قائمة الكلمات المتاحة للتخمين
words = ["good", "bad", "ugly"]

# الحلقة الرئيسية لاستمرار اللعبة وإعادة اللعب (Main Game Loop)
while True:
    # تنظيف الشاشة عند بدء جيم جديد
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # 1. اختيار كلمة عشوائية وتجهيز متغيرات اللعبة
    random_letter = random.choice(words)
    display = ["_"] * len(random_letter)
    lives = 6
    guessed_letters = []

    print("=== WELCOME TO HANGMAN GAME ===")
    print(HANGMAN_ASCII[0])
    print("Word to guess: " + " ".join(display))
    print(f"You have {lives} tries left.\n")

    # حلقة التخمين داخل الجيم الحالي (Gameplay Loop)
    while "_" in display and lives > 0:
        guessed = input("Please guess a letter: ").lower()
        
        # تنظيف الشاشة لتحديث العرض للمستخدم
        os.system('cls' if os.name == 'nt' else 'clear')

        # التحقق مما إذا كان الحرف تم تخمينه من قبل
        if guessed in guessed_letters:
            print(HANGMAN_ASCII[6 - lives])
            print(f"You already guessed '{guessed}'. Try a different letter.")
            print(" ".join(display))
            print(f"You have {lives} more tries\n")
            continue

        # إضافة الحرف المكتوب إلى قائمة الحروف المخمنة
        guessed_letters.append(guessed)

        # إذا كان التخمين خاطئاً (خصم محاولة وعرض الرسمة المناسبة)
        if guessed not in random_letter:
            lives -= 1
            print(HANGMAN_ASCII[6 - lives])
            print(f"Wrong guess! '{guessed}' is not in the word.")
        # إذا كان التخمين صحيحاً (استبدال الشرطة بالحرف)
        else:
            print(HANGMAN_ASCII[6 - lives])
            print(f"Good job! '{guessed}' is in the word.")
            for position in range(len(random_letter)):
                if random_letter[position] == guessed:
                    display[position] = guessed

        # عرض حالة الكلمة الحالية وعدد المحاولات المتبقية
        print(" ".join(display))
        print(f"You have {lives} more tries\n")

    # التحقق من نتيجة الجيم (فوز أو خسارة)
    if lives == 0:
        print("\n========================")
        print("      YOU LOST! 💀      ")
        print(f"The word was: {random_letter}")
        print("========================")
    else:
        print("\n************************")
        print("      YOU WIN! 🎉       ")
        print("************************")

    # سؤال المستخدم إذا كان يريد اللعب مجدداً
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes" and play_again != "y":
        print("\nThank you for playing! See you next time. 👋")
        break