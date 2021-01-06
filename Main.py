import pygame
from Board import Board
from MainMenu import Menu
import shop

WINDOW_SIZE = 600, 600

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    main_menu = Menu()
    running = True
    
    #часть кода Андрея
    board = Board(25, 25)
    screen.fill((0, 0, 0))
    board.render()
    
    # создадим группу, содержащую все спрайты
    all_sprites = pygame.sprite.Group()
    # получим картинку(surface)
    shop_image = load_image("shop.png")
    # добавляем спрайты
    for _ in range(1):
        shop.Shop(all_sprites)
    # рисуем все спрайты на screen
    all_sprites.draw(screen)

    pygame.display.flip()

    while running:
        
        screen.fill((0, 0, 0))
        board.render()

        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
                all_sprites.update(event)

            main_menu.render(screen, event)
