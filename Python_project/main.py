import pygame
import random
from Code.Obstacles.snake import Snake
from Code.Obstacles.virus import Virus
from Code.Obstacles.bullet import Bullet
from Code.Background.ground import Ground
from Code.menu import menu
from Code.mario import Mario
from Code.Background.cloud import Cloud
from Code.highscore import store_highscore

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main(highscore):
    global game_speed, points
    run = True
    game_speed = 7
    X_POS_BG = 0
    Y_POS_BG = 380
    points = 0
    death_count = 0
    clock = pygame.time.Clock()
    player = Mario()
    clouds = [Cloud(SCREEN_WIDTH) for i in range(5)]
    
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    ground = Ground(X_POS_BG, Y_POS_BG)
    

    def score(highscore):
        global points, game_speed
        points += 1        
        if points % 100 == 0:
            game_speed += 0.5
        if points > highscore:
            highscore = points
        text = font.render("Highscore: " + str(highscore) + "  Points: " + str(points), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (900, 40)
        SCREEN.blit(text, textRect)
        return highscore

    # Main Game LOOP
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                exit()
        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()    

        #Creation of Obstacles
        if len(obstacles) == 0:
            if random.randint(0,2) == 0:
                obstacles.append(Virus(SCREEN_WIDTH))
            elif random.randint(0,2) == 1:
                obstacles.append(Snake(SCREEN_WIDTH))
            elif random.randint(0,2) == 2:
                obstacles.append(Bullet(SCREEN_WIDTH))
        
        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(game_speed, obstacles)
            if player.mario_rect.colliderect(obstacle.rect):
                pygame.time.delay(100)
                death_count += 1    
                store_highscore(highscore)            
                menu(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, death_count, points)

        ground.draw(SCREEN)
        ground.update(game_speed)

        for cloud in clouds:
            cloud.draw(SCREEN)
            cloud.update(game_speed, SCREEN_WIDTH)

        player.draw(SCREEN)
        player.update(userInput)

        highscore = score(highscore)

        clock.tick(60)
        pygame.display.update()



menu(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, death_count = 0, points = 0)
