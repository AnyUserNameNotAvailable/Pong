import pygame

pygame.init()

WIDTH = 720
HEIGHT = 480
FPS = 60

ball = pygame.Rect(WIDTH/2 - 10, HEIGHT/2 - 10, 20,20)
player = pygame.Rect(WIDTH - 20, HEIGHT/2 - 35 , 5, 70)
opponent = pygame.Rect(15, HEIGHT/2 - 35, 5, 70)
rgb_color = (200,200,200)


# text variables
game_font = pygame.font.Font('Peepo.ttf', 32)
