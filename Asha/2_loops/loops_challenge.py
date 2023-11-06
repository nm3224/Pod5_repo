
# QUESTION 1: For loops with list

# Let's start simple, and build up from there.

# 1.1: Write a for loop that prints out each day in the `days` variable above.

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

for day in days:
    print(day)

# 1.2: Now, instead of printing out the day, let's ask the user what their favorite thing to do is on that day of the week. (Make sure to use an f-string so that the user knows which day they're being asked about.)

# 1.3: We should keep track of the user's favorite things to do so that we can print them out all together.

# ABOVE your for loop, create a new empty list to hold the user's favorite activities.

# 1.4: Now, back in your for loop, append each of the user's answers into your new list.
# Print out the list after your loop to check if it got populated correctly.

# 1.5: After your first loop, let's create a new one. As an example, let's say the user's favorite thing to do on mondays is plan their week. This time, we want the output to be something like this:
# 'On Mondays, your favorite activity is to plan your week.'

# We need information from both lists! Let's use the `range` function to loop through the indexes of the items in the lists (this will work because the lists are the same length).

# Each time through this new loop, use the index number to index into each of your lists for the data you need to print out.# Take a look back at the code you just wrote. Look at how much it does!

# Often, programmers will be given large tasks, and it's our responsibility to be able to break it down into smaller pieces. We did the above piece by piece, but think about what the prompt might have been to get us there.

# Maybe: Write a program that asks the user about their favorite thing to do each day of the week.

# Afterward, print out for the user each of their favorite daily activities.

# Would this larger task have felt doable without breaking it down into steps?
# Is it clear what needs to be done?
# Try to break down the steps required for this second loop challenge.


activities = []
for day in days:
    activity = input(f'What is your favorite activity on {day}?')
    activities.append(activity)
print(activities)

for index in range(len(days)):
    print(f'On {days[index]} your favorite activity is {activities[index]}.')

for day in days:
    temperature = int(input(f'What is the temperature on {day}?'))
    if temperature < 50:
        print('Wear a jacket')
    elif temperature > 50 and temperature < 65:
        print('Wear a sweater')
    else:
        print ('Put on some sunscreen.')

# QUESTION 3: For loops with the range function
# Write a program that asks the user how many times they would like to be wished happy birthday.
# Then, print out happy birthday that number of times.

num_wishes = int(input('How many times would you liked to be wished Happy Birthday?')) #ask user input and convert to integer
for i in range(num_wishes):
    print('Happy Birthday!')


# QUESTION 4: While loops

# Write a program that asks the user what temperature it is outside. While the temperature is below 65, tell the user to wear a sweater. Once the temperature is over 65, stop looping, and tell the user that Spring has sprung!


temperature = int(input('What is the temperature outside?')) #ask user input
while (temperature) < 65: #create the test for the while
    print("Please put on a sweater.")
    temperature = int(input('What is the temperature outside?')) #ask user input again
print("Spring has sprung!")
  

# NOTE: remember, if you accidentally create an infinite while loop, it's ok! Go into the command line and hit control + C to stop the program. No harm done to your computer (: