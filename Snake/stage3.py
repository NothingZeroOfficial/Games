import pygame
import random
import os

pygame.mixer.init()

pygame.init()



clock = pygame.time.Clock()
front = pygame.font.SysFont(None, 20)



#                                           LOOP
def game_loop():
                                         #specific veriables
    #colors

    exit_game = False
    game_over = False

    ground_color = (0, 255, 0)
    food_color = (255, 0, 10)
    snake_color = (150, 0, 255)
    score_board_color = (0, 0, 0)
    highscore_color =(100, 50, 100)
    fence_color = (100, 55, 0)
    game_over_color = (180, 0, 10)

    screen_width = 400
    screen_hight = 400
    fps = 20
    snake_x = 10
    snake_y = screen_width/2

    val_x = 0
    val_y = 0

    size_w = 10
    size_h = size_w

    food_x = random.randint(20, screen_width-20)
    food_y = random.randint(20, screen_hight-20)
    score = 0

    snk_list = []
    snk_leanth = 2


    if (not os.path.exists('highscore_snake.txt')):
       with open('highscore_snake.txt', 'w') as file:
           file.write("0")
    with open("highscore_snake.txt", "r") as file:
        highscore = file.read()


    #                                           Window
    gameWindow = pygame.display.set_mode((screen_width, screen_hight))
    pygame.display.set_caption('Snake - prototype   by Pathik Sarkar')
    pygame.display.update()

    def text_screen(text, color, x, y):
        screen_text = front.render(text, True, color)
        gameWindow.blit(screen_text, (x, y)) #updates screen

    def plot_snake(gameWindow, color, snk_list, size_w, size_h):
        for x, y in snk_list:
            pygame.draw.rect(gameWindow, color, [x, y, size_w, size_h])

    
    
    pygame.mixer.music.load("BackGroundMusic.mp3")
    pygame.mixer.music.play()


    while not exit_game:

        if game_over == True:

            with open("highscore_snake.txt", "w") as file:
                file.write(str(highscore))


            text_screen("GAME OVER! Press Enter to continue", game_over_color, (screen_width/2)-105, screen_hight/2)
            text_screen(f"HIGHSCORE : {highscore}", highscore_color, (screen_width/2)-50, (screen_hight/2)+20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    game_loop()


            
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and val_x == 0:
                        val_x = 5
                        val_y = 0
                    if event.key == pygame.K_LEFT and val_x == 0:
                        val_x = -5
                        val_y = 0

                    if event.key == pygame.K_UP and val_y == 0:
                        val_y = -5
                        val_x = 0
                    if event.key == pygame.K_DOWN and val_y == 0:
                        val_y = 5
                        val_x = 0

            snake_x = snake_x + val_x
            snake_y = snake_y + val_y

            if abs(snake_x - food_x)<8 and abs(snake_y-food_y)<8:
                score = score+5
                snk_leanth = snk_leanth+4
                if score>int(highscore):
                    highscore = score

                food_x = random.randint(20, screen_width-20)
                food_y = random.randint(20, screen_hight-20)


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_leanth:
                del snk_list[0]


#                                        GAME OVER
            if snake_x<3 or snake_x>screen_width-3 or snake_y<3 or snake_y>screen_hight-3:
                game_over = True
                pygame.mixer.music.load('GameOver.mp3')
                pygame.mixer.music.play()

            if head in snk_list[:-1] and score != 0:
                game_over = True
                pygame.mixer.music.load('GameOver.mp3')
                pygame.mixer.music.play()
                


            gameWindow.fill(ground_color)
            pygame.draw.rect(gameWindow, fence_color, [0, 0, 400, 4])
            pygame.draw.rect(gameWindow, fence_color, [0, 0, 3, 400])
            pygame.draw.rect(gameWindow, fence_color, [0, 397, 400, 3])
            pygame.draw.rect(gameWindow, fence_color, [397, 0, 3, 400])
            text_screen("SCORE: "+str(score), score_board_color, 5, 5)
            plot_snake(gameWindow, snake_color, snk_list, size_w, size_h)
            pygame.draw.rect(gameWindow, food_color, [food_x, food_y, 10, 10])
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

game_loop()