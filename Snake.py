import pygame
import random

pygame.init()
pygame.display.set_caption("Welcome to the game with a little twist!")


ScreenWidth = 650
ScreenHeight = 650

CharacterWidth = 35
CharacterHeight = 35

LimeGreen = (50,205,50)
Black = (0,0,0)
ShamrockGreen = (0,158,96)
Red = (255,0,0)


player_x = 65
player_y = 65

food_x = 300
food_y = 30

enemy_x = 300
enemy_y = 10

speed = 6
points = 0
timer = 0

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

    screen.fill(ShamrockGreen)

    pygame.draw.rect(screen, LimeGreen, (player_x, player_y, CharacterHeight, CharacterWidth))
    

    design(text=f'Points: {points}', color=Black, font_size=24, x=20, y=20)
    design(text=f'Timer: {timer}', color=Black, font_size=24, x=575, y=20)
    
    pygame.display.update()

 


