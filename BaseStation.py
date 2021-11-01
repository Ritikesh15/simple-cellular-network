import math

POWER_OF_BASE_STATION = 0.5
BAND = 5 * (10**9)
SPEED_OF_LIGHT = 299792458
K = POWER_OF_BASE_STATION / ((4 * math.pi * BAND / SPEED_OF_LIGHT)**2)

class BaseStation:
    def __init__(self, _id, coord):
        self.base_station_id = _id
        self.users_in_base_station = []
        self.position = coord

    def __str__(self):
        return "BS with id "+str(self.base_station_id) + " is at " + str(self.position)

    def power_of_bs_at_distance(self,coord):
        dist = self.position.distance_between_points(coord)
        return K/(dist**2)

    def add_ue_to_associated_bs(self, user_obj):
        self.users_in_base_station.append(user_obj)

    def print_bs_association_to_users(self):
        print("BS with id "+str(self.get_id())+" is associated with users with id:", end=' ')
        for user in self.users_in_base_station:
            print(user.get_id(), end = ' ')
        print()

    def get_id(self):
        return self.base_station_id

    def get_pos(self):
        return self.position
