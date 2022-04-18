from stations_challenge import *

bustation2 = BusStation(station_name = 'MetroPark Stop', location = '10th Avenue and 4th Avenue',routes = ['Jungle', 'Amazon', 'Nile']) 

subway_station2 = SubwayStation(station_name= '9th Street', location= 'Paul Revere Street and Broadway Avenue', lines= ['A', 'B', '1', '2'])

bustation3 = BusStation(station_name = 'Penn Station', location = '351 West 31st Street',routes = ['MSG', 'Newark', 'AC']) 

bustation2.show_info()
subway_station2.show_info()
bustation3.show_info()