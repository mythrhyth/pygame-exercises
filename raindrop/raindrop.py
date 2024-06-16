import pygame 
from settings import Settings
from pygame.sprite import Sprite

class Raindrop(Sprite):
    def __init__(self, screen, settings):
        super(Raindrop, self).__init__()
        self.screen = screen
        self.settings = settings 
        
        
        self.image = pygame.image.load("C:\\Users\\rhyth\\OneDrive\\Documents\\py[1]\\exercise_pygame\\raindrop\\raindrop.bmp")
        
        
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        
    def update(self):
        self.rect.y += self.settings.drop_speed
        
        # If the raindrop moves off the screen, reset its position to the top
        if self.rect.top > self.settings.screen_height:
            self.rect.y = 0
    
    def draw_raindrop(self):
        self.screen.blit(self.image, self.rect)
        
    
    