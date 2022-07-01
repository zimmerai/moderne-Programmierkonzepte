import pygame
import os


BG = pygame.image.load(os.path.join("Python_project/Data/Images/Other", "Track.png"))

class Ground:
    def __init__(self, x_pos_bg: int, y_pos_bg: int):
        self.image = BG
        self.image_width = BG.get_width()
        self.x_pos = x_pos_bg
        self.y_pos = y_pos_bg

    def draw(self, SCREEN: pygame.Surface):        
        SCREEN.blit(self.image, (self.x_pos, self.y_pos))
        SCREEN.blit(self.image, (self.image_width + self.x_pos, self.y_pos))
        
    def update(self, game_speed: int):
        if self.x_pos <= -self.image_width:            
            self.x_pos = 0
        self.x_pos -= game_speed