import os

# الحلقة الرئيسية لاستمرار اللعبة (Main Game Loop)
while True:
    # تنظيف الشاشة عند بدء اللعبة
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("=== Welcome to Place the Rabbit ===")
    
    # 1. إنشاء مصفوفة الحقل المكونة من 3 صفوف و 3 أعمدة
    field = [
        ["☘️", "☘️", "☘️"],
        ["☘️", "☘️", "☘️"],
        ["☘️", "☘️", "☘️"]
    ]
    
    # عرض الحقل بشكل منظم في البداية
    for row in field:
        print("  ".join(row))
        
    print("\nWhere should the rabbit 🐇 go?")
    row_column = input("Please choose a row and a column (e.g., 13 for Row 1, Col 3): ")
    
    # 2. التحقق من المدخلات لضمان عدم حدوث خطأ (Validation)
    if len(row_column) != 2 or not row_column.isdigit():
        print("\n❌ Invalid input! Please enter exactly two numbers (e.g., 22).")
        input("\nPress Enter to try again...")
        continue
        
    # تحويل المدخلات إلى أرقام صفوف وأعمدة
    row = int(row_column[0])
    column = int(row_column[1])
    
    # التحقق من أن الأرقام في النطاق الصحيح (من 1 إلى 3)
    if row not in [1, 2, 3] or column not in [1, 2, 3]:
        print("\n❌ Out of bounds! Rows and columns must be between 1 and 3.")
        input("\nPress Enter to try again...")
        continue
        
    # 3. وضع الأرنب في المكان المحدد بعد تعديل الـ Index (يطرح 1 لأن العد يبدأ من 0)
    field[row - 1][column - 1] = "🐇"
    
    # تنظيف الشاشة لعرض النتيجة النهائية بنظافة
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n✨ Success! The rabbit has been placed:\n")
    
    # عرض الحقل النهائي بعد حركة الأرنب
    for row in field:
        print("  ".join(row))
        
    # 4. سؤال المستخدم لو حابب يلعب لفة ثانية
    play_again = input("\nDo you want to place the rabbit again? (yes/no): ").lower()
    if play_again != "yes" and play_again != "y":
        print("\nGoodbye! 🐇👋")
        break