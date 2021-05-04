import pygame

class Boundary:
    def __init__(self, x, y, radius):
        self.position = [x, y]
        self.radius = radius
        self.color = (255,255,255)
        self.outline = 1

    def display(self, screen, color=None):
        if color != None:
            pygame.draw.circle(screen, color, self.position, self.radius)
        else:
            pygame.draw.circle(screen, self.color, self.position, self.radius, self.outline)
