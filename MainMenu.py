import pygame
import Board
import Records
import Shop

from Main import text_format


PLAYING_WINDOW_SIZE = 800, 700
WINDOW_SIZE = 600, 600


class Menu:
    def __init__(self):
        self.width = 600
        self.height = 600

        self.count = 0
        # btns in main menu
        self.btns_in_menu = {
            0: 'start',
            1: 'records',
            2: 'quit'
        }
        self.count_btns = len(self.btns_in_menu)

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.grey = (50, 50, 50)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.yellow = (255, 255, 0)

        self.selected = 'start'

        ######################################################## testing input text
        self.input_box = pygame.Rect(370, 25, 140, 32)
        self.color_inactive = pygame.Color('black')
        self.color_active = pygame.Color('red')
        self.color = self.color_inactive
        self.active = False
        self.text = ''
        #######################################################

    def render(self, screen, event):
        # обработка события
        self.event_processing(event)

        screen.fill(self.blue)

        # элементы меню
        title = text_format("Yandex game", 85, self.yellow)
        if self.selected == "start":
            text_start = text_format("START", 75, self.white)
        else:
            text_start = text_format("START", 75, self.black)
        if self.selected == 'records':
            text_records = text_format("RECORDS", 75, self.white)
        else:
            text_records = text_format("RECORDS", 75, self.black)
        if self.selected == "quit":
            text_quit = text_format("QUIT", 75, self.white)
        else:
            text_quit = text_format("QUIT", 75, self.black)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        records_rect = text_records.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Texts
        screen.blit(title, (self.width / 2 - (title_rect[2] / 2), 80))
        screen.blit(text_start, (self.width / 2 - (start_rect[2] / 2), 300))
        screen.blit(text_records, (self.width / 2 - (records_rect[2] / 2), 360))
        screen.blit(text_quit, (self.width / 2 - (quit_rect[2] / 2), 420))

        #####################testing input box
        font = pygame.font.Font(None, 32)
        txt_surface = font.render(self.text, True, self.color)

        # Blit the text.
        screen.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, self.color, self.input_box, 2)
        ####################################

        pygame.display.flip()

    def event_processing(self, event):
        if event.type == pygame.KEYDOWN:
            # ограничения, чтобы не вызывать key_error в словаре self.btns_in_menu
            if event.key == pygame.K_UP:
                if self.count > 0:
                    self.count -= 1
            elif event.key == pygame.K_DOWN:
                if self.count < self.count_btns - 1:
                    self.count += 1
            # подсветка выбранного элемента
            self.selected = self.btns_in_menu[self.count]
            if event.key == pygame.K_RETURN:
                if self.selected == "start":
                    self.start_game()
                if self.selected == 'records':
                    self.show_records()
                if self.selected == "quit":
                    pygame.quit()
                    quit()
            # возможность ввода в поле
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < 10:
                        self.text += event.unicode

        # активация поля при нажатии
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_box.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive

    def start_game(self):
        board = Board.Board()
        running_game = True
        screen = pygame.display.set_mode(PLAYING_WINDOW_SIZE, flags=pygame.NOFRAME)
        # создадим группу, содержащую все спрайты
        all_sprites = pygame.sprite.Group()
        # добавляем спрайты
        Shop.Shop(all_sprites)
        # рисуем все спрайты на screen
        all_sprites.draw(screen)
        while running_game:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_game = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    board.get_click(event.pos)
                    all_sprites.update(event)

            screen.fill((0, 0, 0))
            all_sprites.draw(screen)
            board.render(screen)

            pygame.display.flip()

    def show_records(self):
        records = Records.Records()
        running = True
        screen = pygame.display.set_mode(WINDOW_SIZE, flags=pygame.NOFRAME)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                records.render(screen, event)
