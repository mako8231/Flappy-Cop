import pygame
from lib.sprite import Sprite

class Pipe():
    def __init__(self, path, x, y, altura):
        self.x = x 
        self.y = y + altura
        self.sprite = Sprite(path, self.x, self.y)
        self.pipe_parts = []
       
    def update(self, dt):
        self.x -= 10 * dt
        pass
    def draw(self):
        scaled_sprite = pygame.transform.scale(self.sprite.image, (self.sprite.rect.width*2, 
                                                                    self.sprite.rect.height*2))

        self.sprite.image = scaled_sprite
        self.sprite.x = self.x 
        self.sprite.y = self.y
        pass