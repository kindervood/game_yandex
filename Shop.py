import pygame

from Board import Board
from Main import load_image
from Main import text_format

import threading
import time

WOOD, STONE, FOOD, PEOPLE = 100, 100, 100, 10


class Shop(pygame.sprite.Sprite):
    image_shop = load_image("shop.png")
    image_tovar = pygame.transform.scale(load_image("tovar.jpg"), (150, 30))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Shop.image_shop
        self.image_transform_size = (150, 50)
        self.image = pygame.transform.scale(self.image, self.image_transform_size)

        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 100

    def render(self, all_sprites_tovar, rect_store_catalog, message, screen):
        # рисуем спрайты товаров
        all_sprites_tovar.draw(screen)
        # рисуем рамку
        pygame.draw.rect(screen, "brown", rect_store_catalog, 5)
        # пишем текст с событием
        message = text_format(f"{message}", 50, (255, 255, 255))
        screen.blit(message, (0, 600))


    def store_catalog(self, screen, object):
        w, h = self.image_transform_size
        rect_store_catalog = (self.rect.x - 30, self.rect.y + h + 10, w + 60, 200)

        all_sprites_tovar = pygame.sprite.Group()

        x = self.rect.x - 16
        y = self.rect.y + h + 20
        # создаём и тут же добавляем спрайты в all_sprites
        for _ in range(4):
            sprite = pygame.sprite.Sprite()
            sprite.image = Shop.image_tovar
            sprite.rect = sprite.image.get_rect()

            sprite.rect.x = x
            sprite.rect.y = y

            all_sprites_tovar.add(sprite)

            y += 50

        return all_sprites_tovar, rect_store_catalog

    def get_info_tovar(self, tovar, screen, object):
        global WOOD, FOOD, STONE, PEOPLE
        text = ""
        rect = tovar.rect
        all_sprites_tovar, rect_store_catalog = self.store_catalog(screen, object)
        if rect.collidepoint(pygame.mouse.get_pos()):
            k = 0
            for i in all_sprites_tovar:
                k += 1

                if rect == i.rect and k == 1:
                    text = "Вы потратили 10 дерева"
                    WOOD = self.check_less_zero("дерева", WOOD, 10, screen)
                    break
                elif rect == i.rect and k == 2:
                    text = "Вы потратили 10 камня"
                    STONE = self.check_less_zero("камня", STONE, 10, screen)
                    break
                elif rect == i.rect and k == 3:
                    text = "Вы потратили 10 еды"
                    FOOD = self.check_less_zero("еды", FOOD, 10, screen)
                    break
                elif rect == i.rect and k == 4:
                    text = "Ничего не произошло"
                    break
            self.set_resources(object)
            return text
            # self.resources(screen)
        return text

    def check_less_zero(self, name_resource, resource, deductible, screen):
        if resource - deductible < 0:
            text_error = text_format(f"У вас недостаточно {name_resource}", 15, "red")

            w, h = self.image_transform_size

            screen.blit(text_error, (self.rect.x - 37, self.rect.y + h + 215))
            pygame.display.flip()
            # занести в поток
            time.sleep(2)
            text_error = text_format(f"У вас недостаточно {name_resource}", 15, "black")
            #####
            screen.blit(text_error, (self.rect.x - 37, self.rect.y + h + 215))
            return resource
        return resource - deductible

    def get_resources(self, object):
        global WOOD, STONE, FOOD, PEOPLE
        try:
            WOOD, STONE, FOOD, PEOPLE = object.wood, object.stone, object.food, object.people
        except:
            pass

    def set_resources(self, object):
        global WOOD, STONE, FOOD, PEOPLE
        try:
            object.wood, object.stone, object.food, object.people = WOOD, STONE, FOOD, PEOPLE
        except:
            pass
