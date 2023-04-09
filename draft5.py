import pygame
import random

# initialize Pygame
pygame.init()

# set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch the Apples!")

# load the background image
background_image = pygame.image.load("background.png").convert()

# set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up the font
FONT = pygame.font.SysFont(None, 48)

# set up the basket
basket_image = pygame.image.load("basket.png").convert_alpha()
basket_rect = basket_image.get_rect()
basket_rect.centerx = WINDOW_WIDTH // 2
basket_rect.bottom = WINDOW_HEIGHT - 10
basket_speed = 0  # initialize the basket speed

# set up the apples
apple_image = pygame.image.load("apple.png").convert_alpha()
apple_rects = []
apple_speed = 3
apples_caught = 0
apples_needed = 10

# set up the game loop
clock = pygame.time.Clock()
running = True

while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                basket_speed = -10  # set the speed to a negative value to move left
            elif event.key == pygame.K_RIGHT:
                basket_speed = 10  # set the speed to a positive value to move right
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                basket_speed = 0  # stop moving the basket

    # update the basket position based on the speed
    basket_rect.move_ip(basket_speed, 0)

    # keep the basket inside the screen
    if basket_rect.left < 0:
        basket_rect.left = 0
    elif basket_rect.right > WINDOW_WIDTH:
        basket_rect.right = WINDOW_WIDTH

    # update the game state
    for apple_rect in apple_rects:
        apple_rect.move_ip(0, apple_speed)
        if apple_rect.colliderect(basket_rect):
            apples_caught += 1
            apple_rects.remove(apple_rect)
        elif apple_rect.bottom > WINDOW_HEIGHT:
            apple_rects.remove(apple_rect)
        if apples_caught == apples_needed:
            game_over = FONT.render("You Win!", True, GREEN)
            game_over_rect = game_over.get_rect()
            game_over_rect.centerx = WINDOW_WIDTH // 2
            game_over_rect.centery = WINDOW_HEIGHT // 2
            running = False

    # spawn new apples
    if random.random() < 0.02:
        apple_rects.append(apple_image.get_rect(top=0, left=random.randint(0, WINDOW_WIDTH - apple_image.get_width())))

    # draw the game
    window.blit(background_image, (0, 0))
    window.blit(basket_image, basket_rect)
    for apple_rect in apple_rects:
        window.blit(apple_image, apple_rect)
    if apples_caught < apples_needed:
        apples_text = FONT.render(f"Apples Caught: {apples_caught}/{apples_needed}", True, BLACK)
        apples_text_rect = apples_text.get_rect()
        apples_text_rect.topleft = (10, 10)
        window.blit(apples_text, apples_text_rect)
    else:
        game_over = FONT.render("You Win!", True, GREEN)
        game_over_rect = game_over.get_rect()
        game_over_rect.centerx = WINDOW_WIDTH // 2
        game_over_rect.centery = WINDOW_HEIGHT // 2
        window.blit(game_over, game_over_rect)

    pygame.display.update()

    # set the frame rate
    clock.tick(60)

# quit Pygame
pygame.quit()

