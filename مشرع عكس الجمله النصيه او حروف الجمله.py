text=input("Enter text \n")
choose=input("To reverse the words in the sentence, press 1.\nTo reverse the letters of the sentence, press 2.\n")
if choose=="1":
    texts=text.split()
    reversed_text=" ".join(texts[::-1])
    print(reversed_text)
elif choose=="2":
    reversed_text=text[::-1]
    print(reversed_text)
else :
    print("Soory, Please type number 1 or 2") 