# Importing pygame module
import pygame
# from pygame.locals import *  # No explicit names needed, so this line is removed

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))

# Fill the scree with white color
window.fill((255, 255, 255))

# Using draw.rect module of
# pygame to draw the outlined rectangle
pygame.draw.rect(window, (0, 0, 255),
                 [100, 100, 400, 100], 2)

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
