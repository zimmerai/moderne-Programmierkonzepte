import pygame
import os
from Code.Obstacles.obstacle import Obstacle


SNAKE = pygame.image.load(os.path.join("Python_project/Data/Images/Enemy", "Enemy1_coloured.png"))   

class Snake(Obstacle):
    def __init__(self, SCREEN_WIDTH: int):
        super().__init__(SNAKE, SCREEN_WIDTH)
        self.rect.y = 290