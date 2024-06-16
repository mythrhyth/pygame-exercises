import pygame 
import sys
import random


def check_events(catcher):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, catcher) 
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, catcher)
             
def check_keydown_events(event, catcher):
    if event.key == pygame.K_LEFT:
        catcher.moving_left = True 
        catcher.update()
    elif event.key == pygame.K_RIGHT:
        catcher.moving_right = True 
        catcher.update()
               
def check_keyup_events(event, catcher):
    if event.key == pygame.K_LEFT:
        catcher.moving_left = False 
        catcher.update()
    elif event.key == pygame.K_RIGHT:
        catcher.moving_right = False
        catcher.update()
                   
            

def update_screen(screen, settings, ball, catcher):
    
    screen.fill(settings.bg_color)
    ball.blitme(screen)
    catcher.blitme(screen)
    pygame.display.flip()
    
def update_balls(catcher, ball, settings):
    
    collisions = ball.rect.colliderect(catcher.rect)
    
    if collisions:
        ball.rect.y = 0 
        settings.points += 1
        ball.rect.x = random.randint(0, 1200 - ball.rect.width)
        
    elif ball.rect.y > ball.screen_rect.height:
        ball.rect.y = 0
        settings.fallen_balls += 1
        if settings.fallen_balls >= 3:
            print("Game Over")
            pygame.quit()
            sys.exit()
    else:
        ball.update()
        
        
