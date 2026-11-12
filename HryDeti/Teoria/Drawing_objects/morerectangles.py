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

# Creating a list of different rects
rectangle_list = [pygame.Rect(50, 100, 500, 200),
                  pygame.Rect(70, 120, 460, 160),
                  pygame.Rect(90, 140, 420, 120),
                  pygame.Rect(110, 160, 380, 80),
                  pygame.Rect(130, 180, 340, 40)
                  ]

# Creating list of different colors
color_list = [(0,   0,   0),
              (255, 255, 255),
              (0,   0, 255),
              (0, 255,   0),
              (255,   0,   0)
              ]

# Creating a variable which we will use
# to iterate over the color_list
color_var = 0

# Iterating over the rectangle_list using
# for loop
for rectangle in rectangle_list:

    # Drawing the rectangle
    # using the draw.rect() method
    pygame.draw.rect(window, color_list[color_var],
                     rectangle)

    # Increasing the value of color_var
    # by 1 after every iteration
    color_var += 1

# Draws the surface object to the screen.
pygame.display.update()
# This is a loop to keep the window open
# run window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame. QUIT:
            running = False

# quit pygame after closing window
pygame. quit()
