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

screen = pygame.display.set_mode([ScreenWidth, ScreenHeight])

