class LidarSensor:
    def __init__(self, num_zones):
        # The constructor sets up the hardware parameters
        self.num_zones = num_zones
        
        # We initialize the sensor state with a list of safe distances.
        # [10.0] * 8 creates an array of eight 10.0s: [10.0, 10.0, 10.0, ...]
        self.current_scan = [10.0] * self.num_zones

    def read_scan(self):
        # This function simply outputs the current state of the array
        return self.current_scan

    def inject_obstacle(self, zone_index, distance):
        # A function to simulate an object stepping in front of the robot
        self.current_scan[zone_index] = distance
        print(f"[SENSOR] Hardware interrupt: Obstacle in zone {zone_index} at {distance} meters!")



        # 1. Instantiate
my_lidar = LidarSensor(8)

# 2. Print initial state
print("Initial Scan:", my_lidar.read_scan())

# 3. Inject obstacle... (Your turn to write this line!)
my_lidar.inject_obstacle(3,2.5)

# 4. Print new state... (Your turn to write this line!)
print("New scan:", my_lidar.read_scan())

