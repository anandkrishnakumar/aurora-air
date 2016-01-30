import math
from geopy.distance import vincenty

class AirplaneModel:
    def __init__(self, brand, model_no, distance_range, fuel_required_per_km, fuel_capacity):
        self.brand = brand
        self.model_no = model_no
        self.distance_range = distance_range
        self.fuel_required_per_km = fuel_required_per_km
        self.fuel_capacity = fuel_capacity

    
class Airplane(AirplaneModel):
    def __init__(self, model, owner):
        AirplaneModel.__init__(self, model.brand, model.model_no, model.distance_range, model.fuel_required_per_km, model.fuel_capacity)
        self.owner = owner
        self.fuel = self.fuel_capacity

    def fly(self, origin, destination):
        distance_to_fly = self.calculate_distance(origin, destination)
        fuel_required = self.calculate_fuel_required(distance_to_fly)
        if self.has_required_fuel(fuel_required):
            self.fuel_change(fuel_required)
            print("Successful!", "Fuel left: "+str(self.fuel), "Distance: "+str(distance_to_fly)+" km", "Fuel used: "+str(fuel_required))
        else:
            print("Not enough fuel", "Distance: "+str(distance_to_fly)+" km", "Fuel used: "+str(fuel_required))

    def fuel_change(self, fuel_used):
        self.fuel = self.fuel-fuel_used

    def has_required_fuel(self, fuel_required):
        if self.fuel >= fuel_required:
            return True
        else:
            return False

    def calculate_fuel_required(self, distance):
        return self.fuel_required_per_km*distance

    def calculate_distance(self, origin, destination):
        origin_coordinates = (origin.lat, origin.long)
        destination_coordinates = (destination.lat, destination.long)
        return vincenty(origin_coordinates, destination_coordinates).km
