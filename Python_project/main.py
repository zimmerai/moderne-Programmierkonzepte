from email.mime import image
import pygame
import os
import random
from threading import Timer

pygame.init()

#GlobalConstants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("Python_project/Images/Mario", "Mario1_run.png")),
           pygame.image.load(os.path.join("Python_project/Images/Mario", "Mario2_run.png"))]

JUMPING = pygame.image.load(os.path.join("Python_project/Images/Mario", "Mario1_run.png"))

DUCKING = [pygame.image.load(os.path.join("Python_project/Images/Mario", "Mario1_duck.png")),
           pygame.image.load(os.path.join("Python_project/Images/Mario", "Mario2_duck.png"))]

VIRUS = [pygame.image.load(os.path.join("Python_project/Images/Enemy", "Enemy2_coloured.png"))]
                #pygame.image.load(os.path.join("Python_project/Images/Enemy", "Enemy2_coloured.png"))]
                #pygame.image.load(os.path.join("Python_project/Images/Cactus", "SmallCactus3.png"))]
SNAKE = [pygame.image.load(os.path.join("Python_project/Images/Enemy", "Enemy1_coloured.png"))]
                #pygame.image.load(os.path.join("Python_project/Images/Cactus", "LargeCactus2.png")),
                #pygame.image.load(os.path.join("Python_project/Images/Cactus", "LargeCactus3.png"))]

BULLET = [pygame.image.load(os.path.join("Python_project/Images/Bullet", "Bullet.png"))]
        #pygame.image.load(os.path.join("Python_project/Images/Bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("Python_project/Images/Other", "Cloud.png"))

BG = pygame.image.load(os.path.join("Python_project/Images/Other", "Track.png"))

class Dinosaur:
    X_POS = 80
    Y_POS = 260
    Y_POS_DUCK = 300
    JUMP_VEL = 8.5
    JUMP_GRAVITY = 1.4
    TIMER_COOLDOWN = 5

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dinoFirstJump = False
        self.dinoSecondJump = False
        self.jumpTimer = 0
        self.dinoJumpCount = 0

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dinoFirstJump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if (userInput[pygame.K_SPACE] or userInput[pygame.K_UP]) and not self.dinoSecondJump and (self.jumpTimer == 0 or self.jumpTimer > self.TIMER_COOLDOWN) and self.dinoJumpCount <= 2: 
            self.onJump()         

        elif userInput[pygame.K_DOWN] and not self.dinoFirstJump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_doubleJump = False
            self.dino_duck = True

        elif not (self.dinoFirstJump or userInput[pygame.K_DOWN]): 
            self.dino_run = True
            self.dinoFirstJump = False
            self.dino_duck = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1    


    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def onJump(self):
        self.dino_duck = False
        self.dino_run = False           
        self.jump_vel = self.JUMP_VEL     
        self.dinoFirstJump = True
        self.dinoJumpCount += 1

    def jump(self):
        self.image = self.jump_img
        if self.dinoFirstJump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= self.JUMP_GRAVITY
            self.jumpTimer += 1
            print(str(self.jumpTimer))
        if self.dino_rect.y >= self.Y_POS:
            self.dinoFirstJump = False
            self.dinoSecondJump = False
            self.dinoJumpCount = 0
            self.jumpTimer = 0
            self.jump_vel = self.JUMP_VEL
        
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

class Cloud:
    CLOUD_DELAY = 12
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(50, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed-self.CLOUD_DELAY
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(50, 1000)
            self.y = random.randint(50, 200)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        
    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()
        
    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class Virus(Obstacle):
    def __init__(self, image):
        #self.type = random.randint(0,1)
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 325

class Snake(Obstacle):
    def __init__(self, image):
       # self.type = random.randint(0,1)
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 260

class Bullet(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 220
        self.index = 0

    #def draw(self, SCREEN):
        #if self.index >= 9:
        #    self.index = 0
        #SCREEN.blit(self.image, self.rect)
        #self.index += 1

def main(highscore):
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    clouds = [Cloud(), Cloud(), Cloud(), Cloud(), Cloud()]
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0    
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0

    def score(highscore):
        global points, game_speed
        points += 1        
        if points % 100 == 0:
            game_speed += 1
        if points > highscore:
            highscore = points
        text = font.render("Highscore: " + str(highscore) + "  Points: " + str(points), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (900, 40)
        SCREEN.blit(text, textRect)
        return highscore

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                exit()
        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()    

        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0,2) == 0:
                obstacles.append(Virus(VIRUS))
            elif random.randint(0,2) == 1:
                obstacles.append(Snake(SNAKE))
            elif random.randint(0,2) == 2:
                obstacles.append(Bullet(BULLET))
        
        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):
                #pygame.draw.rect(SCREEN, (255, 0, 0), player.dino_rect, 2)
                pygame.time.delay(100)
                death_count += 1                
                menu(death_count, highscore)

        background()

        for cloud in clouds:
            cloud.draw(SCREEN)
            cloud.update()

        highscore = score(highscore)

        clock.tick(30)
        pygame.display.update()

def menu(death_count, highscore):
    global points
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
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
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 -20, SCREEN_HEIGHT // 2 -140))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                exit()
            if event.type == pygame.KEYDOWN:
                print("Keydown ist pressed")
                main(highscore)

menu(death_count = 0, highscore=0)
