FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    C = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return C


def convert_to_fahrenheit(celsius):
    F = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return F


user = int(input("Enter the temperature to convert: "))
cel_fah = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

if cel_fah == "c":
    converted_to_fah = convert_to_fahrenheit(user)
    print(f"{user}°c is {converted_to_fah}°F")
elif cel_fah == "f":
    converted_cel = convert_to_celsius(user)
    print(f"{user}°F is {converted_to_cel}°C")
else:
    print("enter a correct answer")
