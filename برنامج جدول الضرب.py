print("*** Welcom to the multiplication table ***")
numper=int(input("Enter a number: "))
for x in range(1,13):
    result=numper*x
    print(f"{numper} x {x} = {result}")
