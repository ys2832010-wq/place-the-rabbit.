import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_screen()
    print("=== Friends Name Abbreviator ===\n")
    
    # 1. بناخد الأسماء وبنفصل بين كل صاحب والتاني بالفاصلة (وخلينا الاسم n سمول عشان نوحدها)
    user_input = input("Enter your friends' full names (First and Last) separated by a comma:\n(e.g., Youssef Ahmed, Ali Mohamed): ")
    
    # لو المستخدم داس إنتر من غير ما يكتب حاجة
    if not user_input.strip():
        print("You didn't enter any names!")
        input("\nPress Enter to try again...")
        continue
        
    friends_list = user_input.split(", ")
    abbreviated_names = []   
    
    for name in friends_list:
        # بنشيل أي مسافات زيادة في الأول أو الآخر بالـ strip
        name = name.strip() 
        
        # 2. الحل هنا: بنقسم الاسم الواحد بناءً على "المسافة" عشان نجيب الأول والأخير
        name_parts = name.split(" ")
        
        # التأكد إن الاسم فيه جزئين فعلاً عشان الكود ميضربش لو كتب اسم واحد بس
        if len(name_parts) >= 2:
            first_name = name_parts[0]
            last_name = name_parts[-1] # استخدام -1 بيكفل إنه يجيب آخر اسم دايماً
            
            first_initial = first_name[0].upper() # خليناها كابيتال عشان يبقى شكلها شيك
            last_initial = last_name[0].upper()
            
            abbreviation = f"{first_initial}.{last_initial}."
            abbreviated_names.append(abbreviation)
        else:
            # لو كتب اسم واحد بس بدون اسم عائلة
            if name: 
                abbreviations = f"{name[0].upper()}."
                abbreviated_names.append(abbreviations)

    print("\nAbbreviated Names:")
    print("*****************")
    for x in abbreviated_names:
        print(x)
    print("*****************")
    
    # سؤال إعادة التشغيل
    restart = input("\nDo you want to try another list? (yes/no): ").lower().strip()
    if restart != 'yes':
        print("\nThank you! Goodbye!")
        break