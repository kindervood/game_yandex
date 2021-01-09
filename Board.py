import pygame
from Main import load_image
import MainMenu
from MainMenu import text_format

CELL_SIZE = 50
PLAYING_WINDOW_SIZE = 800, 800
WINDOW_SIZE = 600, 600
BTN_SIZE = 25, 25


class Board:
    def __init__(self):
        self.cell_size = CELL_SIZE
        self.board = []
        with open('board.txt') as input_file:
            for line in input_file:
                self.board.append(list(map(int, line.split())))
        self.food = 10
        self.people = 10
        self.stone = 10
        self.width = len(self.board[0])
        self.height = len(self.board)
        self.left = 15
        self.top = 15
        self.otstup = 5
        self.grass = load_image("grass.png")
        self.grass = pygame.transform.scale(self.grass, (50, 50))
        self.glade = load_image("glade.png")
        self.glade = pygame.transform.scale(self.glade, (50, 50))
        self.forest = load_image("forest.png")
        self.forest = pygame.transform.scale(self.forest, (50, 50))
        self.mount = load_image("mount.png")
        self.mount = pygame.transform.scale(self.mount, (50, 50))
        self.text = self.text_format("Деревня  " + self.food + self.people + self.stone, 45, self.white)
        self.activ_cell = self.text_format("", 45, self.white)

    def render(self, screen):
        # button to main_menu
        pygame.draw.rect(screen, 'red',
                         (PLAYING_WINDOW_SIZE[0] - BTN_SIZE[0] - self.otstup,
                          self.otstup, BTN_SIZE[0],
                          BTN_SIZE[1]))
        pygame.draw.rect(screen, 'red', (500, 400, 100, 45))

        for x in range(self.width):
            for y in range(self.height):
                cell = self.board[y][x]
                if cell == 0:
                    screen.blit(self.grass,
                                (self.cell_size * x + self.left,
                                 y * self.cell_size + self.top))

                if cell == 1:
                    screen.blit(self.glade,
                                (self.cell_size * x + self.left,
                                 y * self.cell_size + self.top,))
                if cell == 2:
                    screen.blit(self.forest,
                                (self.cell_size * x + self.left,
                                 y * self.cell_size + self.top,))

                if cell == 3:
                    screen.blit(self.mount,
                                (self.cell_size * x + self.left,
                                 y * self.cell_size + self.top))
                if cell == 4:
                    screen.blit(self.village,
                                (self.cell_size * x + self.left,
                                 y * self.cell_size + self.top))
        screen.blit(self.text, (650, 0))
        screen.blit(self.activ_cell, (600, 0))
        pygame.display.flip()

    def get_click(self, mouse_pos, screen):
        # is it cell?
        if self.left < mouse_pos[0] < self.width * self.cell_size + self.left and \
                self.top < mouse_pos[1] < self.height * self.cell_size + self.top:
            cell = self.get_cell(mouse_pos)
            self.on_click_cell(cell, screen)
        # is it quit btn?
        if PLAYING_WINDOW_SIZE[0] - BTN_SIZE[0] - self.otstup < mouse_pos[0] < PLAYING_WINDOW_SIZE[0] \
                - self.otstup and self.otstup < mouse_pos[1] < BTN_SIZE[1] + self.otstup:
            self.btn_quit_pressed()
        if 500 < mouse_pos[0] < 600 and 400 < mouse_pos[1] < 445:
            self.mining(cell)



    def get_cell(self, mouse_pos):
        x, y = ((mouse_pos[0] - self.left) // self.cell_size, (mouse_pos[1] - self.top) // self.cell_size)
        if 0 <= x < self.width and 0 <= y < self.height:
            return x, y
        return -1, -1

    def on_click_cell(self, cell_coords, screen):
        x, y = cell_coords
        self.cell = self.board[y][x]
        if self.cell == 0:
            self.activ_cell = self.text_format("Пустое поле", 45, self.white)
        if self.cell == 1:
            self.activ_cell = self.text_format("Река с ягодами", 45, self.white)
        if self.cell == 2:
            self.activ_cell = self.text_format("Горы", 45, self.white)
        if self.cell == 3:
            self.activ_cell = self.text_format("Лес", 45, self.white)





        pygame.display.flip()

    def btn_quit_pressed(self):
        # TODO: records and some statistic
        main_menu = MainMenu.Menu()
        running = True
        screen = pygame.display.set_mode(WINDOW_SIZE)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                screen.fill((0, 0, 0))
                main_menu.render(screen, event)
