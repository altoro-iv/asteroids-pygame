# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import constant values
from constants import *

def main():
    # initialize pygame
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # creat game loop
    counter = 0
    while counter == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
