print("Dude we are checking whether the give year is leap year or not")
year = int(input("Enter the year : "))
if ((year%4==0 and year%100!=0) or year%400==0):
  print(f"{year} is a Leap Year")
else:
  print(f"{year} is Not A Leap Year")