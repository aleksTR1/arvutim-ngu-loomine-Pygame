import pygame
import random

# Initsialiseerime pygame
pygame.init()

# Määrame akna suuruse
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Aleks_Tagirov_Logitpv24")

# Määrame värvid
white = (255, 255, 255)
blue = (100, 100, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Mängija seaded
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - player_size - 10
player_speed = 7

# Takistuse seaded
obstacle_size = 50
obstacle_x = random.randint(0, screen_width - obstacle_size)
obstacle_y = -obstacle_size
obstacle_speed = 5

score = 0
game_over = False

clock = pygame.time.Clock()

# Mängu tsükkel
running = True
while running:
    # Sündmuste töötlus
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Ekraani täitmine valgega
    screen.fill(white)
    
    if not game_over:
        # Klaviatuuri sisendi töötlus
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        
        # Piirangud, et mängija aknast välja ei läheks
        if player_x < 0:
            player_x = 0
        if player_x > screen_width - player_size:
            player_x = screen_width - player_size
        
        # Takistuse liikumine
        obstacle_y += obstacle_speed
        if obstacle_y > screen_height:
            obstacle_y = -obstacle_size
            obstacle_x = random.randint(0, screen_width - obstacle_size)
            score += 1
        
        # Kokkupõrke tuvastamine
        if (player_x < obstacle_x + obstacle_size and
            player_x + player_size > obstacle_x and
            player_y < obstacle_y + obstacle_size and
            player_y + player_size > obstacle_y):
            game_over = True
        
        # Joonistamine
        pygame.draw.rect(screen, blue, (player_x, player_y, player_size, player_size))
        pygame.draw.rect(screen, red, (obstacle_x, obstacle_y, obstacle_size, obstacle_size))
        
        # Skoori kuvamine
        font = pygame.font.SysFont("Arial", 24)
        score_text = font.render(f"Skoor: {score}", True, black)
        screen.blit(score_text, (10, 10))
    else:
        # Mängu lõppekraan
        font_large = pygame.font.SysFont("Arial", 40)
        game_over_text = font_large.render("Mäng läbi!", True, black)
        restart_text = font.render("Vajuta R uuesti mängimiseks", True, black)
        score_text = font.render(f"Lõppskoor: {score}", True, black)
        
        screen.blit(game_over_text, (screen_width//2 - game_over_text.get_width()//2, screen_height//2 - 50))
        screen.blit(score_text, (screen_width//2 - score_text.get_width()//2, screen_height//2))
        screen.blit(restart_text, (screen_width//2 - restart_text.get_width()//2, screen_height//2 + 50))
        
        # Restart funktsionaalsus
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            player_x = screen_width // 2 - player_size // 2
            obstacle_x = random.randint(0, screen_width - obstacle_size)
            obstacle_y = -obstacle_size
            score = 0
            game_over = False
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
