class UserEquipments:
    def __init__(self, _id, pos, bs):
        self.user_id = _id
        self.base_station = bs
        self.position = pos

    def __str__(self):
        return "UE with id "+str(self.user_id) + " is at " + str(self.position)

    def print_user_association_to_target_bs(self):
        print("UE with id "+str(self.user_id) + " is associated to BS with id " + str(self.base_station.base_station_id))

    def base_station_distance(self,bs):
        return self.position.distance_between_points(bs.position)

    def power_recieved(self,bs):
        return bs.power_of_bs_at_distance(self.position)
    
    def power_recieved_from_bs(self):
        return self.power_recieved(self.base_station)
    
    def get_id(self):
        return self.user_id

    def get_pos(self):
        return self.position

    def associated_bs(self):
        return self.base_station