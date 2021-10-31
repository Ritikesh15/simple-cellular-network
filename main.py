# import plotter
import utils as utl
import cellular_network as cn

# initializing the network
simple_cellular_network = cn.cellular_network(utl.NUM_OF_BASE_STATIONS,utl.NUM_OF_USER_EQUIPMENTS)

simple_cellular_network.users()
simple_cellular_network.base_stations()
simple_cellular_network.user_association_matrix() # 3.a
simple_cellular_network.base_station_association_matrix() # 3.b
simple_cellular_network.SINR_for_each_UE() # 1
simple_cellular_network.bitrate_of_each_UE_and_system_throughput() # 2, 3

# ue_x, ue_y = network.get_user_positions()
# bs_x,bs_y = network.get_base_positions()
# plotter.plot(bs_x, bs_y, ue_x, ue_y)