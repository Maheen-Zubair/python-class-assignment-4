def get_valid_temperature():
    while True:
        try:
            value = float(input("Enter temperature in Fahrenheit: "))
            return value  
        except ValueError:
            print("Please enter a valid number!")

degrees_fahrenheit = get_valid_temperature()
degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0
print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")