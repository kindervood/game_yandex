import pygame

import Records
import Shop
from Main import load_image
import MainMenu
from Main import text_format

CELL_SIZE = 50
PLAYING_WINDOW_SIZE = 800, 800
WINDOW_SIZE = 800, 700
BTN_SIZE = 25, 25
CELL_COUNTRY = (5, 20)  # ячейка деревни
PUT_DO_IMAGES = 'images'
SCORE = 0


class Board:
    def __init__(self, nickname=''):
        self.nickname = nickname
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
        self.food = 20
        self.f = "  " + str(self.food)
        self.people = 10
        self.p = "  " + str(self.people)
        self.people_work = 0
        self.stone = 100
        self.s = "  " + str(self.stone)
        self.wood = 100
        self.w = "  " + str(self.wood)
        self.width = len(self.board[0])
        self.height = len(self.board)
        self.left = 15
        self.top = 15
        self.otstup = 5

        self.vilage = load_image("vilage.jpg")
        self.vilage = pygame.transform.scale(self.vilage, (50, 50))

        self.grass = load_image("grass.jpg")
        self.grass = pygame.transform.scale(self.grass, (50, 50))
        self.river = load_image("river.jpg")
        self.river = pygame.transform.scale(self.river, (50, 50))
        self.forest = load_image("forest.jpg")
        self.forest = pygame.transform.scale(self.forest, (50, 50))
        self.mount = load_image("mount.jpg")
        self.mount = pygame.transform.scale(self.mount, (50, 50))
        self.text = text_format("Деревня  " + self.f + self.p + self.s + self.w, 40, (255, 255, 255))
        self.activ_cell = text_format("", 45, (255, 255, 255))
        self.next_image = load_image("next.jpg")
        self.next_image = pygame.transform.scale(self.next_image, (70, 50))
        self.all_clicks = [[[], []]]
        self.check_reverse_list = 1
        self.day = 1

        self.image_viking = load_image("image_viking.jpg")
        self.image_viking = pygame.transform.scale(self.image_viking, (50, 50))

        self.image_get = load_image("image_get.jpg")
        self.image_get = pygame.transform.scale(self.image_get, (150, 50))

        self.wood_image = load_image("wood.jpg").convert_alpha()
        self.stone_image = load_image("stone.jpg")
        self.food_image = load_image("food.jpg")
        self.people_image = load_image("people.jpg")

        self.wood_image = pygame.transform.scale(self.wood_image, (30, 30))
        self.stone_image = pygame.transform.scale(self.stone_image, (30, 30))
        self.food_image = pygame.transform.scale(self.food_image, (30, 30))
        self.people_image = pygame.transform.scale(self.people_image, (30, 30))

        self.image_scissors = load_image("image_scissors.jpg")
        self.image_axe = load_image("image_axe.jpg")
        self.image_pickaxe = load_image("image_pickaxe.jpg")
        self.image_villagelol = load_image("villagelol.jpg")

        self.image_scissors = pygame.transform.scale(self.image_scissors, (30, 30))
        self.image_axe = pygame.transform.scale(self.image_axe, (30, 30))
        self.image_pickaxe = pygame.transform.scale(self.image_pickaxe, (30, 30))
        self.image_villagelol = pygame.transform.scale(self.image_villagelol
                                                       , (30, 30))

        self.image_settings = load_image("image_settings.jpg")
        self.image_settings = pygame.transform.scale(self.image_settings, (25, 25))

        self.text_error_people = ''

        self.use_pickaxes, self.use_axes, self.use_scissors = 0, 0, 0

        # создадим группу, содержащую спрайт кнопки добыть
        self.all_sprites_get_it = pygame.sprite.Group()
        # добавляем спрайты
        sprite = pygame.sprite.Sprite()
        sprite.image = self.image_get
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x = 350
        sprite.rect.y = 530
        self.sprite_get_it_rect = sprite.rect
        self.all_sprites_get_it.add(sprite)

        # создадим группу, содержащую спрайт кнопки next
        self.all_sprites_next = pygame.sprite.Group()
        # добавляем спрайты
        sprite = pygame.sprite.Sprite()
        sprite.image = self.next_image
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x = 600
        sprite.rect.y = 600
        self.sprite_next_rect = sprite.rect
        self.all_sprites_next.add(sprite)

        self.k = 1

    def render(self, screen):
        # button to main_menu
        pygame.draw.rect(screen, 'red',
                         (PLAYING_WINDOW_SIZE[0] - BTN_SIZE[0] - self.otstup,
                          self.otstup, BTN_SIZE[0],
                          BTN_SIZE[1]))
        pygame.draw.rect(screen, 'red', (650, 5, 100, 25))
        screen.blit(text_format("рекорды", 20, "white"), (662, 4))

        # pygame.draw.rect(screen, 'red', (320, 510, 50, 45))

        for x in range(self.width):
            for y in range(self.height):
                cell = self.board[y][x]
                if cell == 0:
                    screen.blit(self.grass,
                                (self.cell_size * x + self.left,
                                 y * self.cell_size + self.top))

                if cell == 1:
                    screen.blit(self.river,
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
                    screen.blit(Shop.Shop.image_village,
                                (self.cell_size * x + self.left,
                                 y * self.cell_size + self.top))

                if cell == 5:
                    screen.blit(self.image_viking,
                                (self.cell_size * x + self.left,
                                 y * self.cell_size + self.top))

        screen.blit(text_format(self.text_error_people, 30, "red"),
                    (500, 520))

        screen.blit(self.wood_image, (605, 50))
        screen.blit(self.stone_image, (645, 50))
        screen.blit(self.food_image, (685, 50))
        screen.blit(self.people_image, (725, 50))

        screen.blit(text_format(str(self.day), 45, "white"), (620, 550))
        self.all_sprites_next.draw(screen)
        self.all_sprites_get_it.draw(screen)
        try:
            if self.cell == 5:
                screen.blit(self.activ_cell, (10, 530))
            else:
                screen.blit(self.activ_cell, (60, 530))
        except:
            pass

        screen.blit(text_format(f"{str(Shop.AXES)}({str(self.use_axes)})", 20, "white"), (100, 600))
        screen.blit(text_format(f"{str(Shop.PICKAXES)}({str(self.use_pickaxes)})", 20, "white"),
                    (160, 600))
        screen.blit(text_format(f"{str(Shop.SCISSORS)}({str(self.use_scissors)})", 20, "white"),
                    (220, 600))
        screen.blit(text_format(f"{str(Shop.LVL_VILLAGE)}", 20, "white"), (280, 600))

        screen.blit(self.image_pickaxe, (160, 630))
        screen.blit(self.image_axe, (100, 630))
        screen.blit(self.image_scissors, (220, 630))
        screen.blit(self.image_villagelol, (270, 630))

        screen.blit(self.image_settings, (600, 5))

        tt = """3 3 3 3 3 3 3 3 3 3 3
3 3 3 3 3 3 3 3 3 3 3
0 2 1 2 0 0 0 0 0 0 0
0 2 1 2 0 0 0 0 0 0 0
0 2 1 2 0 0 4 0 0 0 5
0 2 1 2 0 0 0 0 0 0 0
0 2 1 2 0 0 0 0 0 0 0
0 2 1 2 0 0 0 2 2 2 0
0 2 1 2 0 0 0 2 2 2 0
0 2 1 2 0 0 0 2 2 2 0"""
        if self.day == 9:
            with open('board.txt', 'w') as f:
                f = f.write(tt)
            self.board.clear()
            with open('board.txt') as input_file:
                for line in input_file:
                    self.board.append(list(map(int, line.split())))

        if self.day == 10:
            self.results(screen)

        pygame.display.flip()

    def get_click(self, mouse_pos, screen):
        if 599 < mouse_pos[0] < 626 and 4 < mouse_pos[1] < 26:
            self.show_settings()

        if 649 < mouse_pos[0] < 751 and 4 < mouse_pos[1] < 26:
            self.show_records()

        # is it cell?
        get_it_rect = self.sprite_get_it_rect
        if not get_it_rect.collidepoint(pygame.mouse.get_pos()):
            self.activ_cell = text_format("", 30, "red")  # помогает изабивться от много кликов
        self.text_error_people = ""
        if self.left < mouse_pos[0] < self.width * self.cell_size + self.left and \
                self.top < mouse_pos[1] < self.height * self.cell_size + self.top:
            cell = self.get_cell(mouse_pos)
            self.all_clicks[0] = [cell, mouse_pos]
            self.on_click_cell(cell)
        # не надо каждый раз кликать на клетку
        if not (self.left < mouse_pos[0] < self.width * self.cell_size + self.left and \
                self.top < mouse_pos[1] < self.height * self.cell_size + self.top) and not (
                get_it_rect.collidepoint(pygame.mouse.get_pos())):
            self.all_clicks[0] = [[], []]
        # if 500 < mouse_pos[0] < 600 and 400 < mouse_pos[1] < 445:
        # self.mining(cell)  # кнопка добыть
        # is it quit btn?
        if PLAYING_WINDOW_SIZE[0] - BTN_SIZE[0] - self.otstup < mouse_pos[0] < PLAYING_WINDOW_SIZE[0] \
                - self.otstup and self.otstup < mouse_pos[1] < BTN_SIZE[1] + self.otstup:
            self.btn_quit_pressed()

        # кнопка следующий день
        next_rect = self.sprite_next_rect
        if next_rect.collidepoint(pygame.mouse.get_pos()):
            self.day += 1
            self.use_pickaxes, self.use_axes, self.use_scissors = 0, 0, 0

            # логика людей
            self.people += self.people_work
            self.people_work = 0
            need_food = self.people * 2
            remains = self.food - need_food
            if remains < 0:
                dead_people = abs(remains) / 2
                if dead_people > int(dead_people):
                    dead_people = int(dead_people) + 1
            else:
                dead_people = 0
            self.people -= dead_people

            self.food -= self.people * 2

            Shop.Shop().get_resources(Board())

        # кнопка добыть
        get_it_rect = self.sprite_get_it_rect
        if get_it_rect.collidepoint(pygame.mouse.get_pos()):
            pickaxes, axes, scissors = Shop.Shop().set_tools()
            # if self.k % 2 == 0:
            self.all_clicks.reverse()
            self.check_reverse_list += 1
            for click in self.all_clicks:
                if click[0] and click[1]:
                    if self.left < click[1][0] < self.width * self.cell_size + self.left and \
                            self.top < click[1][1] < self.height * self.cell_size + self.top:
                        x, y = click[0]
                        self.cell = self.board[y][x]
                        self.text_error_people = f""
                        if self.cell == 1:
                            self.people -= 1
                            self.people_work += 1
                            if self.people >= 0:
                                self.food += 2
                                if scissors - self.use_scissors > 0:
                                    self.food += 2
                                    self.use_scissors += 1
                        if self.cell == 2:
                            self.people -= 1
                            self.people_work += 1
                            if self.people >= 0:
                                self.wood += 10
                                if axes - self.use_axes > 0:
                                    self.wood += 5
                                    self.use_axes += 1
                        if self.cell == 3:
                            self.people -= 1
                            self.people_work += 1
                            if self.people >= 0:
                                self.stone += 10
                                if pickaxes - self.use_pickaxes > 0:
                                    self.stone += 5
                                    self.use_pickaxes += 1
                        if self.people < 0:
                            self.people += 1
                            self.people_work -= 1
                            self.text_error_people = f"Все люди уже заняты"
                        break
                # self.all_clicks.clear()

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
            self.activ_cell = text_format("Лес", 45, (255, 255, 255))
        if self.cell == 3:
            self.activ_cell = text_format("Горы", 45, (255, 255, 255))
        if self.cell == 4:
            self.activ_cell = text_format("Деревня", 45, (255, 255, 255))
        if self.cell == 5:
            tata = """Завтра на вашу деревню нападут"""
            self.activ_cell = text_format(tata, 24, (255, 255, 255))

    def btn_quit_pressed(self):
        # TODO: records and some statistic
        # to main menu
        Shop.PICKAXES, Shop.AXE, Shop.SCISSORS = 0, 0, 0

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

    def finish_game(self, text_end, day_10=False):
        if self.people <= 0 and self.people_work <= 0:
            text_end = text_format("Все люди умерли. Вы проиграли", 30, "red")

            screen = pygame.display.set_mode([800, 800])
            screen2 = pygame.display.set_mode([800, 800])
            running = True
            while running:

                screen.fill((0, 0, 0))

                screen.blit(text_end, [200, 400])

                pygame.draw.rect(screen, 'red', (650, 5, 100, 25))
                screen.blit(text_format("вернуться", 20, "white"), (662, 4))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos
                        if 649 < mouse_pos[0] < 751 and 4 < mouse_pos[1] < 26:
                            #MainMenu.Menu().start_game(f"{self.nickname}")
                            self.btn_quit_pressed()
                            running = False


        elif day_10:
            all_text_end = []
            for i in text_end:
                text_end = text_format(i, 30, "white")
                all_text_end.append(text_end)
            screen = pygame.display.set_mode([800, 800])
            running = True
            while running:

                k = 0
                screen.fill((0, 0, 0))
                for text_end in all_text_end:
                    screen.blit(text_end, [200, 300 + k])
                    k += 30
                k = 0

                pygame.draw.rect(screen, 'red', (650, 5, 110, 25))
                screen.blit(text_format("вернуться", 20, "white"), (662, 4))

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        quit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos
                        if 649 < mouse_pos[0] < 761 and 4 < mouse_pos[1] < 26:
                            main_menu = MainMenu.Menu()
                            main_menu.render(screen, event)
                            running = False

            with open("records.txt", "r") as gg:
                text = gg.read()

            with open("records.txt", "w") as gg:
                gg.write(text + f"{self.nickname}: {str(day_10)}" + "\n")

            with open("records.txt", "r") as gg:
                text = gg.readlines()
                text = list(map(lambda x: x.rstrip("\n"), text))
                end_text = list(
                    reversed(sorted(text, key=lambda x: int(x[len(x) - 4:]))))[0:10]

            with open("records.txt", "w") as gg:
                for i in end_text:
                    gg.write(i + '\n')

            Shop.LVL_VILLAGE = 0
            Shop.STONE, self.stone = 0, 0
            Shop.WOOD = 100
            Shop.FOOD = 100
            Shop.PEOPLE = 100
            Shop.AXES, Shop.PICKAXES, Shop.SCISSORS = 0, 0, 0

            Records.Records().to_main_menu()

    def results(self, screen):
        score_people = (self.people + self.people_work) * 10
        score_instruments = (Shop.AXES + Shop.PICKAXES + Shop.SCISSORS +
                             self.use_axes + self.use_pickaxes + self.use_scissors) * 5
        score_village = Shop.LVL_VILLAGE * 100
        score_day = self.day * 5
        score_all = score_people + score_instruments + score_village + score_day
        # print(score_all)

        if Shop.LVL_VILLAGE < 1:
            text_end = ["Ваш уровень деревни был слишком мал", "Вы не смогли защититься"]
        elif self.people + self.people_work < 20:
            text_end = ["У вас было слишком мало людей", "Вы не смогли защититься"]
        else:
            text_end = ["Поздравляем, вы смогли защититься",
                        f"Ваш результат: {str(score_all)} очков"]
        self.finish_game(text_end, score_all)

    def show_records(self):
        records = Records.Records()
        running = True
        screen = pygame.display.set_mode(WINDOW_SIZE)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                records.render(screen, event)

    def show_settings(self):
        screen = pygame.display.set_mode([800, 700])
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((0, 0, 0))

            text_settings = f"""Это экономическая игра, направленная на*
улучшение ваших прагматических навыков.*
Вам предоставлена деревня с жителями,*
вы её руководитель.*
Управляйте жителями для добычи ресурсов,*
используйте ресурсы для приобретения*
новых инструментов и улучшения деревни.*
О кнопках:*
Магазин: служит для приобретения товара*
Сверху над магазином показывается кол-во ваших ресурсов,*
на которые вы можете покупать нужные вам товары:*
1)Один топор даёт +5 дерева*
2)Одна кирка даёт +5 камня*
3)Одни ножницы дают +2 еды*
А так же кол-во людей, в скобках люди, которые уже работают*
Каждый человек ест по 2 еды в день. Иначе он умирает.*
Для добычи ресурсов требуется нажать на одну из клеток*
поля и далее нажать на кнопку "добыть".*
Цифры без скобок находящиеся рядом с картинками инструментов*
обознают их кол-во, а цифры в скобках обознают уже использованные*
инструменты за этот день. На следующий день купленные инструменты*
обновляются.*
Для перехода на следующий день следует нажать на оранжевую стрелку.*
Всего будет 10 дней. На 10 день на вашу деревню нападёт противник.*
Как подсчитываются очки:*
За каждого выжившего человека даётся + 10 очков*
За каждый купленный инструмент даётся +5 очков*
За каждый уровень дервени даётся +100 очков*
За каждый прожитый день даётся +5 очков*
Если все люди умирут, игра заканчится вашим поражением.*
Если в 10 день ваш уровень деревни будет меньше 1*
или кол-во людей меньше 20, то вы проиграете.*
"""

            kk = 0
            for i in text_settings.split("*"):
                text = text_format(i.lstrip(), 22, "white")
                screen.blit(text, [0, 0 + kk])
                kk += 21.8
            pygame.display.flip()

