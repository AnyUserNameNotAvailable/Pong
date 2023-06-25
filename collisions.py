import random
from settings import *
import time

ballSpeed_X = 5 * random.choice((1,-1))
ballSpeed_Y = 5 * random.choice((1,-1))
playerSpeed = 0

opponentSpeed = 5

def ball_animation(playerText, opponentText, playerScore, opponentScore): 
    global ballSpeed_X,ballSpeed_Y
    ball.x += ballSpeed_X
    ball.y += ballSpeed_Y
    
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ballSpeed_Y *= -1
    if ball.left <= 0:  
        playerScore += 1
        ballRestart()
        playerText = game_font.render(f'{playerScore}', False, rgb_color)  # Update playerText
    if ball.right >= WIDTH:
        opponentScore += 1
        ballRestart()
        opponentText = game_font.render(f'{opponentScore}', False, rgb_color)
        
    if ball.colliderect(player) or ball.colliderect(opponent):
        ballSpeed_X *= -1
    return playerText, opponentText, playerScore, opponentScore
def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponentSpeed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponentSpeed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= HEIGHT:
        opponent.bottom = HEIGHT
        
def ballRestart():
    global ballSpeed_X,ballSpeed_Y 
    ball.center = (WIDTH/2, HEIGHT/2)
    ballSpeed_Y *= random.choice((1,-1))
    ballSpeed_X *= random.choice((1,-1))
    
    
    
def gamePause():
    pass
