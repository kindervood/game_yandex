import pygame

# from Board import Board
from Main import load_image
from Main import text_format

WOOD, STONE, FOOD, PEOPLE, PEOPLE_WORK = 100, 100, 20, 10, 0
PICKAXES, AXES, SCISSORS = 0, 0, 0
LVL_VILLAGE = 0


class Shop(pygame.sprite.Sprite):
    image_shop = load_image("shop.png")
    image_tovar_pickaxe = pygame.transform.scale(load_image("pickaxe.jpg"), (204, 90))
    image_tovar_axe = pygame.transform.scale(load_image("axe.jpg"), (204, 90))
    image_tovar_scissors = pygame.transform.scale(load_image("scissors.jpg"), (204, 90))
    image_tovar_village_up1 = pygame.transform.scale(load_image("village_up1.jpg"), (204, 90))

    image_tovars_listen = [image_tovar_pickaxe, image_tovar_axe, image_tovar_scissors,
                           image_tovar_village_up1]

    image_village = load_image("vilage.jpg")
    image_village = pygame.transform.scale(image_village, (50, 50))

    image_village_up1 = load_image("village_lvl1.jpg")
    image_village_up1 = pygame.transform.scale(image_village_up1, (50, 50))

    image_village_up2 = load_image("village_lvl2.jpg")
    image_village_up2 = pygame.transform.scale(image_village_up2, (50, 50))

    image_villages_list = [image_village, image_village_up1, image_village_up2]

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Shop.image_shop
        self.image_transform_size = (150, 50)
        self.image = pygame.transform.scale(self.image, self.image_transform_size)

        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 100

        self.text_error = ""

        self.pickaxes = 0
        self.axes = 0
        self.scissors = 0
        self.tools = []

    def render(self, all_sprites_tovar, rect_store_catalog, message, text_error, screen):
        # рисуем спрайты товаров
        all_sprites_tovar.draw(screen)
        # рисуем рамку
        pygame.draw.rect(screen, "brown", rect_store_catalog, 5)
        # пишем текст с событием
        message = text_format(f"{message}", 50, (255, 255, 255))
        screen.blit(message, (0, 600))

        w, h = self.image_transform_size
        screen.blit(text_format(text_error, 20, "red"),
                    (self.rect.x - 105, self.rect.y + h + 365))


    def store_catalog(self, screen, object):
        w, h = self.image_transform_size
        rect_store_catalog = (self.rect.x - 30, self.rect.y + h + 0, w + 60, 363)

        all_sprites_tovar = pygame.sprite.Group()

        x = self.rect.x - 16
        y = self.rect.y + h + 3
        # создаём и тут же добавляем спрайты в all_sprites
        for tovarr in Shop.image_tovars_listen:
            sprite = pygame.sprite.Sprite()
            sprite.image = tovarr
            sprite.rect = sprite.image.get_rect()

            sprite.rect.x = x - 11
            sprite.rect.y = y

            all_sprites_tovar.add(sprite)

            y += 90

        return all_sprites_tovar, rect_store_catalog

    def get_info_tovar(self, tovar, screen, object):
        global WOOD, FOOD, STONE, PEOPLE, PICKAXES, AXES, SCISSORS, LVL_VILLAGE
        text = ""
        rect = tovar.rect
        all_sprites_tovar, rect_store_catalog = self.store_catalog(screen, object)
        action = 0
        if rect.collidepoint(pygame.mouse.get_pos()):
            k = 0
            for i in all_sprites_tovar:
                k += 1

                if rect == i.rect and k == 1:
                    # text = "Вы потратили 20 дерева и 20 камня"
                    WOOD, STONE = self.check_less_zero("дерева", "камня", WOOD, STONE, 20, 20,
                                                       screen)
                    action = 1
                    break
                elif rect == i.rect and k == 2:
                    # text = "Вы потратили 20 дерева и 20 камня"
                    WOOD, STONE = self.check_less_zero("дерева", "камня", WOOD, STONE, 20, 20,
                                                       screen)
                    action = 2
                    break
                elif rect == i.rect and k == 3:
                    # text = "Вы потратили 25 камня"
                    WOOD, STONE = self.check_less_zero("дерева", "камня", WOOD, STONE, 0, 25,
                                                       screen)
                    action = 3
                    break
                elif rect == i.rect and k == 4:
                    # text = "Вы потратили 60 дерева и 50 камня"
                    if not LVL_VILLAGE >= 2:
                        WOOD, STONE = self.check_less_zero("дерева", "камня", WOOD, STONE, 60, 50,
                                                           screen)
                    action = 4
                    break
            self.set_resources(object)
            if self.text_error:
                text = ""
                return text, self.text_error
            if action == 1:
                PICKAXES += 1
            if action == 2:
                AXES += 1
            if action == 3:
                SCISSORS += 1
            if action == 4:
                LVL_VILLAGE += 1
                if LVL_VILLAGE > 2:
                    self.text_error = 'Уровень деревени уже максимальный'
                    LVL_VILLAGE = 2
                else:
                    Shop.image_village = Shop.image_villages_list[LVL_VILLAGE]
                    PEOPLE += 10
                    self.set_resources(object)
            return text, self.text_error
        return text, self.text_error

    def check_less_zero(self, name_resource1, name_resource2, resource1, resource2, deductible1,
                        deductible2, screen):
        if (resource1 - deductible1 < 0) and (resource2 - deductible2 < 0):
            self.text_error = f"У вас недостаточно {name_resource1} и {name_resource2}"
            return resource1, resource2
        elif resource1 - deductible1 < 0:
            self.text_error = f"У вас недостаточно {name_resource1}"
            return resource1, resource2
        elif resource2 - deductible2 < 0:
            self.text_error = f"У вас недостаточно {name_resource2}"
            return resource1, resource2
        return resource1 - deductible1, resource2 - deductible2

    def get_resources(self, object):
        global WOOD, STONE, FOOD, PEOPLE, PEOPLE_WORK
        try:
            WOOD, STONE, FOOD, PEOPLE, PEOPLE_WORK = object.wood, object.stone, object.food, \
                                                     object.people, object.people_work
        except:
            pass

    def set_resources(self, object):
        global WOOD, STONE, FOOD, PEOPLE, PEOPLE_WORK
        try:
            object.wood, object.stone, object.food, \
            object.people, object.people_work = WOOD, STONE, FOOD, PEOPLE, PEOPLE_WORK
        except:
            pass

    def set_tools(self):
        global PICKAXES, AXES, SCISSORS
        return PICKAXES, AXES, SCISSORS
