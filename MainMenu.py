import pygame
import Board

PLAYING_WINDOW_SIZE = 800, 800


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
        self.gray = (50, 50, 50)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.yellow = (255, 255, 0)

        self.selected = 'start'

    def render(self, screen, event):
        # is it ok?
        self.event_processing(event)

        screen.fill(self.blue)

        # optimize
        title = self.text_format("Yandex game", 85, self.yellow)
        if self.selected == "start":
            text_start = self.text_format("START", 75, self.white)
        else:
            text_start = self.text_format("START", 75, self.black)
        if self.selected == 'records':
            text_records = self.text_format("RECORDS", 75, self.white)
        else:
            text_records = self.text_format("RECORDS", 75, self.black)
        if self.selected == "quit":
            text_quit = self.text_format("QUIT", 75, self.white)
        else:
            text_quit = self.text_format("QUIT", 75, self.black)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        records_rect = text_records.get_rect()
        quit_rect = text_quit.get_rect()

        # Main Menu Texts
        screen.blit(title, (self.width / 2 - (title_rect[2] / 2), 80))
        screen.blit(text_start, (self.width / 2 - (start_rect[2] / 2), 300))
        screen.blit(text_records, (self.width / 2 - (records_rect[2] / 2), 360))
        screen.blit(text_quit, (self.width / 2 - (quit_rect[2] / 2), 420))
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

            self.selected = self.btns_in_menu[self.count]
            if event.key == pygame.K_RETURN:
                if self.selected == "start":
                    self.start_game()
                if self.selected == 'records':
                    self.show_records()
                if self.selected == "quit":
                    pygame.quit()
                    quit()

    def text_format(self, message, text_size, text_color):
        f2 = pygame.font.SysFont('serif', text_size)
        text2 = f2.render(message, False, text_color)
        return text2

    def start_game(self):
        board = Board.Board()
        running_game = True
        screen = pygame.display.set_mode(PLAYING_WINDOW_SIZE)
        while running_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_game = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    board.get_click(event.pos)

                screen.fill((0, 0, 0))
                board.render(screen)

    def show_records(self):
        pass
