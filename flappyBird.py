import pygame
import sys
import random

pygame.init()
def game_floor():
    screen.blit(floor , (floor_Xpos,680)) 
    screen.blit(floor , (floor_Xpos+576,680)) 

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            hit_sound.play()
            return False
    if bird_rect.top <= -100 or bird_rect.bottom >= 680:
        hit_sound.play()
        return False
    return True
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (700,random_pipe_pos-200))
    return bottom_pipe , top_pipe
    # return random pipe co-ordinates
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 768:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe , pipe)

gravity = 0.25
birdMove = 0
clock = pygame.time.Clock()
game_active = True
 

screen = pygame.display.set_mode((576,768)) 

background = pygame.image.load("assets/images/background-day.png").convert()
background = pygame.transform.scale2x(background)

bird = pygame.image.load("assets/images/bluebird-midflap.png").convert_alpha()
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center=(100,384))

floor = pygame.image.load("assets/images/base.png")
floor = pygame.transform.scale2x(floor)
floor_Xpos = 0

mesasge = pygame.image.load("assets/images/message.png")
mesasge = pygame.transform.scale2x(mesasge)
gameOver_rect = mesasge.get_rect(center = (288,384))

pipe_surface = pygame.image.load("assets/images/pipe-green.png")
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipeList = []
pipe_height = [200 , 400 ,500] 

flap_sound = pygame.mixer.Sound("assets/audio/wing.wav")
hit_sound = pygame.mixer.Sound("assets/audio/hit.wav")

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE , 1200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE and game_active:
                birdMove = 0
                birdMove -=8
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False :
                bird_rect.center = (100 , 384)
                birdMove = 0
                pipeList.clear()
                game_active = True
        if event.type == SPAWNPIPE and game_active:
            pipeList.extend(create_pipe())
                 
    screen.blit(background , (0,0))
    
    if game_active:
      birdMove+=gravity
      bird_rect.centery += birdMove
      screen.blit(bird , bird_rect) 
      game_active = check_collision(pipeList)

      pipeList = move_pipes(pipeList)
      draw_pipes(pipeList)
    else:
      screen.blit(mesasge , gameOver_rect)

    game_floor()
    floor_Xpos -=1
    if floor_Xpos == -576:
        floor_Xpos = 0

    
    pygame.display.update()
    clock.tick(120)