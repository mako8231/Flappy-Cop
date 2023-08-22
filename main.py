import pygame
import sys
from lib import sprite

# Initialize pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame App")

#bird 
bird_spr = 'assets/char.png'
sprite_x = 30
sprite_y = screen_height//2

#criar uma instância de sprite
bird_spr = sprite.Sprite(bird_spr, sprite_x, sprite_y)

#grupo de sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(bird_spr)

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(white)

    # Draw game elements
    # ... (your drawing code here)

    scaled_sprite = pygame.transform.scale(bird_spr.image, (bird_spr.rect.width*2, bird_spr.rect.height*2))
    bird_spr.image = scaled_sprite
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()
    

    # Limit frames per second
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
