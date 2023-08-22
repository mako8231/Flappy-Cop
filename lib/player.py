import pygame 
from lib import sprite 
LINEAR_VEL = 10

class Player():
    def __init__(self, x, y, picture_path):
        self.x = x
        self.y = y
        self.velocidade = {'x':0, 'y':0}
        self.sprite = sprite.Sprite(picture_path, self.x, self.y)

    def update(self, dt):
        self.velocidade['y'] += LINEAR_VEL * dt 
        if self.velocidade['y'] > 10:
            self.velocidade['y'] = 10

        self.x += self.velocidade['x']
        self.y += self.velocidade['y'] 

    def input_handling(self):
        pass

    def draw(self):
        scaled_sprite = pygame.transform.scale(self.sprite.image, (self.sprite.rect.width*2, 
                                                                          self.sprite.rect.height*2))
        self.sprite.image = scaled_sprite
        self.sprite.rect.x = self.x 
        self.sprite.rect.y = self.y 
        
        pass