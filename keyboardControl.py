import pygame
from owl_client import OwlClient, Pose
from robot_arm_ip import robot_arm_ip
import time

client = OwlClient(robot_arm_ip)

jointSpeed = 50  # degrees/sec
increment = 0.05

# Initialize pygame
pygame.init()

# Set up a dummy window necessary for keyboard inputs
screen = pygame.display.set_mode((1, 1))

# Wait for robot to be available
while not client.is_running():
    time.sleep(0.2)

# move to pose that doesn't trigger singularity
starting_pose = Pose()
starting_pose.x = -0.176
starting_pose.y = -0.240204
starting_pose.z = 0.489203
starting_pose.roll = 3.1376
starting_pose.pitch = -0.087288
starting_pose.yaw = 1.56449

client.move_to_pose(starting_pose, jointSpeed)
print("Moving to starting pose")

# initialize current pose (modified by keyboard ctrl)
current_pose = Pose()
current_pose.x = -0.176
current_pose.y = -0.240204
current_pose.z = 0.489203
current_pose.roll = 3.1376
current_pose.pitch = -0.087288
current_pose.yaw = 1.56449

# REPL loop: get user input
running = True
while running:
    pygame.time.Clock().tick(60)  # Run loop at max 60 times per second
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        current_pose.y += increment
        client.move_to_pose(current_pose, jointSpeed)

    if keys[pygame.K_s]:
        current_pose.y -= increment
        client.move_to_pose(current_pose, jointSpeed)

    if keys[pygame.K_a]:
        current_pose.x += increment
        client.move_to_pose(current_pose, jointSpeed)

    if keys[pygame.K_d]:
        current_pose.x -= increment
        client.move_to_pose(current_pose, jointSpeed)

    if keys[pygame.K_q]:
        current_pose.z += increment
        client.move_to_pose(current_pose, jointSpeed)
    
    if keys[pygame.K_e]:
        current_pose.z -= increment
        client.move_to_pose(current_pose, jointSpeed)

pygame.quit()
