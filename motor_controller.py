class VehicleMotorController:
    def __init__(self, max_speed_limit):
        self.speed_limit = max_speed_limit  # Max positive speed (m/s)
        self.current_velocity = 0.0         # Current physical state (m/s)

    def set_velocity(self, target_velocity):
        # 1. Upper Bound Saturation (Prevents going over the speed limit)
        if target_velocity > self.speed_limit:
            self.current_velocity = self.speed_limit
            print(f"[WARN] Requested speed too high! Capped at: {self.speed_limit} m/s")
        
        # 2. Lower Bound Saturation (Prevents slamming into reverse)
        elif target_velocity < 0.0:
            self.current_velocity = 0.0
            print("[WARN] Negative speed requested! Safely stopped at 0.0 m/s")
        else:
            self.current_velocity = target_velocity
            print(f"[INFO] Motors driving at: {self.current_velocity} m/s")












# 1. Dragging the block onto the canvas and naming it "my_motors". 
# We are setting the block's internal parameter to a 5.0 m/s limit.
my_motors = VehicleMotorController(max_speed_limit=5.0)

# 2. Sending our first test signal (Target: 3.0 m/s)
print("--- TEST 1 ---")
my_motors.set_velocity(3.0)

# 3. Sending an over-speed test signal (Target: 8.5 m/s)
print("\n--- TEST 2 ---")
my_motors.set_velocity(8.5)

# 4. Sending a dangerous negative test signal (Target: -2.0 m/s)
print("\n--- TEST 3 ---")
my_motors.set_velocity(-2.0)




 






