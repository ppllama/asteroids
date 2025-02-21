import pygame
from constants import *
from player import *

def main():
    
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        print(f"FPS: {clock.get_fps():.1f}")
        player.update(dt)

        screen.fill((0,0,0))
        player.draw(screen)
        


        pygame.display.flip()
        
        # print("foo")

if __name__ == "__main__":
    main()
