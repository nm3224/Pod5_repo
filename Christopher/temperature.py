""" 
The formula for converting between fahrenheit and celsius is to first subtract 32, then multiply by 5/9. Can you do the following in python?

1. Convert a temperature of 100 degrees fahrenheit to celsius
    * Save this to a variable called `celsius_100`, and use `print()` to print out the value
    * Is the resulting temperature you get an integer or float? How do you know?
2. Convert a temperature of 0 degrees fahrenheit to celsius
    * Save this to a variable called `celsius_0`, and use `print()` to print out the value
3. Convert a temperature of 34.2 degrees fahrenheit to celsius
    * Do this one all in one print statement **without** saving any variables
"""
# Convert a temperature of 100 degrees fahrenheit to celsius
temperature_F = 100 # degrees Fahrenheit
celsius_100 = (temperature_F - 32) * 5/9 # formula for converting fahrenheit to celsius
print(celsius_100) # print out the value
# Print the type of the variable
print("celsius_100 is a", type(celsius_100)) # print out the type of the variable
# Convert a temperature of 0 degrees fahrenheit to celsius
temperature_F = 0 # degrees Fahrenheit
celsius_0 = (temperature_F - 32) * 5/9 # formula for converting fahrenheit to celsius
print(celsius_0) # print out the value
# Convert a temperature of 34.2 degrees fahrenheit to celsius and print it with one print statement
print((34.2 - 32) * 5/9) # print out the value with one print statement

""" 
4. Convert a temperature of 5 degrees celsius to fahrenheit?
5. What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
"""
temperature_C = 5 # degrees Celsius
fahrenheit_5 = (temperature_C * 9/5) + 32 # formula for converting celsius to fahrenheit
# What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
temperature_C = 30.2 # degrees Celsius
fahrenheit_30 = (temperature_C * 9/5) + 32 # formula for converting celsius to fahrenheit
print("30.2 degrees celsius is", fahrenheit_30, "degrees fahrenheit") # print out the value
temperature_F = 85.1 # degrees Fahrenheit
# If/else statement to determine which temperature is hotter and print out the result
if fahrenheit_30 > temperature_F: 
    print("30.2 degrees celsius is hotter than 85.1 degrees fahrenheit")
else:
    print("85.1 degrees fahrenheit is hotter than 30.2 degrees celsius")