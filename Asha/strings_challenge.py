#Asha Maurya - Week 2 - Challenge 3 - Strings Practice

# 1. 3 ways to print multiple items
ingredient_1 = 'milk'
ingredient_2 = 'eggs'
ingredient_3 = 'flour'
ingredient_4 = 'sugar'

# 1.1 Print the 4 ingredients in a single print statement, as 4 separate strings (separated by commas)
print('Four simple ingredients can combine to make so many different things:','milk', ',','eggs',',', 'flour',',', 'sugar')

# 1.2 Print the 4 ingredients using string concatenation
# (make sure what you print out is legible-- add spaces and/or commas to your string so they don't all become one word!)
print('Four simple ingredients can combine to make so many different things: '+ingredient_1 + ',', ingredient_2+ ',',ingredient_3+ ',',ingredient_4)

# 1.3 Print out the 4 ingredients using an f-string
# (again make sure to add spaces and/or commas to make the printout make sense)
print(f'{ingredient_1}, {ingredient_2}, {ingredient_3}, {ingredient_4}')

# 2. String Methods
# 2.1 Save your f-string from step 1.3 as a variable called ingredients
ingredients = (f'Four simple ingredients can combine to make so many different things: {ingredient_1}, {ingredient_2}, {ingredient_3}, {ingredient_4}')

# 2.2 Uh oh, one of these ingredients isn't quite right. Use one of our string methods to replace 'milk' with 'butter'
# in a print statement
print(ingredients.replace('milk','butter'))

# When we use a string method in a print statement, does it change the string in our variable?
# 2.3 Use a string method to count the number of times that 'milk' appears in our string.
print('Milk appears', ingredients.count('milk'),'time(s)in this string')

# 2.4 Let's print out our `ingredients` variable again just to be sure.
print(ingredients)

# 'milk' is still in there! To save our changes to the string, we'll need to update the variable.
# 2.5 Update our `ingredients` variable using the replace method, the same way we printed it out in step 2.2

# print `ingredients` to make sure the change stuck this time.
ingredients = ingredients.replace('milk', 'butter')
print(ingredients)

# 2.6 That looks better. Let's make it official: print the ingredients list all-caps now that it's right.
print(ingredients.upper())

# 3 User Input/Type conversion
# 3.1 Let's get some user input. Create a variable called `activity`, that saves the user's input to the question:
# What is your favorite thing to do for fun?
activity = input('What is your favorite thing to do for fun? ')

# 3.2 Create a second variable called `frequency` that asks the user:
# Roughly how many times a week do you make time to <activity>? <-- use your `activity` variable in an f-string here
frequency = input(f'Roughly how many times a week do you make time to {activity}?')

# 3.3 When the user inputs a number, what data type is it saved as?
# Print out the _type_ of the `frequency` variable to check.
print(type(frequency))

# 3.4 Uncomment the print statements below, and use `type conversion` to fix the second one, allowing it to run
print('Research shows that making time for enjoyment actually makes you more focused.')
print(f'We recommend you {activity} at least {int(frequency) * 2} times a week!')
