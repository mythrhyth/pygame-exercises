import pygame
from raindrop import Raindrop

def update_screen(screen, settings, raindrops):
    screen.fill(settings.background_color)
    raindrops.update()
    raindrops.draw(screen)
    pygame.display.flip()
    
def get_number_raindrops(settings, raindrop_width):
    available_space_x = settings.screen_width - (2* raindrop_width)
    number_of_raindrops_x = int(available_space_x / (2* raindrop_width))
    return number_of_raindrops_x

def get_number_rows(settings, raindrop_height):
    available_space_y = settings.screen_height - 2 * raindrop_height
    number_rows = int(available_space_y / (2* raindrop_height))
    return number_rows

def create_raindrops(settings, screen,raindrops, raindrop_width, raindrop_height, number, num):
    raindrop = Raindrop(screen, settings)
    
    raindrop.x = raindrop_width +2 * raindrop_width * number
    raindrop.y = raindrop_height + 2* raindrop_height* num
    
    raindrop.rect.y = raindrop.y
    raindrop.rect.x = raindrop.x
    raindrops.add(raindrop)


def create_fleet(settings, screen, raindrops):
    raindrop = Raindrop(screen, settings)
    raindrop_width = raindrop.rect.width
    raindrop_height = raindrop.rect.height
    
    number_of_raindrops_x = get_number_raindrops(settings, raindrop_width)
    number_rows = get_number_rows(settings, raindrop_height)
    
    
    
    for num in range(number_rows):
        
        for number in range(number_of_raindrops_x):
            create_raindrops(settings, screen, raindrops, raindrop_width, raindrop_height, number, num)
            
        
     
    