print("Lets check whether the Dude is Under Weight ? , Over Weight ? OR dude is Perfect!")
weight=float(input("Dude enter your weight in KG : "))
height=float(input("Dude enter yout height in M : "))

bmi=round(weight/height**2)

if bmi<18.5:
    print("Dude you are under weight, Eat somthing")
elif bmi>18.5 and bmi<25:
    print ("Dude You have a normal BMI ")  #normal means that there is no problem with it
elif bmi>25 and bmi<30 :
    print("Dude do some excercise you are over weight")
elif bmi>30 and bmi<35 :
    print ("Dude you are obse, i ment you are in red light... What you eat dude?")
else:
    print("Dude go hospital ")