# Importing the library
import pygame

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400, 300))

# Initializing RGB Color
color = (255, 0, 0)

# Changing surface color
surface.fill(color)
pygame.display.flip()

# run window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame. QUIT:
            running = False

# quit pygame after closing window
pygame. quit()
