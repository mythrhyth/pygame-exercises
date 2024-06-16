import pygame 


class Catcher():
    def __init__(self, screen, settings):
        
        self.image = pygame.image.load("C:\\Users\\rhyth\\OneDrive\\Documents\\py[1]\\exercise_pygame\\catch\\catcher.bmp")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.settings = settings 
        self.screen_rect = self.screen.get_rect()
        
        self.rect.x = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.height
        
        self.moving_right = False
        self.moving_left = False 
        
    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.catcher_speed
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.catcher_speed

        
    def blitme(self, screen):
        screen.blit(self.image, self.rect)
        
     