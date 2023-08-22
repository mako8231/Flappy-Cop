import pygame
import sys
from lib.sprite import Sprite
from lib.player import Player
from lib.pipe import Pipe

# Initialize pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame App")

#bird 
bird_spr = 'assets/char.png'

player = Player(100, 100, bird_spr)
pipe = Pipe('assets/pipe_up_top.png', 300, 400, 0)

#grupo de sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player.sprite)
all_sprites.add(pipe.sprite)

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Game loop
clock = pygame.time.Clock()
running = True
tempo_anterior = pygame.time.get_ticks()
#controle de inputs do teclado
def input_events():
    pass

#loop de controle da lógica do jogo
def update(dt:float):
    player.update(dt)
    pass

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.velocidade['y'] = -5

    # Clear the screen
    screen.fill(white)

    # Draw game elements
    # ... (your drawing code here)

    scaled_sprite_1 = pygame.transform.scale(player.sprite.image, (player.sprite.rect.width*2, player.sprite.rect.height*2))
    scaled_sprite_2 = pygame.transform.scale(pipe.sprite.image, (pipe.sprite.rect.width*2, pipe.sprite.rect.height*2))
    player.sprite.image = scaled_sprite_1
    pipe.sprite.image = scaled_sprite_2
    player.draw()
    all_sprites.draw(screen)


    #calculando o delta-time 
    tempo_atual = pygame.time.get_ticks()
    dt = (tempo_atual - tempo_anterior) / 1000.0
    tempo_anterior = tempo_atual

    update(dt)
    input_events()

    # Update the display
    pygame.display.flip()
    

    # Limit frames per second
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
