import pygame
import math
from settings import WHITE

class Planet:
    def __init__(self, x, y, radius, speed, angle):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.angle = angle
        self.target_x = x
        self.target_y = y

    def update(self, screen_width, screen_height):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

        if self.x < 0 or self.x > screen_width:
            self.angle = math.pi - self.angle
        if self.y < 0 or self.y > screen_height:
            self.angle = -self.angle

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)
        
    def move_towards_target(self):
        self.x += (self.target_x - self.x) * 0.02
        self.y += (self.target_y - self.y) * 0.02
