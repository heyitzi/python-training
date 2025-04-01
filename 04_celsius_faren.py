def temp_converter(temperature, unit):
    if unit == 1:
        fahrenheit = round((temperature * 9 / 5) + 32, 2)
        return f"{temperature}°C are {fahrenheit}°F"
    else:
        celsius = round((temperature - 32) * 5 / 9, 2)
        return f"{temperature}°F are {celsius}°C"
    
user_temp = input("What is the temperature? ")
user_unit = input("What unit are you converting from: choose 1 for celsius or 2 for farenheit? ")

print(temp_converter(int(user_temp), int(user_unit)))