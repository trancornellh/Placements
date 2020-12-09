import pygame
import sys

pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Placements")

x = 50
y = 50
width = 50
height = 50
vel = 5

running = True

while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.display.update()


pygame.quit()
