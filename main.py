# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import constant values
from constants import *

def main():
    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # create a clock object
    clock = pygame.time.Clock()
    dt = 0

    # create game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # fills the whole screen with color black
        pygame.Surface.fill(screen, "black")
        pygame.display.flip()

        # set fps to 60 frames per second
        clock.tick(60)

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
