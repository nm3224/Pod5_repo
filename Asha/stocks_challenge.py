print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
user_name = input('What is your name?')
# TODO: Write code to ask the client his name and save it to a variable.
user_savings = input ('how much do you have in savings?')
# TODO: Write code to ask the client his savings and save it to another variable.
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? \n Type: \n amzn for Amazon \n aapl for Apple \n fb for Facebook \n goog for Google \n msft for Microsoft \n")
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.
#Your code should look like this:

savings_int = int(user_savings) #cast the savings string as an integer

if stock == "amzn": #verify the price of amazon
    num_stocks = savings_int / amazon
    stock_price = amazon
    stock = "Amazon"
elif stock == "aapl": #verify the price of aapl
    num_stocks = savings_int / apple
    stock_price = apple
    stock = "Apple"
elif stock == "fb ": #verify the price of facebook
    num_stocks = savings_int / fb
    stock_price = fb
    stock = "Facebook"
elif stock == "goog": #verify the price of aapl
    num_stocks = savings_int / google
    stock_price = google
    stock = "Google"
elif stock == "msft": #verify the price of aapl
    num_stocks = savings_int / msft 
    stock_price = msft
    stock = "Microsft"
else:
    print('Please choose another stock from the list and enter the code')

print("Challenge 3.2.3: Output for the user the result")
# # TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# # Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

# print()
print(f'{user_name} has ${user_savings} in savings, therefore {num_stocks} shares of {stock} can be purchased at the current price of ${stock_price}.')