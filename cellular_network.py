import utils
import math
# import base_station as bs_module
# import user_equipments as ue_module

class cellular_network:
    def __init__(self,num_bs,num_ue):
        random_coordinates_for_bs_list = utils.create_random_coordinates(num_bs)
        random_coordinates_for_ue_list = utils.create_random_coordinates(num_ue)
        
        self.id_coord_assigned_bs_list = utils.assign_id_and_coord_to_base_station(random_coordinates_for_bs_list) #bs_list
        self.partial_assigned_ue_list = utils.assign_id_coord_and_null_base_to_user(random_coordinates_for_ue_list) #ue_list
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
            if dist < utils.MAX_RANGE_OF_BS:
                interference = interference + bs.power_of_bs_at_distance(user_obj.position)
        interference = interference + utils.NOISE*utils.BANDWIDTH_PER_USER
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
            bitrate = utils.BANDWIDTH_PER_USER * math.log2(1 + sinr)
            bitrate_list.append((_id, bitrate))
        return bitrate_list

    def users(self):
        print("User's respective id and coordinate in the network:")
        for user_obj in self.partial_assigned_ue_list: #ue_list
            print(user_obj) #print obj
        print()

    def base_stations(self):
        print("Base station's respective id and coordinate in the network:")
        for base in self.id_coord_assigned_bs_list: #bs_list
            print(base) #print_obj
        print()

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
        print("SINR for each UE (id,sinr)")
        for _id, sinr in sinr_list:
            print("UE "+str(_id)+" : "+str(sinr))
        print()

    def bitrate_of_each_UE_and_system_throughput(self):
        bitrate_list = self.get_bitrate_list()
        thruPut = 0
        print("Shannon bitrate for each UE (id,bitrate)")
        for _id, bitrate in bitrate_list:
            thruPut += bitrate
            print("UE "+str(_id)+" : "+str(bitrate))
        print("System throughput: "+str(thruPut))

    # def print_user_entity(self):
    #     for station in self.partial_assigned_ue_list:
    #         print(str(station))

    # def get_user_positions(self):
    #     ue_x = []
    #     ue_y = []
    #     for user in self.partial_assigned_ue_list:
    #         pos = user.get_pos()
    #         ue_x.append(pos.x)
    #         ue_y.append(pos.y)
    #     return ue_x,ue_y

    # def get_base_positions(self):
    #     bs_x = []
    #     bs_y = []
    #     for base in self.id_coord_assigned_bs_list:
    #         pos = base.get_pos()
    #         bs_x.append(pos.x)
    #         bs_y.append(pos.y)
    #     return bs_x,bs_y
