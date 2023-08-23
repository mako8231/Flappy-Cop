import pygame
import sys
import os 
import json
from lib.sprite import Sprite
from lib.player import Player
from lib.pipe import Pipe
from lib.spawner import Spawner

# Initialize pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FlappyCop")

#bird 
bird_spr = 'assets/char.png'

#grupo de sprites
all_sprites = pygame.sprite.Group()

#objetos 
player = Player(100, 100, bird_spr)
spawner = Spawner('assets/pipe_up_top.png', 'assets/pipe_upside_down.png', all_sprites, player)
objects = []
objects.append(player)

paralax_0 = pygame.image.load('assets/paralax.png')
paralax_0_scaled = pygame.transform.scale(paralax_0, (800, 600))

paralax_1 = pygame.image.load('assets/paralax_1.png')
paralax_1_scaled = pygame.transform.scale(paralax_1, (800, 600))


background_images = [
    paralax_1_scaled,
    paralax_0_scaled
]

background_positions = [0, 0]
background_speeds = [0.4, 0.8]

#score
score = 0
max_score = 0

for obj in objects:
    all_sprites.add(obj.sprite)

# Colors
gray = (127, 127, 127)
black = (0, 0, 0)

# Game loop
clock = pygame.time.Clock()
running = True
tempo_anterior = pygame.time.get_ticks()

#processar texto
font = pygame.font.Font(None, 36)

#controle de inputs do teclado
def input_events():
    pass

#loop de controle da lógica do jogo
def update(dt:float):
    for object in objects:
        object.update(dt)
    spawner.update(dt)

    if (len(spawner.pipes) > 0):
        for pipe in spawner.pipes: 
            pipe.update(dt)    
    
    pass
 
def restart_game(player, spawner):
    for pipe in spawner.pipes:
        pipe.sprite.kill
        all_sprites.remove(pipe.sprite)
    
    spawner.pipes.clear()
    player.y = 100
    player.alive = True 

def load_file(path):
    if os.path.exists(path):
        with open(path, 'r') as file:
            data = json.load(file)
        return data['max_score'] 
    return 0
        

def save_file(path):
    if os.path.exists(path):
        with open(path, 'r') as file:
            data = json.load(file)
        
        data['max_score'] = max_score
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
    else: 
        data = {'max_score': max_score}
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)

#carregar o arquivo de max score 
max_score = load_file('save.json')
while running:
    #texto do score 
    score_text = font.render("Score: {}".format(int(score)), False, (255, 255, 255))
    score_text_rect = score_text.get_rect(center=(100, 60))

    
    m_score_text = font.render("Max Score: {}".format(int(max_score)), False, (255, 255, 255))
    m_score_text_rect = m_score_text.get_rect(center=(100, 100))

    #mostrar a frase GAME OVER quando o player morrer" 
    game_over = font.render("Aperte R para continuar.".format(int(score)), False, (255, 255, 255))
    game_over_rect = game_over.get_rect(center=(screen_width//2, screen_height//2))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and player.alive:
            if event.key == pygame.K_SPACE:
                player.velocidade['y'] = -5
            if event.key == pygame.K_z:
                player.velocidade['y'] = -5
        if event.type == pygame.KEYDOWN and not player.alive:
            if event.key == pygame.K_r:
                restart_game(player, spawner)
                save_file('save.json')
                score = 0
        

    # Clear the screen
    screen.fill(gray)

    # Draw game elements
    # ... (your drawing code here)

    for i in range(len(background_images)):
        if player.alive:
            background_positions[i] -= background_speeds[i]    

    for i, position in enumerate(background_positions):
        bg_width = background_images[i].get_width()
        screen.blit(background_images[i], (position%bg_width - bg_width, 0))
        screen.blit(background_images[i], (position%bg_width, 0))
     

    for object in objects:
        object.draw()
    if (len(spawner.pipes) > 0):
        for pipe in spawner.pipes: 
            pipe.draw()    
    #desenhar os objetos
    all_sprites.draw(screen)
    screen.blit(m_score_text, m_score_text_rect)
    screen.blit(score_text, score_text_rect)

    if not player.alive:
        screen.blit(game_over, game_over_rect)

    #calculando o delta-time 
    tempo_atual = pygame.time.get_ticks()
    dt = (tempo_atual - tempo_anterior) / 1000.0
    tempo_anterior = tempo_atual
    
    if player.alive:
        score += 1 * dt
        if max_score < score:
            max_score = score 

    update(dt)
    input_events()

    # Update the display
    pygame.display.flip()
    

    # Limit frames per second
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
