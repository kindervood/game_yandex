import pygame
from Board import Board
from MainMenu import Menu

WINDOW_SIZE = 600, 600

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    main_menu = Menu()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            screen.fill((0, 0, 0))
            main_menu.render(screen, event)
