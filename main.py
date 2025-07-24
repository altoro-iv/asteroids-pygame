# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import constant values
from constants import *
from player import Player

def main():
    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # create a clock object
    clock = pygame.time.Clock()

    # group for all objects that can be updated
    updatable = pygame.sprite.Group()

    # group for all objects that can be drawn
    drawable = pygame.sprite.Group()

    # set both groups as containers for the Player
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    # create game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        # fills the whole screen with color black
        screen.fill("black")

        # loop through drawables to draw them individually
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # set fps to 60 frames per second
        clock.tick(60)

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
