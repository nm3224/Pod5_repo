class Station:
    def __init__(self, station_name, location):
        self.station_name = station_name
        self.location = location
    
    def show_info(self):
        print(f'{self.station_name} station is located at {self.location}')

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

class SubwayStation(Station):
    def __init__(self, station_name, location, lines):
        super().__init__(station_name, location)
        self.lines = lines
    
    def show_info(self):
        print(f'{self.station_name} station is located at {self.location}, and the line {self.lines} stop here.')


station_grand_central = BusStation('Grand Central Station', '42nd Street and Park Avenue', ['New Haven', 'Bronx', 'Long Island'] )

station_court_square = SubwayStation('14th street', '14th street and 7th avenue', ['1', '2', '3', 'L'] )

station_union_square = SubwayStation('Court Square', 'Jackson Avenue and 45th Avenue', ['7', 'G', 'E', 'M'] )

station_metropolotion = SubwayStation('Metropolitan Station', 'Metropolitan Avenue and Union Avenue', ['L', 'G'] )