import random
import pygame

from main import load_image


class Shop(pygame.sprite.Sprite):
    image_shop = load_image("shop.png")
    image_rofl = load_image("rofl.jpg")

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = Shop.image_shop
        self.image_rofl = Shop.image_rofl
        self.rect = self.image.get_rect()
        self.rect.x = 770
        self.rect.y = 10

    def update(self, *args):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.image_rofl
