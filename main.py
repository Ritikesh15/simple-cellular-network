import SimpleCellularNetwork as scn

NUM_OF_BASE_STATIONS = 20
NUM_OF_USER_EQUIPMENTS = 500

# initializing the network
simple_cellular_network = scn.SimpleCellularNetwork(NUM_OF_BASE_STATIONS, NUM_OF_USER_EQUIPMENTS)

# simple_cellular_network.users()
# simple_cellular_network.base_stations()
simple_cellular_network.SINR_for_each_UE() # 1
simple_cellular_network.bitrate_of_each_UE_and_system_throughput() # 2, 3
simple_cellular_network.user_association_matrix() # 3.a
simple_cellular_network.base_station_association_matrix() # 3.b
