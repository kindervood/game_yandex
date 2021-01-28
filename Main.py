import os
import sys
import pygame

import MainMenu

CELL_COUNTRY = (5, 20)  # ячейка деревни
PATH = 'images'
WINDOW_SIZE = (800, 700)


def load_image(name):
    fullname = os.path.join(
        PATH, name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def text_format(message, text_size, text_color, shrift='serif'):
    f2 = pygame.font.SysFont(shrift, text_size)
    text2 = f2.render(message, False, text_color)
    return text2


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    width, height = WINDOW_SIZE
    os.environ['SDL_VIDEO_WINDOW_POS'] = "500,25"
    screen = pygame.display.set_mode([width, height], flags=pygame.NOFRAME)
    running = True
    main_menu = MainMenu.Menu()

    tt = """3 3 3 3 3 3 3 3 3 3 3
    3 3 3 3 3 3 3 3 3 3 3
    0 2 1 2 0 0 0 0 0 0 0
    0 2 1 2 0 0 0 0 0 0 0
    0 2 1 2 0 0 4 0 0 0 0
    0 2 1 2 0 0 0 0 0 0 0
    0 2 1 2 0 0 0 0 0 0 0
    0 2 1 2 0 0 0 2 2 2 0
    0 2 1 2 0 0 0 2 2 2 0
    0 2 1 2 0 0 0 2 2 2 0"""
    with open('board.txt', 'w') as f:
        f = f.write(tt)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            screen.fill((0, 0, 0))
            main_menu.render(screen, event)
