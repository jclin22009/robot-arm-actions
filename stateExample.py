from owl_client import OwlClient
from robot_arm_ip import robot_arm_ip
import time

client = OwlClient(robot_arm_ip)

# Wait for Robot to be available to operate
while not client.is_running():
    time.sleep(0.2)

while True:
    print("Current joint pose", client.get_joint().get_joints())
    print("Current TCP pose", client.get_tcp().get_pose())
    time.sleep(0.2)