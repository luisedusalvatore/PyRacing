import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

objects = [{'x': 400, 'y': 100, 'z': 1},
           {'x': 400, 'y': 200, 'z': 2},
           {'x': 400, 'y': 300, 'z': 3}]

def draw_object(obj):
    scale = 1 / obj['z']
    size = int(100 * scale)
    pygame.draw.circle(screen, (255, 0, 0), (obj['x'], obj['y']), size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30, 30, 30))

    for obj in objects:
        draw_object(obj)

    pygame.display.flip()
    clock.tick(60)