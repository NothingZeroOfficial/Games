import pygame
pygame.init()
clock = pygame.time.Clock()

white = (255, 255, 255)
bracket = (55, 0, 0)
color = (0, 255, 255)

val_x = 3
val_y = 2
speed_increase = 2

pos_x = 20
pos_y = 20

#variables
exit_game = False


#screen
window = pygame.display.set_caption('pong-bounce')
window = pygame.display.set_mode((500, 500))

pygame.display.update()

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True


    pos_x = pos_x + val_x
    pos_y = pos_y + val_y



    window.fill(white) # comment this line to get line as output insted of object
    pygame.draw.rect(window, bracket, [0, 0, 3, 500])

    pygame.draw.rect(window, color, [pos_x, pos_y , 20, 20]) 
    pygame.display.update()
    clock.tick(50)

    if pos_x < 1:
        val_x = val_x+speed_increase if val_x>0 else -(val_x+speed_increase)

    elif pos_x > 500-19:
        val_x = -(val_x+speed_increase) if val_x>0 else val_x+speed_increase

    if pos_y < 0:
        val_y = val_y+speed_increase if val_y>0 else -(val_y+speed_increase)
    elif pos_y > 500-19:
        val_y = -(val_y+speed_increase) if val_y>0 else val_y+speed_increase



pygame.quit()
quit()