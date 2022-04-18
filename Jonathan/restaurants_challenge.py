print("Challenge: Favourite Restaurants")

print()

print("Question 1")

'''
Below is a dictionary consisting of details of 1 restaurant fetched from Yelp.

Go through the dictionary and print out the following 3 pieces of information about the restaurant:
1. The latitude and longitude of Four Barrel Coffee
2. The complete address of Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
3. The website of Four Barrel Coffee
'''


restaurant = {
    "name": "Four Barrel Coffee",
    "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
    "latitude": 37.7670169511878,
    "longitude": -122.42184275,
    "city": "San Francisco",
    "country": "US",
    "address2": "",
    "address3": "",
    "state": "CA",
    "address1": "375 Valencia St",
    "zip_code": "94103",
    "distance": 1604.23,
    "transactions": ["pickup", "delivery"]
}

print(restaurant)

# TODO: Write code to print the latitude and longitude of Four Barrel Coffee.
print()
print(restaurant["latitude"], restaurant["longitude"])

# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
print()
print(f'{restaurant["address1"]}, {restaurant["city"]}, {restaurant["state"]} {restaurant["zip_code"]}')

# TODO: Write code to print the URL of the website of Four Barrel Coffee.
print()
print(restaurant["url"])

print()
print("Question 2")

# TODO: Choose 3 of your most favourite restaurants in NYC, and create a dictionary for each of them with the following key-value pairs:
#         1. name : name of the resturant (string)
#         2. address: address of the restaurant (string)
#         3. favourite_dish: your favourite thing to order at the restaurant (string)

# TODO: Print each dictionary

# The dictionary for each restaurant should look something like this


restaurant_1  = {
    "name": "Shake Shack",
    "address" : "160 Berry Street, Brooklyn, NY 11249",
    "favourite_dish" : "Avocado Bacon Burger"
}


restaurant_2  = {
    "name": "Sweetgreen",
    "address" : "8 E. 18th Street, New York, NY 10003",
    "favourite_dish" : "Crispy Chicken Salad"
}


restaurant_3  = {
    "name": "Black Forest Brookyln",
    "address" : "733 Fulton Street, Brooklyn, NY 11217",
    "favourite_dish" : "Chicken and Waffles"
}


print()

print("Question 3")

# Imagine that any 1 of your most favourite restaurants stopped serving your favourite dish there.
# Remove the 'favourite_dish' key value pair from that restaurant's dictionary


# TODO: Remove the 'favourite_dish' key-value pair from one of your 3 restaurants
restaurant_1.pop("favourite_dish")

# TODO: Print the new dictionary. The new dictionary should only contain 'name' and 'address' for that restaurant

print()
print(restaurant_1)

print()
print("Question 4")

# Imagine that another one of your most favourite restaurants modified its address.
# Update just this value in that restaurant's dictionary


# TODO: Update the address field of 1 restaurant
# TODO: Print the new address of the restaurant by accessing that field of the restaurant's dictionary
# TODO: Print the updated dictionary.

restaurant_2["address"] = "66 E 55th Street, New York, NY 10022"
print(restaurant_2)

print()
print("Question 5")

# Printing out all 3 of our restaurants every time is getting annoying. Let's clean up our code!


# TODO: Put your 3 restaurant dictionaries into a list called `restaurants`
# TODO: Loop through your list and print out the name and address of each restaurant

restaurants = [restaurant_1, restaurant_2, restaurant_3]

for i in restaurants:
    print(f"Do you want to eat at {i['name']} located at {i['address']}?")

print()
print("Cool! I'll meet you there at 7 PM!")
