password=input("Enter password to check strength")
if len(password)<6:
    strength="weak"
elif len(password)>=6 and len(password)<12:
    strength="Medium"
elif len(password)>12:
    strength="Hard"
print(strength)