print("Welcome to Rollercoaster park !")

#takes dude's height
height=float(input("Enter your height in Foots: "))

#takes dude's age 
age=int(input ("Enter yout age : "))

#condition to check is dude is tall enough
if height>=5:
    print('You are tall enough for a roller coaster')

    #ok dude is tall enough, but is he 18 year old ? to check that added another condition
    if age>=18:
        print ('you can go on the ride now!')
    else:
        print ('Sorry, you must be at least 18 years old.')
else:
    print ('Sorry, you can\'t go on the roller coaster. You need to grow first.')
