print("welcome to the speed converter!")
miles = float(input("Enter the speed in miles: "))
conversion = 0.44704
total = round(miles * conversion, 2)
print(f"you're going {total} meters per second")