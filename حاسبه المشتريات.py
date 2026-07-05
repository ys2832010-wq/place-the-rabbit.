number=[]
item=[]
print("***** Welcom to IShop calculator *****\n")
basket=int(input("How many items are there in your baskat today? "))
print("\n")
print("Let's get to counting them....")
for x in range(basket):
    items=input(f"Please tell me the name of the item mumber {x+1} ").lower()
    item.append(items)
    price=float(input(f"What is the price of {items}\n$"))
    number.append(price)
see_basket=input("Would you like to see your entire basket items?yes or no? ").lower()
if see_basket=="yes":
    print(" ".join(item))
much=input("Would you like to see how much it'll cost? yes or no ").lower()
if much=="yes" :
    print(sum(number))