import pygame
import os
from Code.Obstacles.obstacle import Obstacle


VIRUS = pygame.image.load(os.path.join("Python_project/Data/Images/Enemy", "Enemy2_coloured.png"))

class Virus(Obstacle):
    def __init__(self, SCREEN_WIDTH: int):
        super().__init__(VIRUS, SCREEN_WIDTH)
        self.rect.y = 325