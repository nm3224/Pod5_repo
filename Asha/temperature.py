#Asha Maurya - Week 2 - Challenge 2 - Converting temperatures

#Convert a temperature of 100 degrees fahrenheit to celsius and print
fahrenheit = 100
celsius_100 = (fahrenheit - 32) * 5.0/9.0
print(f'The temperature of {fahrenheit} Fahrenheit is equal to {celsius_100} Celsius.')

# Determine if the number is integer or float
if isinstance(celsius_100, int):
        print(f'{celsius_100} is an integer')
else:
    print(f'{celsius_100} is a float')

# Convert a temperature of 34.2 degrees fahrenheit to celsius and print
print(f'{(34.2 - 32) * 5.0/9.0} celsius is equal to 34.2 fahrenheit')

# Convert a temperature of 5 degrees celsius to fahrenheit and print
print(f'{(9.0/5.0 * 5) + 32} fahrenheit is equal to 5 celsius')

# What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
convert = (9.0/5.0 * 30.2) + 32
if convert > 85.1:
    print(f'30.2 celsius converted to {convert} fahrenheit is greater than 85.1 fahrenheit')
elif convert == 85.1:
    print(f'30.2 celsius converted to {convert} fahrenheit is equal to 85.1 fahrenheit')
else:
    print(f'30.2 celsius converted to {convert} fahrenheit is less than 85.1 fahrenheit')