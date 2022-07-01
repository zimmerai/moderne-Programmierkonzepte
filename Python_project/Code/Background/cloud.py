import os
import random
import pygame


CLOUD = pygame.image.load(os.path.join("Python_project/Data/Images/Other", "Cloud.png"))

class Cloud:
    CLOUD_DELAY = 2
    def __init__(self, SCREEN_WIDTH: int):
        self.x = SCREEN_WIDTH + random.randint(50, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self, game_speed: int, SCREEN_WIDTH: int):
        self.x -= game_speed/2
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(50, 1000)
            self.y = random.randint(50, 200)

    def draw(self, SCREEN: pygame.Surface):
        SCREEN.blit(self.image, (self.x, self.y))