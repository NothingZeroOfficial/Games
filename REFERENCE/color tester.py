import pygame
pygame.init()

while True:

    shade1 = float(input('1: '))
    shade2 = float(input('2: '))
    shade3 = float(input('3: '))

    print('\nColor ready\n\n')

    color = (shade1, shade2, shade3)

    plate = pygame.display.set_caption('Color-test')
    plate = pygame.display.set_mode((200,200))
    plate.fill(color)
    pygame.display.update()