import pygame
import os
from Boundary import Boundary
from Ray import Ray
from random import randint

os.environ["SDL_VIDEO_CENTERED"]='1'

width, height = 1920, 1080
size = (width, height)
#colors
black = (20, 20, 20)
white = (247, 247, 247)
gray = (100, 100, 100)
orange = (249, 129, 58)
lightOrange = (253, 203, 158)
green = (204, 234, 187)

#pygame configurations
pygame.init()
pygame.display.set_caption("2D Raymarching")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
screen_offset = 50

Collisions = []

object_count = 10
angle = 0
objects = []

for i in range(object_count):
    obj = Boundary(randint(screen_offset, width - screen_offset), randint(screen_offset, height - screen_offset), randint(20, 100))
    obj.color = (0, 0, 0)
    obj.outline = 0
    objects.append(obj)

autoRotation = True

run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    key = pygame.key.get_pressed()
    if key[pygame.K_w] or key[pygame.K_UP]:
        angle -= 0.002
    if key[pygame.K_s] or key[pygame.K_DOWN]:
        angle += 0.002
    x_mouse, y_mouse = pygame.mouse.get_pos()
    ray = Ray(x_mouse, y_mouse, 0, screen, white)

    ray.angle = angle

    screen.fill(black)

    for object in objects:
        object.display(screen)

    for p in Collisions:
        pygame.draw.circle(screen, white, p, 2)

    if len(Collisions) > 2000:
        Collisions.pop()
    ray.March(objects, Collisions)

    if autoRotation == True:
        angle += 0.002

pygame.quit()
