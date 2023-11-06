print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
client_name = input('What is your name? ')

# TODO: Write code to ask the client his savings and save it to another variable.
client_savings = input('How much do you have in savings? ')

# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'appl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft. ")

print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.
def calc_shares(stk):
    if stk == 'amzn':
        num_shares = ["Amazon", amazon, round(int(client_savings) / amazon, 2)]
    elif stk == 'appl':
        num_shares = ["Apple", apple, round(int(client_savings) / apple, 2)]
    elif stk == 'fb':
        num_shares = ["Facebook", fb, round(int(client_savings) / fb, 2)]
    elif stk == 'goog':
        num_shares = ["Google", google, round(int(client_savings) / google, 2)]
    elif stk == 'msft':
        num_shares = ["Microsoft", msft, round(int(client_savings) / msft, 2)]
    else:
        stock = input ("You have not picked one of the available stocks. Type 'amzn' for Amazon, 'appl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft. ")
        num_shares = calc_shares(stock)
    return num_shares

share_info = calc_shares(stock)

print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:
print(f'{client_name} has ${client_savings} in savings, and {client_name} can buy {share_info[2]} share(s) of {share_info[0]} at the current price of ${share_info[1]}.')

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print()
