import pygame
from lib.sprite import Sprite

class Pipe():
    def __init__(self, path, x, y, altura):
        self.x = x 
        self.y = y
        self.sprite = Sprite(path, x, y)
        pass
    def update(self, dt):
        self.x -= 10 * dt
        pass
    def draw(self):
        self.sprite.x = self.x 
        pass