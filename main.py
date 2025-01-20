# This allows us to use code from 
# the open-source pygame library
# throughout this file
import pygame
import sys
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (bullets, updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))

        for item in updateable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)
        for item in asteroids:
            if item.detect_collision(player):
                print("Game over!")
                sys.exit()
            for bullet in bullets:
                if bullet.detect_collision(item):
                    item.split()
                    bullet.kill()

        pygame.display.flip()
        dt = clock.tick() / 1000

if __name__ == "__main__":
    main()
