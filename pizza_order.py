#Dude this project is about pizza billing 

# small pizza =15$
# medium pizza =17$
# large pizza=20$

# Extra pepperonie on samll pizza = +3$
# Extra pepperonie on medium and large pizza = +5$
# Extra chees on pizza = +1$

# user will select the pizza by S , M or L


print("\nWelcome to the Dude's pizza shop!\n")

print("\nsmall pizza =15$,\nmedium pizza =17$,\nlarge pizza=20$,\n")

print("\nExtra pepperoni on small pizza = +3$, \nExtra pepperoni on medium and large pizza = +4$\nExtra cheese on pizza = +1$\n\n ")

#Taking user's order Dude 

size_of_pizza=str(input("\nEneter the size of the pizza S ,M or L = ")).upper()
extra_pepparoni=str(input("Want to add extra pepparoni ? Y or N = ")).upper()
extra_chees=str(input("Want to add extra chees ? Y or N = ")).upper()

if size_of_pizza!=("S"or"M"or"L") and  extra_pepparoni!=("Y"or"N") and extra_chees!=("Y"or"N") :
    print("Dude please Enter valide details")
else: 
    if size_of_pizza=="S" :
        bill=15
        if extra_pepparoni=="Y":
            bill+=3
            if extra_chees=="Y":
                bill+=1
                print(f"\n Your total amout is {bill}")
            else:
                print(f"\n Your total amout is {bill}")   
        else :
            bill=15
            print(f"\n Your total amout is {bill}")
    elif size_of_pizza=="M" :
        bill=17
        if extra_pepparoni=="Y":
            bill+=4
            if extra_chees=="Y":
                bill+=1
                print(f"\n Your total amout is {bill}")
            else:
                print(f"\n Your total amout is {bill}")
        else :
            bill=17
            print(f"\n Your total amout is {bill}")
    else :
        bill=20
        if extra_pepparoni=="Y":
            bill+=4
            if extra_chees=="Y":
                bill+=1
                print(f"\n Your total amout is {bill}")
            else:
                print(f"\n Your total amout is {bill}")
        else :
            bill=20        
            print(f"\n Your total amout is {bill}")        
                

# name = str(input("")).upper()
# if name!="ABHAY":
#     print("done")
# else:
#     print("not happening")