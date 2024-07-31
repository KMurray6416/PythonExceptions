    # Task 1

temperature_input = float(input("Please enter the temperature in Fahrenheit: "))

    # Task 2

def temperature_conversion(temp_input):
    try:
        return (temp_input - 32) * 5 / 9
    except ValueError:
        return "Please enter only numbers and decimals for conversion."
    
try:
    result = temperature_conversion(temperature_input)
    if result != temperature_conversion(temperature_input):
        raise Exception("Unexpected error happened during conversion!")
except Exception as x:
    print(f"Alert!: {x}")
else:
    print(f"The result of the conversion from Fahrenheit to Celsius is: {result:.2f} ")
finally:
    print("Thank you for choosing your # ! App for weather forecasts!!")
