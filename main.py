import pygame

# Initializes pygame
pygame.init()

# Game clock for framerate
clock = pygame.time.Clock()

# Creates game screen
screen = pygame.display.set_mode((800, 600))

player = pygame.image.load("meow.png")
playerX = 200
playerY = 250
playerX_change = 0
playerY_change = 0

# Draws player icon onto screen
def draw_player(x, y):
    screen.blit(player, (x,y))

running = True
while running:
    # Fills screen with color (RGB)
    screen.fill((126, 189, 64))

    for event in pygame.event.get():
        # exits the game
        if event.type == pygame.QUIT:
            running = False

        # Keyboard controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -5
            if event.key == pygame.K_DOWN:
                playerY_change = 5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_LEFT:
                playerX_change = -5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0

    # Changes player position 
    playerX += playerX_change
    playerY += playerY_change

    # Game bounds 
    if playerX <= 0:
        playerX = 0
    elif playerX >= 768:
        playerX = 768

    if playerY <= 0:
        playerY = 0
    elif playerY >= 568:
        playerY = 568

    draw_player(playerX, playerY)
    pygame.display.update()
    # Framerate 60 fps
    clock.tick(60)
        
              