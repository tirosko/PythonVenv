import pygame
pygame.init()
surface = pygame.display.set_mode((500, 400))

# colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.draw.rect(surface, red, pygame.Rect(50, 50, 100, 80))
pygame.draw.rect(surface, green, pygame.Rect(200, 50, 100, 80), 5)
pygame.draw.rect(surface, blue, pygame.Rect(350, 50, 100, 80), 10)

# pygame.display.flip()
# pygame.time.wait(4000)
# pygame.quit()

# This is a loop to keep the window open
# run window
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    pygame.time.wait(4000)
# quit pygame after closing window
pygame. quit()
