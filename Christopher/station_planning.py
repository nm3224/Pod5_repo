'''
Now, it's time to design a few more stations of your own in another script! 

Make a new python script called "station_planning.py"
    -In this script, *import* tfhe classes you made in this challenge file
    -Instantiate 3 more stations of your choosing (at least 1 bus and 1 subway)
    -Feel free to make up names, locations, lines, and routes!
'''
from stations_challenge import SubwayStation, BusStation

# Sunny Time Station is a subway station
sunny_time_station = SubwayStation('Sunny Time Station', 'Sunny Time Avenue and East Street', ['Up', 'Down', 'West', 'East'])
sunny_time_station.show_info()

# Eugene Station is a bus station
eugene_station = BusStation('Eugene Station', 'Willamette Street and 11th Avenue', ['Springfield', 'University of Oregon', 'Florence'])
eugene_station.show_info()
print('(Night falls in Eugene...)')
eugene_station.close_station()
eugene_station.show_info()
print('A stranger appears at the station and says, "Station is closed, but if you open that manhole cover you can take the secret subway underground..."')
sub_subway_station = SubwayStation('Sub-Subway Station', 'Willamette Street and 11th Avenue and 12 Feet Down', ['Portland', 'New York City', 'El Dorado', 'Xanadu'])
sub_subway_station.show_info()