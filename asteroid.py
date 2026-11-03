import pygame
import random

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
from player import Player


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
    
    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_angle = random.uniform(20, 50)
        new_asteroid1 = Asteroid(self.position[0],self.position[1], new_radius)
        new_asteroid2 = Asteroid(self.position[0],self.position[1], new_radius)
        new_velocity1 = self.velocity.rotate(new_angle)
        new_velocity2 = self.velocity.rotate(-new_angle)
        new_asteroid1.velocity = new_velocity1 * 1.2
        new_asteroid2.velocity = new_velocity2 * 1.2
        