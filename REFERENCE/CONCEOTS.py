import pygame
x = pygame.init()

#                                           Window
gameWindow = pygame.display.set_mode((700, 400))
pygame.display.set_caption("My First Game")


#                                     specific veriables
exit_game = False
game_over = False


#                                        Game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("Pressed -->")
            elif event.key == pygame.K_UP:
                print("Pressed /\\")


#                                          QUIT
pygame.quit()
quit()