import pygame
import circleshape
from constants import *

class Shot(circleshape.CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation)

    def draw(self, screen):
        pygame.draw.circle(screen, 255,self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * PLAYER_SHOOT_SPEED * dt

