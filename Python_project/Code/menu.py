import os
import pygame

from Code.highscore import read_highscore


RUNNING = pygame.image.load(os.path.join("Python_project/Data/Images/Mario", "Mario1_run.png"))

def menu(SCREEN: pygame.Surface, SCREEN_WIDTH: int, SCREEN_HEIGHT: int, death_count: int, points: int):
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        highscore = read_highscore()        
        text_on_screen(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, death_count, points, highscore)          
        pygame.display.update()
        events(highscore)
        

def text_on_screen(SCREEN: pygame.Surface, SCREEN_WIDTH: int, SCREEN_HEIGHT: int,death_count: int, points: int, highscore: int):
            font = pygame.font.Font('freesansbold.ttf', 30)
            
            if death_count == 0:                 
                text = font.render("Press any key to start", True, (0,0,0))            
            elif death_count > 0:
                text = font.render("Press any key to restart", True, (0,0,0))
                score = font.render("Your Score: " + str(points), True, (0,0,0))
                scoreRect = score.get_rect()
                scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
                SCREEN.blit(score, scoreRect)
                highscoreText = font.render("Your Highscore: " + str(highscore), True, (0,0,0))
                highscoreTextRect = highscoreText.get_rect()
                highscoreTextRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
                SCREEN.blit(highscoreText, highscoreTextRect)
                
            textRect = text.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            SCREEN.blit(text, textRect)
            SCREEN.blit(RUNNING, (SCREEN_WIDTH // 2 -20, SCREEN_HEIGHT // 2 -140))

def events(highscore: int):
    from main import main #needs to be at this position (Otherwise: circular import)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            run = False
            exit()
        if event.type == pygame.KEYDOWN:
            main(highscore)