import pygame

from Board import Board
from Main import load_image
from Main import text_format


class Shop(pygame.sprite.Sprite):
    image_shop = load_image("shop.png")
    image_rofl = load_image("rofl.jpg")
    image_tovar = pygame.transform.scale(load_image("tovar.jpg"), (150, 30))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Shop.image_shop
        self.image_transform_size = (150, 50)
        self.image = pygame.transform.scale(self.image, self.image_transform_size)
        self.image_rofl = Shop.image_rofl
        self.image_rofl = pygame.transform.scale(self.image_rofl, self.image_transform_size)

        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 100

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            pass
            # self.store_catalog()

    def store_catalog(self, screen):
        w, h = self.image_transform_size
        rect_store_catalog = (self.rect.x - 30, self.rect.y + h + 10, w + 60, 200)

        flag = True
        while flag:

            # спрайты (картинки товаров)
            # создаём группу спрайтов
            all_sprites = pygame.sprite.Group()

            x = self.rect.x - 16
            y = self.rect.y + h + 20
            # создаём и тут же добавляем спрайты в all_sprites
            for _ in range(4):
                sprite = pygame.sprite.Sprite()
                sprite.image = Shop.image_tovar
                sprite.rect = sprite.image.get_rect()

                sprite.rect.x = x
                sprite.rect.y = y

                all_sprites.add(sprite)

                y += 50

            # рисуем спрайты
            all_sprites.draw(screen)
            # рисуем рамку
            pygame.draw.rect(screen, "brown", rect_store_catalog, 5)
            pygame.display.flip()

            for event in pygame.event.get():
                if self.rect.collidepoint(
                        pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                    flag = not flag
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for tovar in all_sprites:
                        self.get_info_tovar(tovar, screen)

    def get_info_tovar(self, tovar, screen):
        rect = tovar.rect
        if rect.collidepoint(pygame.mouse.get_pos()):

            text = text_format("Поздравляю, вы долбаёб", 50, (0, 0, 0))
            screen.blit(text, (0, 600))
            text = text_format("Поздравляю, вы купили негра", 50, (0, 0, 0))
            screen.blit(text, (0, 600))
            text = text_format("Поздравляю, вы съели деда", 50, (0, 0, 0))
            screen.blit(text, (0, 600))
            text = text_format("Поздравляю!!!", 50, (0, 0, 0))
            screen.blit(text, (0, 600))

            if rect == (584, 170, 150, 30):
                text = text_format("Поздравляю, вы долбаёб", 50, (255, 255, 255))
            elif rect == (584, 220, 150, 30):
                text = text_format("Поздравляю, вы купили негра", 50, (255, 255, 255))
            elif rect == (584, 270, 150, 30):
                text = text_format("Поздравляю, вы съели деда", 50, (255, 255, 255))
            elif rect == (584, 320, 150, 30):
                text = text_format("Поздравляю!!!", 50, (255, 255, 255))
            screen.blit(text, (0, 600))

    def return_rect(self):
        return self.rect
