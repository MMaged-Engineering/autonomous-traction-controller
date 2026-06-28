import numpy as np

# 1. Our LiDAR data 
raw_sensor_data = [10.0, 2.0, 1.5, 10.0, 10.0, 10.0, 5.0, 6.0]
scan_matrix = np.array(raw_sensor_data)

# 2. Hardware parameters
base_cruising_speed = 5.0 # m/s
max_track_width = 5.0     # meters (Anything wider than this is 100% throttle)

# --- THE DYNAMIC CORNERING LOGIC ---

# Step A: Slice the array to find the closest left and right walls
left_clearance = np.min(scan_matrix[1:3])
right_clearance = np.min(scan_matrix[6:8])

# Step B: Find the absolute tightest pinch point on either side
tightest_clearance = min(left_clearance, right_clearance)

throttle_scale = tightest_clearance / max_track_width


# Step D: Apply the scale to the motors
# We use the built-in min() function to ensure our scale never goes above 1.0
safe_scale = min(throttle_scale, 1.0)
target_velocity = base_cruising_speed * safe_scale

print(f"Tightest side clearance: {tightest_clearance} meters")
print(f"Traction Scale Factor: {safe_scale}")
print(f"[CMD] Commanding Motors to: {target_velocity} m/s")
