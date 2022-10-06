import pygame
import random

# Item Box Variables
box_height = 30
box_width = 30
box_x = 0
box_y = 0

# Spawn an item box
def spawn_box(clock):
    global box_x, box_y
    if(clock % 4000 <= 5):
        print("change values")
        box_x = random.randint(50, 1230)
        box_y = random.randint(0, 770)
    return pygame.Rect(box_x, box_y, box_height, box_width)
