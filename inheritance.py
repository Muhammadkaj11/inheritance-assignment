
class Vehicle:
    def __init__(self, vehicle_type, capacity):
        self.vehicle_type = vehicle_type  
        self.capacity = capacity  

    def __str__(self):
        return f"{self.vehicle_type} with capacity {self.capacity}"



class Bus(Vehicle):
    def __init__(self, vehicle_type, capacity, fare_per_passenger):
    
        super().__init__(vehicle_type, capacity)
        self.fare_per_passenger = fare_per_passenger  


    def calculate_total_fare(self, num_passengers):
    
        if num_passengers > self.capacity:
            raise ValueError("Number of passengers exceeds vehicle capacity.")
        return num_passengers * self.fare_per_passenger #calculations

bus = Bus(vehicle_type="City Bus", capacity=50, fare_per_passenger=2.5)

num_passengers = 30
total_fare = bus.calculate_total_fare(num_passengers)

print(f"Total fare for {num_passengers} passengers: ${total_fare:.2f}")
