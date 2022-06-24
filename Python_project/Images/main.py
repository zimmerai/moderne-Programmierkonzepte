import pygame
import os

pygame.init()

#GlobalConstants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("Images/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Images/Dino", "DinoRun2.png"))]

JUMPING = [pygame.image.load(os.path.join("Images/Dino", "DinoJump.png"))]

DUCKING = [pygame.image.load(os.path.join("Images/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Images/Dino", "DinoDuck2.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("Images/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Images/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Images/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("Images/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Images/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Images/Cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("Images/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Images/Bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("Images/Other", "Cloud.png"))

BG = pygame.image.load(os.path.join("Images/Other", "Track.png"))

class Dinosaur:
    X_POS = 80
    Y_POS = 310

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run
        if self.dino_jump:
            self.jump

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False

    def duck(self):

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        pass

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))



def main():
    run = True
    clock = pygame.time.clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        clock.tick(30)
        pygame.display.update()
