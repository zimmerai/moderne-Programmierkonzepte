import os
import pygame

RUNNING = [pygame.image.load(os.path.join("Python_project/Data/Images/Mario", "Mario1_run.png")),
           pygame.image.load(os.path.join("Python_project/Data/Images/Mario", "Mario2_run.png"))]

JUMPING = pygame.image.load(os.path.join("Python_project/Data/Images/Mario", "Mario1_run.png"))

DUCKING = [pygame.image.load(os.path.join("Python_project/Data/Images/Mario", "Mario1_duck.png")),
           pygame.image.load(os.path.join("Python_project/Data/Images/Mario", "Mario2_duck.png"))]

class Mario:

    X_POS = 80
    Y_POS = 260
    Y_POS_DUCK = 300
    JUMP_VEL = 8.5
    JUMP_GRAVITY = 0.8
    JUMP_TIMER_COOLDOWN = 10

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.mario_duck = False
        self.mario_run = True
        self.mario_jump = False        
        self.mario_jump_timer = self.JUMP_TIMER_COOLDOWN
        self.mario_jump_count = 0

        self.step_index = 0 #for the Animation
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.mario_rect = self.image.get_rect()
        self.mario_rect.x = self.X_POS
        self.mario_rect.y = self.Y_POS

    def update(self, userInput):
        if self.mario_duck:
            self.duck()
        if self.mario_run:
            self.run()
        if self.mario_jump:
            self.jump()

        if self.step_index >= 20:
            self.step_index = 0

        #Interaction with User / Events
        if (userInput[pygame.K_SPACE] or userInput[pygame.K_UP] or userInput[pygame.K_w]) and (self.mario_jump_timer == self.JUMP_TIMER_COOLDOWN or self.mario_jump_timer < 0) and self.mario_jump_count <= 2: 
            self.onJump()         

        elif (userInput[pygame.K_DOWN] or userInput[pygame.K_s]) and not self.mario_jump:
            self.mario_run = False
            self.mario_jump = False
            self.mario_doubleJump = False
            self.mario_duck = True

        elif not (self.mario_jump or userInput[pygame.K_DOWN] or userInput[pygame.K_s] ): 
            self.mario_run = True
            self.mario_jump = False
            self.mario_duck = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 10]
        self.mario_rect = self.image.get_rect()
        self.mario_rect.x = self.X_POS
        self.mario_rect.y = self.Y_POS_DUCK
        self.step_index += 1    

    def run(self):
        self.image = self.run_img[self.step_index // 10]
        self.mario_rect = self.image.get_rect()
        self.mario_rect.x = self.X_POS
        self.mario_rect.y = self.Y_POS
        self.step_index += 1

    def onJump(self):
        self.mario_duck = False
        self.mario_run = False           
        self.jump_vel = self.JUMP_VEL     
        self.mario_jump = True
        self.mario_jump_count += 1

    def jump(self):
        self.image = self.jump_img
        if self.mario_jump:
            self.mario_rect.y -= self.jump_vel * 2
            self.jump_vel -= self.JUMP_GRAVITY
            self.mario_jump_timer -= 1            
        if self.mario_rect.y >= self.Y_POS:
            self.mario_jump = False
            self.mario_jump_count = 0
            self.mario_jump_timer = self.JUMP_TIMER_COOLDOWN
            self.jump_vel = self.JUMP_VEL
        
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.mario_rect.x, self.mario_rect.y))