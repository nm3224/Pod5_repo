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
user_name = input("What is your name?")
print()

# TODO: Write code to ask the client his savings and save it to another variable.
user_savings = input ("How much do you have in savings? ")
print()

# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

# '''
# Your code should look like this:

savings_int = int (user_savings)

if stock == "amzn": 
    #savings divided by stock value
    num_stocks = savings_int / amazon
    stock_price = amazon
elif stock == "aapl":
    num_stocks = savings_int / apple
    stock_price = apple
elif stock == "fb":
    num_stocks = savings_int / fb
    stock_price = fb
elif stock == "goog":
    num_stocks = savings_int / google
    stock_price = google
elif stock == "msft":
    num_stocks = savings_int / msft
    stock_price = msft
else:
    print ('Not once of the big ones.')

print("Challenge 3.2.3: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print()
print (f'{user_name} has {user_savings} in savings and they can buy {num_stocks} shares of {stock} at the current price of {stock_price}.')
