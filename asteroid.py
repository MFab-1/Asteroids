import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        #Killing and checking if the asteroid had the smallest size 
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        #Calculating new parameters for the 2 spawning asteroids
        angle = random.uniform(20,50)
        newvector1 = pygame.math.Vector2.rotate(self.velocity, angle)
        newvector2 = pygame.math.Vector2.rotate(self.velocity, -angle)
        newradius = self.radius - ASTEROID_MIN_RADIUS

        ast1 = Asteroid(self.position.x, self.position.y,newradius)
        ast1.velocity = newvector1 * 1.2
        ast2 = Asteroid(self.position.x, self.position.y,newradius)
        ast2.velocity = newvector2 * 1.2



        