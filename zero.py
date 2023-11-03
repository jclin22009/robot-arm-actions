from owl_client import OwlClient, Joint
from robot_arm_ip import robot_arm_ip
import time

client = OwlClient(robot_arm_ip)

# Wait for Robot to be available to operate
while not client.is_running():
    time.sleep(0.2)

_toolspeed = 100  # mm/sec

print("Moving to Pose1")
# Pose 1
zero_position = Joint() # 🍃😳
zero_position.Base = 0.0
zero_position.Shoulder = 0.0
zero_position.Elbow = 0.0
zero_position.Wrist1 = 0.0
zero_position.Wrist2 = 0.0
zero_position.Wrist3 = 0.0

# Move to Pose1
client.move_to_joint(zero_position, _toolspeed)