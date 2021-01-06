import pygame

from Main import load_image


class Shop(pygame.sprite.Sprite):
    image_shop = load_image("shop.png")
    image_rofl = load_image("rofl.jpg")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Shop.image_shop
        self.image_rofl = Shop.image_rofl
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 100

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.image_rofl

            # СОЗДАТЬ ФУНКЦИЮ КОТОРАЯ ОТКРЫВАЕТ НОВОЕ ОКНО И НЕ ЗАКРЫВАЕТ
            # СТАРОЕ И В КОТОРОМ ТИПО МОЖНО БУДЕТ КУПИТЬ ЧТО ТО
