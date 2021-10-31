from random import randint
import math
import base_station as bs_module
import user_equipments as ue_module

POWER_OF_BASE_STATION = 0.5
BAND = 5 * (10**9)
SPEED_OF_LIGHT = 299792458
K = POWER_OF_BASE_STATION / ((4 * math.pi * BAND / SPEED_OF_LIGHT)**2)
NOISE = 5 * (10**-21) # standard thermal noise
MAX_RANGE_OF_BS = 2000
BANDWIDTH_PER_USER = (10 ** 6)
NUM_OF_BASE_STATIONS = 20
NUM_OF_USER_EQUIPMENTS = 500
 
class Coordinate :
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "( "+str(self.x)+" , "+str(self.y)+" )"

    def distance_between_points(self, coord):
        distance = math.sqrt((self.x-coord.x)*(self.x-coord.x)+(self.y-coord.y)*(self.y-coord.y))
        return distance

def create_random_coordinates(num_ue_or_bs):
    coordinates_set = set()
    while len(coordinates_set) < num_ue_or_bs:
        x, y = randint(0, 5000), randint(0, 5000)
        coord = Coordinate(x, y)
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
    null_bs = bs_module.BaseStation(0, Coordinate(0, 0))
    for coord in position_of_ue:
        #append user object
        partial_assigned_ue_list.append(ue_module.UserEquipments(_id, coord, null_bs))
        _id = _id + 1
    return partial_assigned_ue_list
