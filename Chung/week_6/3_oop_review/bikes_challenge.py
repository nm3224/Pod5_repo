# You are starting a bike-sharing service. Your first bike station will be at 14th St and 5 Ave.
# The dictionary below represents your first station.

from argparse import _StoreConstAction


station = {
	'name': 'Station A',
 	'address': '14th St and 5 Ave',
 	'bikes': []
}

print('Question 1')

# You don't have any bikes at this station. Create a function 'add' that adds bikes to the bikes list.
# A bike can be represented by an id number in the bikes list
# Parameters: id (int)
# Returns: nothing

def add(id):
	if type(id) == int:
		station['bikes'].append(id)
	if type(id) == list:
		station['bike'].extend(id)
	else:
		print('You must add the id(s) of the bike(s) as an integer or a list of integers')

print('')

print('Question 2')
# Create a function 'check_out' to checks out a bike (removes it by id) from the bikes list
# Parameters: id (int)
# Returns: nothing

def check_out(id):
	if type(id) == int:
		station['bikes'].remove(id)
	else:
		print('You must give the bike\'s id as an integer to check it out.')

print('')

print('Question 3')
# Create a function 'check_in' that returns a bike (adding it by id) to the bikes list.
# Parameters: id (int)
# Returns: nothing

def check_in(id):
	if type(id) == int:
		station['bikes'].append(id)
	else:
		print('You must give the bike\'s id as an integer to check it in.')

print('')

print('Question 4')
# Congratulations! Your business is expanding. You want to create multiple stations around the city.
# Create a class BikeStation that has the data (name, address, bikes) and all the functions (add, check_out, check_in)
# Parameters to create object: name (string) and address (string)
# Returns: BikeStation Object

class BikeStation(object):
	'''initialize class with attruibutes'''
	def __init__(self, name, address):
		self.name = name
		self.address = address
		self.bikes = []

	def __repr__(self):
		return f'The {self.name} station is located at {self.address}, and it has the following bikes: {", ".join([str(bike) for bike in self.bikes])}.'

	def add(self, id):
		if type(id) == int:
			self.bikes.append(id)
		if type(id) == list:
			self.bikes.extend(id)
		else:
			print('You must add the id(s) of the bikes as an integer or s list of integers')
	def check_out(self, id):
		if type(id) == int:
			self.bikes.remove(id)
		else:
			print('You must give the bike\'s id as an integer to remove it.')

	def check_in(self, id):
		if type(id) == int:
			self.bikes.append(id)
		else:
			print('You must give the bike\'s id as an integer to check it in.')


print('')

print('Question 5')
# You will create station objects using BikeStation class and save them to variables.
# 5.1 - First station, name is Station A. Give it an address of your own choosing.
# 5.2 - Second station, name is Station B. Give it an address of your own choosing.

station_a = BikeStation('Station a', '45 Long St')
station_b = BikeStation('Station B', '1234 5th Ave')

print('')

print('Question 6')
# 6.1 - Add bikes 1, 2, 3 to Station A.
# 6.2 - Add bikes 4, 5, 6 to Station B.
# Print the bikes attributes for both Station A and Station B objects.

station_a.add([1,2,3])
station_b.add([4,5,6])

print(station_a)
print(station_b)

print('')

print('Question 7')
# 7.1 - Check out bike 3 from Station A
# 7.2 - Check out bike 5 from  Station B
# 7.3 - Check in bike 3 to Station B
# Print the bikes attributes for both Station A and Station B objects.

station_a.check_out(3)
station_b.check_out(5)
station_b.check_in(3)

print(station_a)
print(station_b)
