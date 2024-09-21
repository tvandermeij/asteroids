# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroidsfield import *
from circleshape import *
from shots import *

def main():
    pygame.init()
    time = pygame.time.Clock()
    dt = 0
    score = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        dt = time.tick(60) / 1000 

        for item in updateable: 
            item.update(dt)

        for item in asteroids:
            for bullet in shots:
                if item.collision(bullet) == True:
                    item.split(asteroidfield)
                    bullet.kill()
                    score += 1
        
        for item in asteroids:
            if item.collision(player) == True: 
                print("Game over!")
                print(f"Your score was: {score}")
                return True

        
        pygame.Surface.fill(screen, "black")

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()