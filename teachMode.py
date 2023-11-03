from owl_client import OwlClient, Joint
from robot_arm_ip import robot_arm_ip
import time
import pygame
import datetime
import json

client = OwlClient(robot_arm_ip)

# Wait for Robot to be available to operate
while not client.is_running():
    time.sleep(0.2)

_toolspeed = 50  # mm/sec
joint1 = Joint(-0.1060069354430056, -1.5044083653721625, 0.1419258114490489, 0.06604325889546545, -1.6805326568502887, 0.001095678919307553)
client.move_to_joint(joint1, _toolspeed)

client.enter_teach_mode()

(width, height) = (600, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Teach Mode Input')
screen.fill((255,255,255))
pygame.display.flip()

running = True
poses = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pose = client.get_joint().get_joints()
            print(f'Saved pose: {pose}')
            poses.append(pose)
        if event.type == pygame.QUIT:
            running = False

client.end_teach_mode()
print("Exited teach mode")

# save poses to file titled H:MM:SS AM/PM on M D
date = datetime.datetime.now().strftime("%I:%M:%S %p on %B %d")
serializable_poses = json.dumps(poses)
with open(f'joints {date}.json', 'w') as f:
    f.write(serializable_poses)