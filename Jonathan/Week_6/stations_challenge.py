'''
NYC Transit Challenge! 

In this challenge, you will use OOP and inheritance to design subway and bus stations!
You'll use the parent class Station to make child classes for SubwayStation and BusStation. 

Note, you should NOT need to change the Station class at all in this challenge.

Since subways and buses have different information, the methods and attributes will be a bit different
'''


print('Question 1: Making the SubwayStation Class')
'''
Using the Station class below as the parent, make a child class called SubwayStation

SubwayStation should:
-have an additional attribute called 'lines' that is user-defined as a list during initialization. 
    this will indicate which subway lines stop at the station (for example ['A', 'C'])
-override the show_info() method from Station to display which subway lines stop there, in addition to the station_name and location
'''
class Station:
    def __init__(self, station_name, location):
        self.station_name = station_name
        self.location = location
    
    def show_info(self):
        print(f'{self.station_name} station is located at {self.location}')

class SubwayStation(Station):
    def __init__(self, station_name, location, lines):
        super().__init__(station_name, location)
        self.lines = lines
    
    def show_info(self):
        print(f'{self.station_name} station is located at {self.location}, and the line {self.lines} stop here.')

print()
print('Question 2: Make an example subway station')
'''
Using your SubwayStation class, instantiate a subway station with the info below. 
Then run the show_info() method to make sure you get the station_name, location, and lines printed out

station_name: '14th street'
location: '14th street and 7th avenue'
lines: ['1', '2', '3', 'L']
'''

station_union_square = SubwayStation('14th street', '14th street and 7th avenue', ['1', '2', '3', 'L'] )

station_union_square.show_info()
print()

print('Question 3: Making the BusStation Class')

'''
Using the Station class below as the parent, make a child class called BusStation

BusStation should:
-have an additional attribute called 'routes' that is user-defined as a list during initialization. 
    this will indicate where buses can go from this station. For example, ['DC', 'Philly', 'Pittsburgh']
-have an additional attribute called 'open' that is always initalized as True (a boolean variable)
-have additional methods called open_station() and close_station() to open and close the station
-override the show_info() method from Station to display the bus routes and if the station is open, in addition to the station name and location
'''
class BusStation(Station):
    def __init__(self, station_name, location, routes):
        super().__init__(station_name, location)
        self.routes = routes
        self.open = True
    
    def open_station(self):
        if self.open == True:
            print(f'The {self.station_name} at {self.location} is open!')
        else:
            print(f'Sorry. The {self.station_name} at {self.location} is close.')

    def show_info(self):
        print(f'{self.station_name} station is located at {self.location}, and goes to the following routes: {self.routes}.')
        self.open_station

print()
print('Question 4: Make an example bus station')
'''
Using your BusStation class, instantiate a bus station with the info below. 
Then, run the show_info() method to make sure you get the station_name, location, routes, and whether the station is open printed out
Then, demonstrate that you can close and open the bus station
    i.e. that the show_info() method reflects correctly when the station is open versus closed

station_name: 'NYC Megabus Stop'
location: '34th street and 12th avenue'
lines: ['Boston', 'DC', 'Philly']
'''
station_port_authority = BusStation('NYC Megabus Stop', '34th street and 12th avenue', ['Boston', 'DC', 'Philly'] )
station_port_authority.show_info()


print()
print('Question 5: Importing your classes')

'''
Now, it's time to design a few more stations of your own in another script! 

Make a new python script called "station_planning.py"
    -In this script, *import* the classes you made in this challenge file
    -Instantiate 3 more stations of your choosing (at least 1 bus and 1 subway)
    -Feel free to make up names, locations, lines, and routes!
'''

from station_planning import Station, BusStation, SubwayStation
station_grand_central = BusStation('Grand Central Station', '42nd Street and Park Avenue', ['New Haven', 'Bronx', 'Long Island'] )
station_grand_central.show_info()
print()

station_court_square = SubwayStation('14th street', '14th street and 7th avenue', ['1', '2', '3', 'L'] )
station_court_square.show_info()
print()

station_union_square = SubwayStation('Court Square', 'Jackson Avenue and 45th Avenue', ['7', 'G', 'E', 'M'] )
station_union_square.show_info()
print()

station_metropolotion = SubwayStation('Metropolitan Station', 'Metropolitan Avenue and Union Avenue', ['L', 'G'] )
station_metropolotion.show_info()
print()