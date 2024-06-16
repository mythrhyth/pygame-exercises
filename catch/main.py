import pygame 
import sys 
from settings import Settings
import game_functions as gf 
from  ball import Ball
from catcher import Catcher
from pygame.sprite import Group


pygame.init()

def run_game():
    
    
    settings = Settings()
    
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Catch")
    
    ball = Ball(screen, settings)
    catcher = Catcher(screen, settings)
    
    balls = Group()
    
    
    while True:
        ball.update()
        gf.check_events(catcher)
        
        gf.update_balls(catcher, ball, settings)
        
                
        gf.update_screen(screen, settings, ball, catcher)
        
run_game()             
                
                