temperature=float(input("enter temperature: "))
unit=input("enter unit (C for Celsius / F for Fahrenheit) ")
if unit.upper()=="C":
    fahrenheit=(temperature*9/5)+32
    print(f"{temperature}°C = {fahrenheit:.2f}°F")
elif unit.upper() == "F":
    celsius = (temperature - 32) * 5/9
    print(f"{temperature}°F = {celsius:.2f}°C")
else:
    print("Invalid unit entered! Please enter C or F.")
