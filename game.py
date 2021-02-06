#Pygame

import pygame
from pygame.locals import *

pygame.init()

vec = pygame.math.Vector2  # 2 for two dimensional
 
HEIGHT = 450
WIDTH = 400
x = HEIGHT/2
y = WIDTH/2
vel = .05
FPS = 60

FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

run = True

while(run):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    displaysurface.fill((0))
    pygame.draw.rect(displaysurface, (255, 0, 0), (x, y, 50, 50))
    pygame.display.update()

pygame.quit()