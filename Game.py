import pygame
import random
import os

pygame.mixer.init()
pygame.init()



# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Screen dimensions
screen_width = 600
screen_height = 600

gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Background image
bgimg = pygame.image.load("assets\snake.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

# Game title
pygame.display.set_caption("SnakesWithMrinmoy")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def Welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,220,229))
        text_screen("Welcome to Snakes", BLACK, 115, 250)
        text_screen("Press Space to Play", BLACK, 115, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("assets\Dreamer.mp3")
                    pygame.mixer.music.play()
                    gameloop()
            
        pygame.display.update()
        clock.tick(30)


# Game loop
def gameloop():
    
    
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 20
    velocity_x = 0
    velocity_y = 0
    FPS = 30

    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)
    score = 0
    init_velocity = 5

    if (not os.path.exists("Highscore.txt")):
        with open("HighScore.txt", "w") as f:
            f.write("0")
            
    # Reads high score
    with open("HighScore.txt", "r") as f:
        highscore = f.read()
        
    def plot_snake(gameWindow, color, snk_list, snake_size):
        for x,y in snk_list:
            pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

    snk_list = []
    snk_length = 1
    
    while not exit_game:
        if game_over:
            # Writes high score
            with open("HighScore.txt", "w") as f:
                f.write(str(highscore))
                
            gameWindow.fill(WHITE)
            text_screen("Game Over!", RED, 10, 200)
            text_screen("Press Enter to Continue", RED, 10, 250)
            
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load("assets\Dreamer.mp3")
                        pygame.mixer.music.play()
                        gameloop()
        else:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                        
                    if event.key == pygame.K_q:
                        score += 5        
                        
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
                
            if abs(snake_x - food_x) < 6 and (snake_y - food_y) < 6:
                score  += 10
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snk_length += 5
                if score > int(highscore):
                    highscore = score
                
            gameWindow.fill(WHITE)
            gameWindow.blit(bgimg, (0,0))
            text_screen("Score: "+ str(score) + "  HighScore: " + str(highscore), RED, 5, 5)
            pygame.draw.rect(gameWindow, RED, [food_x, food_y, snake_size, snake_size])
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            if len(snk_list) > snk_length:
                del snk_list[0]
                
            if head in snk_list[: -1]:
                game_over = True
                pygame.mixer.music.load("assets\Explosion.mp3")
                pygame.mixer.music.play()
            
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load("assets\Explosion.mp3")
                pygame.mixer.music.play()
            
            plot_snake(gameWindow, WHITE, snk_list, snake_size)
        pygame.display.update()
        clock.tick(FPS)
        
    pygame.quit()
    quit()
    
# gameloop()
Welcome()