from datetime import date
today=date.today()
age=int(input("Enter your age:"))
if age>=18 and today.weekday()==2:
    print("Wednesday discount $2..Adult ticket price will be $10")
elif age>=18:
    print("Adult ticket price will be $10")
else:
    print("Children ticket price is $8")
