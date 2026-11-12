# https://www.geeksforgeeks.org/python/pygame-drawing-objects-and-shapes/
# Importing pygame module
import pygame
# from pygame.locals import *

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))

# Fill the scree with white color
window.fill((255, 255, 255))

# Using draw.rect module of
# pygame to draw the solid circle
# pygame.draw.circle(window, (0, 255, 0),
#    [300, 300], 170, 3)

pygame.draw.circle(window, (0, 255, 0),
                   [300, 300], 100, 5)

# Draws the surface object to the screen.
pygame.display.update()

# K pôvodnemu pridáme slučku pre udalosť QUIT, aby okno ostalo otvorené
# run window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame. QUIT:
            running = False

# quit pygame after closing window
pygame. quit()
