color=[]
add_color=input("Add the first color you like:\n")
color.append(add_color)
add_more_color=input("Do you want to add more colors? Yes or No?\n").lower()
if add_more_color=="yes" :
    add_tow_color=input("Add colors you like are:\n")
    color.append(add_tow_color)
    print(f"The color your like are:\n{color}")
elif add_more_color=="no":
    print(f"The color your like are:\n{color}")
else :
    print("invalid selecotion")