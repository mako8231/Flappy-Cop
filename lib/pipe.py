import pygame
from lib.sprite import Sprite

class Pipe():
    def __init__(self, path, x, y, altura, player):
        self.x = x 
        self.y = y + altura
        self.sprite = Sprite(path, self.x, self.y)
        self.player = player

        scaled_sprite = pygame.transform.scale(self.sprite.image, (self.sprite.rect.width*2, 
                                                                    self.sprite.rect.height*2))
        
        self.sprite.image = scaled_sprite
        self.sprite.rect = scaled_sprite.get_rect(center=self.sprite.rect.center)
        
       
    def update(self, dt):
        if self.sprite.rect.colliderect(self.player.sprite.rect):
            self.player.alive = False 
      
        if self.player.alive:
            self.x -= 170 * dt
        pass
    def draw(self):
        self.sprite.rect.x = self.x 
        self.sprite.rect.y = self.y
        pass