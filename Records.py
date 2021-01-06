import pygame
import MainMenu

WINDOW_SIZE = 600, 600
BTN_SIZE = 20, 20

class Records:
    def __init__(self):
        self.width, self.height = WINDOW_SIZE
        self.otstup = 15

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.grey = (50, 50, 50)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.yellow = (255, 255, 0)

    def render(self, screen, event):
        screen.fill(self.grey)

        self.event_processing(event)

        title = self.text_format("Records", 85, self.black)
        title_rect = title.get_rect()
        screen.blit(title, (self.width / 2 - (title_rect[2] / 2), 80))
        # кнопка в главное меню
        pygame.draw.rect(screen, 'red',
                         (WINDOW_SIZE[0] - BTN_SIZE[0] - self.otstup,
                          self.otstup, BTN_SIZE[0],
                          BTN_SIZE[1]))

        pygame.display.flip()

    def event_processing(self, event):
        # обработка событий
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if WINDOW_SIZE[0] - BTN_SIZE[0] - self.otstup < mouse_pos[0] < WINDOW_SIZE[0] \
                    - self.otstup and self.otstup < mouse_pos[1] < BTN_SIZE[1] + self.otstup:
                self.to_main_menu()

    def text_format(self, message, text_size, text_color):
        # обработка текста
        f2 = pygame.font.SysFont('serif', text_size)
        text2 = f2.render(message, False, text_color)
        return text2

    def to_main_menu(self):
        # возвращение в главное меню
        main_menu = MainMenu.Menu()
        running = True
        screen = pygame.display.set_mode(WINDOW_SIZE)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                screen.fill((0, 0, 0))
                main_menu.render(screen, event)
