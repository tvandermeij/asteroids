from circleshape import *
import pygame
from constants import *
import random
from player import *
from asteroidsfield import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, asteroidfield):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            self.random_angle = random.uniform(20, 50)
            self.angle_one = self.velocity.rotate(self.random_angle)
            self.angle_two = self.velocity.rotate(-self.random_angle)
            self.new_radius = self.radius - ASTEROID_MIN_RADIUS
            self.velocity_one = self.angle_one * 1.2
            self.velocity_two = self.angle_two * 1.2
            asteroidfield.spawn(self.new_radius, self.position, self.velocity_one)
            asteroidfield.spawn(self.new_radius, self.position, self.velocity_two)


