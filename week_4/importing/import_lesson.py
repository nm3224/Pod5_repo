'''
....................................................................................................
..,::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::,..
..,**********************************************************************************************,..
..,++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++,..
..,++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++,..
..,+++*%S###*++++++++++++++++++++++++++++++++++++++++++++++++++++++++*??*++++++++++++++++++++++++,..
..,+*S#%#@@#*++++++++++++++++++++++++++++++++++++++++++++++++++?%%?++S@@#*+++++++++++++++++++++++,..
..,%@@*+@@@%++++++++++++++++++++++++++++++++++++++++++++++++++?@@@?++?##S++++++++++++++++++++++++,..
..:@@?+?@@@*+*???*???*+*???++++%###????*++++*?%%?*+++???**??**S@@@?**???*++???**??*++++++*?%?*???,..
..:#@?+S@@#++#@@@#@@@#%#@@@S+++#@@@S#@@#*++%@@#S@#*+*@@@##@@#?@@@S?+S@@@*+*@@@@@@@@S+++*S@@#S@@@@:..
..,*?**@@@%+?@@@S*%@@@S*%@@@*+*@@@%+*#@@%+S@@#+*#@%*%@@@?*%#%?@@@?+*@@@S++%@@@%*S@@#++?@@@?++@@@S,..
..,+++%@@@*+S@@@*+S@@#++%@@#++%@@@*++#@@%%@@@*+*@@#%@@@#+++++S@@#++?@@@?++#@@S++#@@S+*@@@S++?@@@?,..
..,+++#@@#+*@@@S+*@@@%+*@@@%++#@@S++*@@@?@@@S++*@@**@@@%++++*@@@%++S@@#++?@@@?+*@@@?+%@@@*++S@@#*,..
..,++*@@@%+?@@@?+?@@@*+?@@@*+?@@@?++#@@#?@@@%++%@S+%@@@*++++%@@@*+*@@@%++S@@@*+%@@#++S@@@++*@@@S+,..
..,++%@@@*+S@@#++#@@#++%@@@%S@@@@%?#@@#**@@@#%S@#*+#@@#+++++%@@@S%#@@@#%#@@@S++S@@@%S@@@@S%#@@@?+,..
..,++S@@S+*#@@%+*#@@%++*S@@@S@@@##@@#%*++?S@@@#?++*#@@?+++++*S@@#S*%#@@#S@@@?++*#@@#%*%#@@#@@@#++,..
..,++***+++***+++***+++++**+?@@@?+**+++++++***+++++***++++++++**+++++**++***+++++**++++*S%%@@@%++,..
..,+++++++++++++++++++++++++S@@#+++++++++++++++++++++++++++++++++++++++++++++++++++++++#S+%@@@*++,..
..,***********************+*@@@%+******************************************************#@@@@@?+**,..
..,::::::::::::::::::::::::;*+;:::::::::::::::::::::::::::::::::::::::::::::::::::::::::+**+;::::,..
....................................................................................................






Outline the class agenda for today
    1. Importing your own functions from other python scripts
    2. Feel comfortable calling functions that you've created and imported
    3. Importing existing Python libraries
    4. Using functions from imported libraries
    

**** Review what is a function?


A block of code that, when called (running the function), executes a particular action

- Reduce the amount of code needed for your script
- helps organize your work, allows you to think of your program as a series of procedures or steps

                    schedule = []

                    abbr = ['mon', 'wednes', 'fri',]

                    to_do = [' morning - buy groceries', ' evening - meal prep']


                    def fix_my_week():
                        for day in abbr:
                            for task in to_do:
                                schedule.append((day + 'day').title() + task)

                    fix_my_week()
                    print(schedule)


 
    

**** What is importing?


Importing is the process of bringing in some code/functions that are beyond the standard python libary. Think of the standard python libary as the default
package, if you want to add more functionality you'll have to import it to your script





A library is a bundle of python code. What we have been using so far in the course comes from the Python Standard Library. 

print()
.upper()
.title()
.append()

When importing, we are bringing more functionality to our code. Since we have previously written functions and other Python libraries at our disposal, importing allows us to use
them

                                1. Importing your own functions from other python scripts

Lets use two files for this demonstration. In one file we have a few functions from the previous lecture. 


    <<custom_functions.py>>

    Display the custom_functions.py file




   <<importing_functions.py>> 

The syntax for importing is to write the command 'import' at the beginning of your script along with what we are importing.

import only 'say_hello', run a few examples 

            From custom_functions import say_hello 

    

            say_hello('Yusuf')
            say_hello('Tyler') 
 
    then run 
        
            print(word)  , in custom_functions word='hello'

We need to import all the functions and variables from, so we must Change import to 

            from custom_functions import *

            print(word)

capitalize 'word' with 'cap_this(phrase)'

            cap_this(word)


run interaction() with 3 possible inputs
    > with yes, no, and bad entry

Explain default parameter 
    say_hello_stranger(name='there')



                3. Importing existing python libraries & 4. Using functions from imported libraries


Lets import two entire existing libraries. 


os - stands for operating system. It allows us to run command line funcitons (ls, cd, dir) from within our python script

                import os

                print(os.getlogin()) # Get user login name

                print(os.system("dir")) # lists the system directory 



                comment-out print commands

numpy - python library that adds a lot of mathematical functionality. Very useful for working with numerical data. We do however have to import it in order
to utilize it

without importing, we get the error code "not defined". Our script does not have any reference to numpy because we did not import it.

                Import numpy

                Import numpy as np   Importing a library with an alias. Long long library name to 'cool'

                from numpy import *  Wildcard, from numpy import all. We'll see more examples of this shortly


With numpy now properly imported to my current script, I can now use the mean() function


num_list = [10, 5, 144, 7, 64]

list_avg = np.mean(num_list)

            def without_numpy_average(list):
                total = 0
                for num in list:
                    total = total + num
                avg = total / len(list)
                return avg
                





************ IF THERE IS TIME, use Fahrenheit to celcius example *****************



Add to <<custom_functions.py>>


                def fahrenheit_to_celcius(temp):
                    celsius = (temp - 32) * 5/9
                    return celsius


when calling function in <<import_functions.py>> no need to change the import syntax at the top of the page, the asterisk or wildcard catches all functions, 
and imports


                converted_temp = fahrenheit_to_celsius(70)
                print(converted_temp)

***********************************************************************************




Recap:

- how to import and call functions separated across 2 different files
- Importing additional libraries in python, like os and numpy
- how to import specific functions, and how to import all functions from libraries/modules


this makes our code more modular. Compartmentalizing our code into separate pieces that work together

'''
