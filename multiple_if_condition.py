print("\nwelcome to the motoGP track race Dude\n")
age=int(input("whats your age Dude : "))
height=int(input("\nEnter your height in 'CM' Dude :"))
if height>=120 :
    print('\n"shhh you are tall guy"\n')
    if age>15 and age < 18 : 
        print(" You to pay 5$ for the entry,\n")
    elif age>18 and age<23:
        print("you have to pay 7$ for the entry Dude,\n") 
    else :
        print("Dude you have to pay 10$ for the entry,\n")

    photos=input("dude you want photos ? per pic 3$ Y or N : ")
    if photos.upper() =="Y":
        print("\n I gotch you ! \n")
    else :
        print("\nok Dude Thank you!\n")        
else:
    print("\ngrow tall dude! only tall people can ride the bike")