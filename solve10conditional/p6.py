distance=float(input("Enter distance(in km)"))
if distance<3:
    transport="Walk"
elif distance>=3 and distance<=15:
    transport="Bike"
elif distance>=15:
    transport="Car"
print(transport)