# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    #init the screen and variables
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #Create groups and player (always set the groups before)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    Spaceship = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    Fieldofasteroids = AsteroidField()

    #Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return   

    #Updating and checking collision between ateroids and spaceship
        updatable.update(dt)
        for Asteroids in asteroids:
            if Asteroids.collisionscheck(Spaceship) == True:
                sys.exit("Game over")
        
    #Checking colission between shots and asteroids
        for Asteroids in asteroids:
            for bullet in shots:
                if bullet.collisionscheck(Asteroids) == True:
                    bullet.kill()
                    Asteroids.split()

    #Else generate antoher frame
        pygame.Surface.fill(screen,0)
        for items in drawable:
            items.draw(screen)
        pygame.display.flip()

        #Limit the framerate
        dt = clock.tick(60) / 1000


    

if __name__ == "__main__":
    main()