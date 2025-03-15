import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 255255255, self.position, self.radius, 2)

    def update(self, dt):
        forward = pygame.Vector2(0, 1)
        self.position += forward + (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vec_one = self.velocity.rotate(random_angle)
            vec_two = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_one = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid_two = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid_one.velocity = vec_one * 1.2
            new_asteroid_two.velocity = vec_two * 1.2