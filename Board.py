import pygame
from Main import load_image
import MainMenu
from Main import text_format

CELL_SIZE = 50
PLAYING_WINDOW_SIZE = 800, 800
WINDOW_SIZE = 600, 600
BTN_SIZE = 25, 25
CELL_COUNTRY = (5, 20)  # ячейка деревни
PUT_DO_IMAGES = 'images'


class Board:
    def __init__(self):
        self.cell_size = CELL_SIZE
        self.board = []
        with open('board.txt') as input_file:
            for line in input_file:
                self.board.append(list(map(int, line.split())))
        self.width = len(self.board[0])
        self.height = len(self.board)
        self.left = 15
        self.top = 15
        self.otstup = 5
        self.cell_country = CELL_COUNTRY
        self.food = 10
        self.f = "  " + str(self.food)
        self.people = 10
        self.p = "  " + str(self.people)
        self.stone = 10
        self.s = "  " + str(self.stone)
        self.wood = 10
        self.w = "  " + str(self.wood)
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
        self.text = text_format("Деревня  " + self.f + self.p + self.s + self.w, 15, (255, 255, 255))
        self.activ_cell = text_format("", 45, (255, 255, 255))

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
                #if cell == 4:
                    #screen.blit(self.village,
                                #(self.cell_size * x + self.left,
                                 #y * self.cell_size + self.top))
        screen.blit(self.text, (650, 0))
        screen.blit(self.activ_cell, (600, 0))
        pygame.display.flip()

    def get_click(self, mouse_pos):
        # is it cell?
        if self.left < mouse_pos[0] < self.width * self.cell_size + self.left and \
                self.top < mouse_pos[1] < self.height * self.cell_size + self.top:
            cell = self.get_cell(mouse_pos)
            self.on_click_cell(cell)
            if 500 < mouse_pos[0] < 600 and 400 < mouse_pos[1] < 445:
                self.mining(cell)# кнопка дабыть
        # is it quit btn?
        if PLAYING_WINDOW_SIZE[0] - BTN_SIZE[0] - self.otstup < mouse_pos[0] < PLAYING_WINDOW_SIZE[0] \
                - self.otstup and self.otstup < mouse_pos[1] < BTN_SIZE[1] + self.otstup:
            self.btn_quit_pressed()


    def get_cell(self, mouse_pos):
        # получение координаты клетки относительно всего поля
        x, y = (
            (mouse_pos[0] - self.left) // self.cell_size,
            (mouse_pos[1] - self.top) // self.cell_size)
        if 0 <= x < self.width and 0 <= y < self.height:
            return x, y
        return -1, -1

    def on_click_cell(self, cell_coords):
        x, y = cell_coords
        self.cell = self.board[y][x]
        if self.cell == 0:
            self.activ_cell = text_format("Пустое поле", 45, (255, 255, 255))
        if self.cell == 1:
            self.activ_cell = text_format("Река с ягодами", 45, (255, 255, 255))
        if self.cell == 2:
            self.activ_cell = text_format("Горы", 45, (255, 255, 255))
        if self.cell == 3:
            self.activ_cell = text_format("Лес", 45, (255, 255, 255))

    def btn_quit_pressed(self):
        # TODO: records and some statistic
        # to main menu
        main_menu = MainMenu.Menu()
        running = True
        screen = pygame.display.set_mode(WINDOW_SIZE, flags=pygame.NOFRAME)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                screen.fill((0, 0, 0))
                main_menu.render(screen, event)

    def get_distance_vector(self, cell_click):
        S = (abs(self.cell_country[0] - cell_click[0]) + abs(
            self.cell_country[1] - cell_click[1])) ** 0.5
        return S

    def mining(self, cell_coords):
        x, y = cell_coords
        self.cell = self.board[y][x]
        if self.cell == 1:
            self.food += 5
            self.people -= 1
        if self.cell == 2:
            self.stone += 2
            self.people -= 1
        if self.cell == 3:
            self.wood += 2
            self.people -= 1

