# converting 100 degrees Fahrenheit to degrees in Celsius to one decimal point, and print result
celsius_100 = round(((100 - 32) * 5 / 9), 1)
print(celsius_100)

# converting 0 degrees Fahrenheit to degrees in Celsius to one decimal point, and print result
celsius_0 = round(((0 - 32) * 5 / 9), 1)
print(celsius_0)

# converting 34.2 degrees Fahrenheit to degrees in celsius to one decimal point, and print result
print(round(((34.2 - 32) * 5/ 9), 1))

#converting 5 degrees Celsius to degrees in Fahrenheit to one decimal point, and print result
fahrenheit_5 = round((5 * 9 / 5 + 32), 1)
print(fahrenheit_5)

# converting 30.2 degrees Celsius to degrees in Fahrenheit to one decimal point, and print result
print(round(30.2 * 9 / 5 + 32, 1))

# function to convert Fahrenheit to Celsius
def fah_to_cels(fah):
    try:
        float(fah)
    except ValueError:
        print("The value must be an integer or a floating point number")
        return
    cels = round((float(fah) - 32) * 5 / 9, 1)
    print(f'{fah} degrees Fahrenheit is {cels} degrees Celsius')
    return cels

# ask for input of temperature in Fahrenheit
deg_fah = input("What degrees in Fahrenheit do you want to convert to Celsius? ")
# convert with fah_to_cels() function
fah_to_cels(deg_fah)

# function to convert Celsius to Fahrenheit
def cels_to_fah(cels):
    try:
        float(cels)
    except ValueError:
        print("The value must be an integer or a floating point number")
        return
    fah = round((float(cels) * 9 / 5 + 32), 1)
    print(f'{cels} degrees Celsius is {fah} degrees Fahrenheit')
    return fah

# ask for input of remperature in Celsius
deg_cels = input("What degrees in Celsius that you want to convert to Fahrenheit? ")
# convert with cels_to_fah() function
cels_to_fah(deg_cels)
