import pygame 
import sys 
from pygame.sprite import Group
from settings import Settings 
from raindrop import Raindrop 
import game_functions as gf


pygame.init()


    

    
settings = Settings()

  
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption("Raindrop")

raindrop = Raindrop(screen, settings)










    
def run_game():
    
    raindrops = Group()
    
    
    gf.create_fleet(settings, screen, raindrops)
    
    
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        
        
        
                
        gf.update_screen(screen, settings, raindrops)
    

run_game()
            
            
