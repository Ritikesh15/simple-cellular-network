from random import randint
import BaseStation as bs_module
import UserEquipments as ue_module
import Coordinate as utl
import math
# import base_station as bs_module
# import user_equipments as ue_module

BANDWIDTH_PER_USER = (10 ** 6)
MAX_RANGE_OF_BS = 2000
NOISE = 5 * (10**-21) # standard thermal noise

def create_random_coordinates(num_ue_or_bs):
    coordinates_set = set()
    while len(coordinates_set) < num_ue_or_bs:
        x, y = randint(0, 5000), randint(0, 5000)
        coord = utl.Coordinate(x, y)
        coordinates_set.add(coord)
    return coordinates_set

def assign_id_and_coord_to_base_station(position_of_bs):
    _id = 0
    id_coord_assigned_bs_list = []
    for coord in position_of_bs:
        #append bs obj 
        id_coord_assigned_bs_list.append(bs_module.BaseStation(_id, coord))
        _id = _id + 1
    return id_coord_assigned_bs_list

def assign_id_coord_and_null_base_to_user(position_of_ue):
    _id = 0
    partial_assigned_ue_list = []
    null_bs = bs_module.BaseStation(0, utl.Coordinate(0, 0))
    for coord in position_of_ue:
        #append user object
        partial_assigned_ue_list.append(ue_module.UserEquipments(_id, coord, null_bs))
        _id = _id + 1
    return partial_assigned_ue_list


class SimpleCellularNetwork:
    def __init__(self,num_bs,num_ue):
        random_coordinates_for_bs_list = create_random_coordinates(num_bs)
        random_coordinates_for_ue_list = create_random_coordinates(num_ue)
        
        self.id_coord_assigned_bs_list = assign_id_and_coord_to_base_station(random_coordinates_for_bs_list)
        self.partial_assigned_ue_list = assign_id_coord_and_null_base_to_user(random_coordinates_for_ue_list)
        self.initialize_simple_cellular_network()

    def initialize_simple_cellular_network(self):
        for user_obj in self.partial_assigned_ue_list:
            closest_bs = self.find_closest_bs(user_obj)
            user_obj.base_station = closest_bs
            closest_bs.add_ue_to_associated_bs(user_obj)

    def find_closest_bs(self, user_obj):
        max_power = -math.inf
        for bs in self.id_coord_assigned_bs_list:
            curr_power = user_obj.power_recieved(bs)
            if  curr_power > max_power:
                max_power = curr_power
                max_power_bs = bs
        return max_power_bs

    def power_of_interference_noise(self,user_obj):
        interference = 0
        for bs in self.id_coord_assigned_bs_list:
            if bs == user_obj.associated_bs():
                continue
            dist = user_obj.base_station_distance(bs)
            if dist < MAX_RANGE_OF_BS:
                interference = interference + bs.power_of_bs_at_distance(user_obj.position)
        interference = interference + NOISE*BANDWIDTH_PER_USER
        return interference

    def get_sinr_list(self):
        sinr_list=[]
        for user_obj in self.partial_assigned_ue_list:
            sinr = user_obj.power_recieved_from_bs() / self.power_of_interference_noise(user_obj)
            sinr_list.append((user_obj.get_id(), sinr))
        return sinr_list

    def get_bitrate_list(self):
        bitrate_list=[]
        sinr_list = self.get_sinr_list()
        for _id, sinr in sinr_list:
            bitrate = BANDWIDTH_PER_USER * math.log2(1 + sinr)
            bitrate_list.append((_id, bitrate))
        return bitrate_list

    def user_association_matrix(self):
        print("User's association to target base station:")
        for user_obj in self.partial_assigned_ue_list:
            user_obj.print_user_association_to_target_bs()
        print()

    def base_station_association_matrix(self):
        print("Base station association with users:")
        for base in self.id_coord_assigned_bs_list:
            base.print_bs_association_to_users()
        print()

    def SINR_for_each_UE(self):
        sinr_list = self.get_sinr_list()
        print("SINR for each UE (id,sinr):")
        for _id, sinr in sinr_list:
            print("UE with id "+str(_id)+" has SINR of "+str(sinr))
        print()

    def bitrate_of_each_UE_and_system_throughput(self):
        bitrate_list = self.get_bitrate_list()
        thruPut = 0
        print("Bitrate for each UE (id,bitrate):")
        for _id, bitrate in bitrate_list:
            thruPut += bitrate
            print("UE with id "+str(_id)+" has bitrate of "+str(bitrate))
        print()
        print("System throughput: "+str(thruPut))
        print()

    #printing users
    # def users(self):
    #     print("User's respective id and coordinate in the network:")
    #     for user_obj in self.partial_assigned_ue_list: #ue_list
    #         print(user_obj) #print obj
    #     print()

    #printing base stations
    # def base_stations(self):
    #     print("Base station's respective id and coordinate in the network:")
    #     for base in self.id_coord_assigned_bs_list: #bs_list
    #         print(base) #print_obj
    #     print()