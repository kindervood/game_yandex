import pygame
from MainMenu import Menu

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
        self.width = len(self.board[0])
        self.height = len(self.board)
        self.left = 15
        self.top = 15
        self.otstup = 5
        grass = load_image("grass.png")
        grass2 = load_image("grass2.png")
        glade = load_image("glade.png")
        glade2 = load_image("glade2.png")
        forest = load_image("forest.png")
        forest2 = load_image("forest2.png")
        mount = load_image("mount.png")
        mount2 = load_image("mount2.png")
        village = load_image("village.png")
        village2 = load_image("village2.png")

    def render(self, screen):
        # button to main_menu
        pygame.draw.rect(screen, 'red',
                         (PLAYING_WINDOW_SIZE[0] - BTN_SIZE[0] - self.otstup,
                          self.otstup, BTN_SIZE[0],
                          BTN_SIZE[1]))

        for x in range(self.width):
            for y in range(self.height):
                cell = self.board[y][x]
                if cell == 0:
                    screen.blit(grass,
                                     (self.cell_size * x + self.left,
                                      y * self.cell_size + self.top, self.cell_size,
                                      self.cell_size), 1)
                
                if cell == 1:
                    screen.blit(glade,
                                     (self.cell_size * x + self.left,
                                      y * self.cell_size + self.top, self.cell_size,
                                      self.cell_size), 1)
                if cell == 2:
                    screen.blit(forest,
                                     (self.cell_size * x + self.left,
                                      y * self.cell_size + self.top, self.cell_size,
                                      self.cell_size), 1)
                
                if cell == 3:
                    screen.blit(mount,
                                     (self.cell_size * x + self.left,
                                      y * self.cell_size + self.top, self.cell_size,
                                      self.cell_size), 1)
               if cell == 4:
                    screen.blit(village,
                                     (self.cell_size * x + self.left,
                                      y * self.cell_size + self.top, self.cell_size,
                                      self.cell_size), 1)       

        pygame.display.flip()

    def get_click(self, mouse_pos):
        # is it cell?
        if self.left < mouse_pos[0] < self.width * self.cell_size + self.left and \
                self.top < mouse_pos[1] < self.height * self.cell_size + self.top:
            cell = self.get_cell(mouse_pos)
            self.on_click_cell(cell)
        # is it quit btn?
        if PLAYING_WINDOW_SIZE[0] - BTN_SIZE[0] - self.otstup < mouse_pos[0] < PLAYING_WINDOW_SIZE[0] \
                - self.otstup and self.otstup < mouse_pos[1] < BTN_SIZE[1] + self.otstup:
            self.btn_quit_pressed()

    def get_cell(self, mouse_pos):
        x, y = ((mouse_pos[0] - self.left) // self.cell_size, (mouse_pos[1] - self.top) // self.cell_size)
        if 0 <= x < self.width and 0 <= y < self.height:
            return x, y
        return -1, -1

    def on_click_cell(self, cell_coords):
        x, y = cell_coords
        # TODO: show info about cell

    def btn_quit_pressed(self):
        # TODO: records and some statistic
        main_menu = Menu()
        running = True
        screen = pygame.display.set_mode(WINDOW_SIZE)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                screen.fill((0, 0, 0))
                main_menu.render(screen, event)
