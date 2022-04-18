#Asha Maurya - Week 2 - Challenge 1 - Meals

# Define variable for Meal
# print('1.1: Create a variable called `meal`, and save a string describing what you had for lunch in it')
meal = 'I ate Lentils with Rice for lunch today.'

# Print variable for Meal
# print('1.2: Print the meal variable')
print(meal)

# Update definition of variable for Meal, then print
# print('1.3: Update the meal variable to be a string describing what you want for dinner. print it out again')
meal = 'I would like to eat a Baked Sweet Potato for dinner.'
print(meal)

# print('2: How old is Google?')
# # 2.1: Google was founded in 1993. The current year is 2022. Create a variable called google_age, and use subraction
# # to figure out how old Google is
# # ex: my_age = current_year - birth_year
google_birth = 1993
current_year = 2022
age = current_year - google_birth
print(age)

# # 2.2: Using an f-string, print out a sentence about Google's age. Make sure to include your variable in the f-string!
age_years= f'Google is {age} years old.'
print(age_years)

# # 2.3 How many _months_ old is Google? Create a new variable google_age_months, and use multiplication to figure it out,
# # then print a new f-string with the info.
# # (Assume 12 months for each year, you don't need to check which month they started)
age_months = f'Google is {age*12} months old.'
print(age_months)


# print('3.1: The line of code below is commented out because it produces many SyntaxErrors.')
# print('Fix the problem and turn the comment back into regular Python code')
# #completion message = 'Completed the first Python challenge!
completion_message = 'Completed the first Python challenge!'

# # 3.2 What were the syntax errors that you fixed? print out a quick explanation of each one.
error = 'There were two errors: \
\n(1) Added an underscore to the declared name of the variable \
\n(2) Added missing single quote at the end of the variable definition'
print(error)

# print('3.3: Turn the comment below back into regular Python code')
print(completion_message)