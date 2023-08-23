import pygame 
from lib.pipe import Pipe
from numpy import random

#PARAMETROS DO CANO
PIPE_DOWN_X = 800
PIPE_DOWN_Y = 4

PIPE_UP_X = 800
PIPE_UP_Y = 430

MAX_INTERVALO = 2

class Spawner():
    def __init__(self, up_pipe_path, down_pipe_path, all_sprites, player):
        self.pipes = []
        self.player = player 
        self.up_pipe_path = up_pipe_path
        self.down_pipe_path = down_pipe_path
        self.intervalo = 0
        self.all_sprites = all_sprites
    def update(self, dt):
        self.intervalo += dt
        if self.intervalo > MAX_INTERVALO and self.player.alive == True:
            self.intervalo = 0 
            #gerar dois canos de alturas aleatórias a cada intervalo de tempo
            up_pipe = Pipe(self.up_pipe_path, PIPE_UP_X, PIPE_UP_Y, random.randint(-20, 70), self.player)
            down_pipe = Pipe(self.down_pipe_path, PIPE_DOWN_X, PIPE_DOWN_Y, random.randint(-80, 0), self.player)
            
            self.all_sprites.add(up_pipe.sprite)
            self.all_sprites.add(down_pipe.sprite)
            
            self.pipes.append(up_pipe)
            self.pipes.append(down_pipe)

            #removendo os canos do limite da tela
            for pipe in self.pipes:
                if pipe.sprite.rect.right < 0:
                    pipe.sprite.kill
                    self.pipes.remove(pipe)
        pass
    def draw(self):
        if len(self.pipes) > 0:
            for pipe in self.pipes:
                pipe.draw()
        pass

    
    