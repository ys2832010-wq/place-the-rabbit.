basket=[["Appels","Bananas"],["Milk","Water"]]
numbers=[1,2,3,4,]
print(basket)
input("press enter to change the content.....")
print("Here is the updated basket")
basket[0].insert(0,"Oranges")
basket[0].insert(3,"Kiwis")
basket[1].remove("Water")
basket[1].insert(0,"Coffee")
basket[1].append("Tea")
basket.extend(numbers)
print(basket)