import pygame
import random 




class Ball():
    def __init__(self, screen, settings):
        self.settings = settings
        self.image = pygame.image.load("C:\\Users\\rhyth\\OneDrive\\Documents\\py[1]\\exercise_pygame\\catch\\ball.bmp")
        self.screen = screen
        
        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect()
        
        self.rect.x = random.randint(0, 1200 - self.rect.width)
        self.rect.y = 0
        
    def update(self):
        self.rect.y += self.settings.ball_speed
        
        if self.rect.y > self.screen_rect.height:
            self.rect.y = 0
    
    def blitme(self, screen):
        screen.blit(self.image, self.rect)