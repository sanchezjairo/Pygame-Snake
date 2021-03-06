import pygame
import random

pygame.init()
pygame.display.set_caption("Welcome to the game with a little twist!")


ScreenWidth = 650
ScreenHeight = 650

CharacterWidth = 35
CharacterHeight = 35

FoodWidth = 20
FoodHeight = 20

LimeGreen = (50,205,50)
Black = (0,0,0)
ShamrockGreen = (0,158,96)
Red = (255,0,0)
Darkgrey = (169,169,169)

player_x = 325
player_y = 325

food_x = 300
food_y = 30

enemy_x = 300
enemy_y = 10

enemy2_x = 200
enemy2_y = 10

speed = 6
points = 0
timer = 0
time = 0

screen = pygame.display.set_mode([ScreenWidth, ScreenHeight])

def is_touched(x1, y1, x2, y2, width, height):
    if(x1 >= x2 + width) or (x2 >= x1 + width):
         return False

    if (y1 >= y2 + height) or (y2 >= y1 + height):
         return False
    return True

def design(text, color, font_size, x, y):
    font = pygame.font.SysFont(None, font_size)
    img = font.render(text, True, color)
    screen.blit(img, (x,y))

running = True
while running:

    pygame.time.delay(20)

    time += 1

    if time >= 60:
        time= 0 
        timer += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.event

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed
    if keys[pygame.K_DOWN]:
        player_y += speed
    if keys[pygame.K_UP]:
        player_y -= speed
       
    enemy_y += speed
    enemy2_y += speed

    if enemy_y > ScreenHeight:
        enemy_y = 0
        enemy_x = random.random() * (ScreenWidth-CharacterWidth)

    if enemy2_y >ScreenHeight:
        enemy2_y = 0
        enemy2_x = random.random() * (ScreenWidth- CharacterWidth)

    if is_touched(player_x, player_y, enemy_x, enemy_y, CharacterWidth, CharacterHeight,):
        points = 0
        player_x = 325
        player_y = 325
        timer = 0
    if is_touched(player_x,player_y,food_x,food_y, CharacterHeight,CharacterWidth):
        points += 1
        food_y = 200
        food_x = random.random() * (ScreenWidth-CharacterWidth)
    if is_touched(player_x, player_y, enemy2_x, enemy2_y, CharacterWidth, CharacterHeight):
        points = 0
        player_x = 325
        player_y = 325
        timer = 0

    screen.fill(ShamrockGreen)

    pygame.draw.rect(screen, LimeGreen, (player_x, player_y, CharacterHeight, CharacterWidth))
    pygame.draw.rect(screen, Red, (enemy_x, enemy_y, CharacterHeight, CharacterWidth))
    pygame.draw.rect(screen, Darkgrey, (food_x, food_y, CharacterHeight, CharacterWidth))
    pygame.draw.rect(screen, Red, (enemy2_x, enemy2_y, CharacterHeight, CharacterWidth))

    design(text=f'Points: {points}', color=Black, font_size=24, x=20, y=20)
    design(text=f'Timer: {timer}', color=Black, font_size=24, x=550, y=20)
    
    pygame.display.update()

 


