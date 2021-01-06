import os
import sys
import pygame

import MainMenu

CELL_COUNTRY = (5, 20)  # ячейка деревни
PATH = 'images'
WINDOW_SIZE = (600, 600)


def load_image(name, colorkey=None):
    fullname = os.path.join(
        PATH, name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    width, height = WINDOW_SIZE
    screen = pygame.display.set_mode([width, height])
    running = True
    main_menu = MainMenu.Menu()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            screen.fill((0, 0, 0))
            main_menu.render(screen, event)
