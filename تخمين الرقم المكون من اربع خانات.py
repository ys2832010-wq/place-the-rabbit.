pin=int(input("Enter a 4 digit PIN code:\n"))
import random
code=random.randint(1000,9999)
if  len(str(pin))!= 4 :
    print("Please Enter a 4 digits") 
elif pin== code :
    print("Congratulations, PIN code match")
else :
    print(f"Failure! PIN code did not match.\nThe computer generated this PIN: {code}")
    input("press Enter to exit")
    