FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    C = (fahrenheit - 32) * 5/9
    return C


def convert_to_fahrenheit(celsius):
    F = (celsius * 9/5) + 32
    return F
user = int(input("Enter the temperature to convert: "))
cel_fah = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

if cel_fah == "c":
    print(f"{user}°c is {convert_to_fahrenheit(user)}°F")
elif cel_fah == "f":
    convert_to_celsius(user)
    print(f"{user}°F is {convert_to_celsius(user)}°C")
else:
    print("enter a correct answer")
