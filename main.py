import pygame

# Initializes pygame
pygame.init()

# Initalizes the joystick module
pygame.joystick.init()

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

        # detects if a controller is pluged in
        if event.type == pygame.JOYDEVICEADDED:
            print("Controller connected: " + str(event))
            joy = pygame.joystick.Joystick(event.device_index)
            # buttons = joy.get_numbuttons()
            # print(screen, f"Number of buttons: {buttons}")

            # for i in range(buttons):
            #     button = joy.get_button(i)
            #     print(screen, f"Button {i:>2} value: {button}")
            # print(str(joy.get_name()))
        
        # movement with controller buttons
        if event.type == pygame.JOYBUTTONDOWN:
            print(event)
            # X button
            if event.button == 0:
                playerY_change = -5
            # A button
            if event.button == 1:
                playerX_change = 5
            # B button
            if event.button == 2:
                playerY_change = 5
            # Y button
            if event.button == 3:
                playerX_change = -5
            # select button
            if event.button == 8:
                running = False

        # Stops continuous movement when button is lifted (Controller)
        if event.type == pygame.JOYBUTTONUP:
            if event.button == 0 or event.button == 2:
                playerY_change = 0
            if event.button == 1 or event.button == 3:
                playerX_change = 0


        # D-pad Controls (Goofy setup)
        if event.type == pygame.JOYAXISMOTION:
            print(event)
            if event.axis == 1 and event.value == 1:
                playerX_change = 5
            if event.axis == 1 and event.value <= -1:
                playerX_change = -5
            if event.axis == 4 and event.value == 1:
                playerY_change = 5
            if event.axis == 4 and event.value <= -1:
                playerY_change = -5

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

        # Stops continuous movement when button is lifted (Keyboard)
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
        
              