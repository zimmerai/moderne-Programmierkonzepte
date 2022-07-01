from typing import List
from pygame import Surface


class Obstacle:
    def __init__(self, image: Surface, SCREEN_WIDTH: int):
        self.image = image        
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        
    def update(self, game_speed: int, obstacles: List):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()
        
    def draw(self, SCREEN: Surface):
        SCREEN.blit(self.image, self.rect)