import pygame 
import sys

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
    
def update_balls(catcher, balls, ball):
    collisions = pygame.sprite.groupcollide(balls, catcher, True, False)
    
    if collisions or balls.rect.y > balls.screen_rect.height:
        balls.empty()
        balls.add(ball)
     
   
        
    