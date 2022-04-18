from stations_challenge import SubwayStation, BusStation

taipei_central = BusStation('Taipei Bus Central', 'Chunghwua Road Section 1 and Boai Road', ['North Gate', 'Yunghe', 'Zhonghe High School'])

neihu_station = BusStation('Neihu Southeast Parking Lot', 'No.34 Xingzhong Road', ['Neihu', 'Banqiao', 'Tienmu', 'Yangmingshan'])

mrt_jingan = SubwayStation('MRT Jingan', 'No. 790 Jingping Road Section 3, Zhonghe', ['Green', 'Blue', 'Circular'])

taipei_central.show_info()
taipei_central.close_station()
taipei_central.show_info()

neihu_station.show_info()
neihu_station.close_station()
neihu_station.show_info()

mrt_jingan.show_info()
