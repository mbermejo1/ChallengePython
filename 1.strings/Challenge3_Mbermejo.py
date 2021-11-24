print("Welcome to temperature converter.")
temperature = float(input("input the temperature fahrenheit: "))
celsius = round((temperature - 32) * 5/9, 4)
kelvin = round((temperature - 32) * 5/9 + 273.15, 4)
print(f"""
      \n {temperature} fahrenheit
      \n {celsius} celsius
      \n {kelvin} kelvin""")