import pygame

from circleshape import CircleShape

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 255255255, self.position, self.radius, 2)

    def update(self, dt):
        forward = pygame.Vector2(0, 1)
        self.position += forward + (self.velocity * dt)
