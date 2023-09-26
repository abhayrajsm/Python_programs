print("\nwelcome to the motoGP track race Dude\n")
age=int(input("whats your age Dude : "))
height=int(input("\nEnter your height in 'CM' Dude :"))
if height>=120 :
    print('\n"shhh you are tall guy"\n')
    if age>15 and age < 18 : 
        bill=5
        print(" You to pay 5$ for the entry,\n")
    elif age>18 and age<23:
        bill=7
        print("you have to pay 7$ for the entry Dude,\n") 
    else :
        bill=10
        print("Dude you have to pay 10$ for the entry,\n")

    photos=input("dude you want photos ? per pic 3$ Y or N : ")
    if photos.upper() =="Y":
        bill+=3
        print(f"\n I gotch you!  Total {bill}$ dude. \n")
    else :
        print(f"\n ok Dude total is {bill}$ , Thank you! \n")        
else:
    print("\ngrow tall dude! only tall people can ride the bike")