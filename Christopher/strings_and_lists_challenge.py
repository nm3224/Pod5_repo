# You run a startup media company called Ripple Media
# It's typical when you hire a new employee in your company, to setup an email id for them

employee_name = 'Ash Rahman'

# You have decided the format of the email should be: Ash Rahman -> ash.rahman@ripplemedia.com
# Let's write some code that converts a name into an email id that matches this format
# 1.1 TODO: Let's save the lowercase version of the employee_name in a new variable 'lower_name' (use a string method to lower the name)
lowercase_name = employee_name.lower()
print(f'lowercase_name: {lowercase_name}')
# 1.2 TODO: We want to separate the first name and last name and save it in a variable 'names_list' (use a string method to split the string into a list)
# Split the string into a list
names_list = lowercase_name.split() # default is to split on whitespace
print(f'names_list: {names_list}')
# 1.3 TODO: We want to join the first name and last name with a '.' and save it in a variable called 'joined_names' (use a string method to join the list into a new string)
joined_names = '.'.join(names_list)
print(f'joined_names: {joined_names}')
# 1.4 TODO: We want to add '@ripplemedia.com' to the end of the string inside joined_names and save it in a variable 'email' (use an f-string to combine the username with the email domain)
email = f'{joined_names}@ripplemedia.com'
print(email)