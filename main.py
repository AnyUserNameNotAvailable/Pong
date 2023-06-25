import pygame, sys
from settings import *
from collisions import *
import time


class Game:

    def __init__(self):
        
        #general setup
        
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Pong')
        self.clock = pygame.time.Clock()
        self.playerScore = 0
        self.opponentScore = 0
        self.playerText = game_font.render(f'{self.playerScore}', False, rgb_color)
        self.opponentText = game_font.render(f'{self.opponentScore}', False, rgb_color)

    def run(self):
        playerSpeed = 0
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        playerSpeed -= 5
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        playerSpeed += 5
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        playerSpeed += 5
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        playerSpeed -= 5

            self.playerText, self.opponentText, self.playerScore, self.opponentScore = ball_animation(self.playerText, self.opponentText, self.playerScore, self.opponentScore)
            player.y += playerSpeed
            if player.top <= 0:
                player.top = 0
            if player.bottom >= HEIGHT:
                player.bottom = HEIGHT
            opponent_ai()
            # Visuals
            self.screen.fill('black')
            pygame.draw.rect(self.screen, rgb_color, player)
            pygame.draw.rect(self.screen, rgb_color, opponent)
            pygame.draw.ellipse(self.screen, rgb_color, ball)
            pygame.draw.aaline(self.screen, rgb_color, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
            # Text Surface
            self.screen.blit(self.playerText, (540, 60))
            self.screen.blit(self.opponentText, (180, 60))

            pygame.display.update()
            self.clock.tick(FPS)
            
            

                    
if __name__ == '__main__':
    game = Game()
    game.run()
        
        