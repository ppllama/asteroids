import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   
    while True:
    # Add this event loop to process system events
        for event in pygame.event.get():
            pass  # do nothing with events, but process them
        
    screen.fill((0, 0, 0))
    pygame.display.flip()

    # while True:
    #     screen.fill((0,0,0))
    #     pygame.display.flip()
    #     # print("foo")

if __name__ == "__main__":
    main()
