import pygame
import random
import os


pygame.init()
clock = pygame.time.Clock()

def game_loop():

    base = (255, 200, 100)
    color = (0, 255, 255)
    border = (0, 255, 0)
    score_board = (0, 0, 0)
    game_over_color = (255, 255, 255)
    oth_score = (100, 200, 100)

    val_x = random.randint(2, 4)
    val_y = random.randint(2, 4)
    speed_increase = 2

    pos_x = 20
    pos_y = random.randint(20, 460)


    #Racket
    rac_color = (100, 0, 255)
    racX = 490
    racY = 200


    #variables
    exit_game = False
    score = 0

    
    if not os.path.exists('highscore_pong.txt'):
       with open('highscore_pong.txt', 'w') as file:
           file.write("0")
    with open("highscore_pong.txt", "r") as file:
        high_score = file.read()

    game_over = False


    #screen
    window = pygame.display.set_caption('PING-PONG by Pathik Sarkar')
    window = pygame.display.set_mode((500, 500))

    front = pygame.font.SysFont(None, 20)
    def text_screen(text, color, x, y):
        screen_text = front.render(text, True, color)
        window.blit(screen_text, (x, y)) #updates screen

    while not exit_game:

        if game_over == True:
            with open("highscore_pong.txt", "w") as file:
                file.write(str(high_score))

            text_screen("GANEOVER    ||    Press Enter to re-start", game_over_color, 150, 200)
            text_screen(f"HIGHSCORE : {high_score}", oth_score, 205, 260)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    game_loop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN and game_over == False:
                    if event.key == pygame.K_UP:
                        if racY != 0:
                            racY = racY - 40
                    if event.key == pygame.K_DOWN:
                        if racY != 400:
                            racY = racY + 40


            pos_x = pos_x + val_x
            pos_y = pos_y + val_y



            window.fill(base)
            pygame.draw.rect(window, border, [0, 0, 3, 500])
            pygame.draw.rect(window, border, [0, 497, 500, 3])
            pygame.draw.rect(window, border, [0, 0, 500, 3])

            text_screen("SCORE:  "+ str(score), score_board, 224, 245)

            pygame.draw.rect(window, color, [pos_x, pos_y , 20, 20]) 
            pygame.draw.rect(window, rac_color, [racX, racY, 10, 100])
            pygame.display.update()
            clock.tick(50)

            if pos_x < 1:
                val_x = val_x+speed_increase if val_x>0 else -(val_x+speed_increase)
                pygame.mixer.music.load('Bouncing.mp3')
                pygame.mixer.music.play()
            elif pos_x > 500-19:
                if (pos_y+20 > racY and pos_y< racY+100) and pos_x < 500:
                    score = score+5
                    val_x = -(val_x+speed_increase) if val_x>0 else val_x+speed_increase
                    pygame.mixer.music.load('Bouncing.mp3')
                    pygame.mixer.music.play()
                else:
                    if score>int(high_score):
                        high_score = score
                    pygame.mixer.music.load('GameOver.mp3')
                    pygame.mixer.music.play()
                    game_over = True

            if pos_y < 0:
                val_y = val_y+speed_increase if val_y>0 else -(val_y+speed_increase)
                pygame.mixer.music.load('Bouncing.mp3')
                pygame.mixer.music.play()
            elif pos_y > 500-19:
                val_y = -(val_y+speed_increase) if val_y>0 else val_y+speed_increase
                pygame.mixer.music.load('Bouncing.mp3')
                pygame.mixer.music.play()

        pygame.display.update()

    pygame.quit()
    quit()

highScore = game_loop()