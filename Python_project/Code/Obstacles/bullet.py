from typing import List
import pygame
import os
from Code.Obstacles.obstacle import Obstacle


BULLET = pygame.image.load(os.path.join("Python_project/Data/Images/Bullet", "Bullet.png"))

class Bullet(Obstacle):
    BULLET_VEL = 5
    def __init__(self, SCREEN_WIDTH: int):
        super().__init__(BULLET, SCREEN_WIDTH)
        self.rect.y = 200

    def update(self, game_speed: int, obstacles: List):
        self.rect.x -= game_speed + self.BULLET_VEL
        if self.rect.x < -self.rect.width:
            obstacles.pop()