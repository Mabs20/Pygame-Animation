# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Rainy Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREEN = (100, 125, 75)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
DARK_BLUE = (0, 0, 100)
GRAY = (150, 150, 150)
DARK_GRAY = (75, 75, 75)
NOT_QUITE_DARK_GRAY = (100, 100, 100)
YELLOW = (200, 200, 100)
BLACK = (0, 0, 0)
BACK_BLUE = (103, 151, 229)
FRONT_BLUE = (176, 196, 232)

#Settings

def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, GRAY, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GRAY, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GRAY, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, GRAY, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, GRAY, [x + 20, y + 20, 60, 40])

def draw_small_drop(sr):
    rect = sr[:4]
    pygame.draw.ellipse(screen, BACK_BLUE, rect)

def draw_big_drop(br):
    rect = br[:4]
    pygame.draw.ellipse(screen, FRONT_BLUE, rect)
    
'''Make clouds'''
num_clouds = 100
clouds = []

for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 200)
    loc = [x, y]
    clouds.append(loc)


daytime = True
lights_on = True


''' Make rain '''
num_small_drops = 700
srain = []

num_big_drops = 50
brain = []

for i in range(num_small_drops):
    x = random.randrange(0, 1000)
    y = random.randrange(-100, 600)
    r = random.randrange(1, 5)
    stop = random.randrange(400, 700)
    sr = [x, y, r, r, stop]
    srain.append(sr)

for i in range(num_big_drops):
    x = random.randrange(0, 1000)
    y = random.randrange(-100, 600)
    r = random.randrange(10, 14)
    stop = random.randrange(600, 700)
    br = [x, y, r, r, stop]
    brain.append(br)
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                daytime = not daytime
            elif event.key == pygame.K_l:
                lights_on = not lights_on
                    # google 'pygame key constants' for more keys

                
    # Game logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 

    # Game logic
    '''move clouds'''
    for c in clouds:
        c[0] -= 1
    
        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(-50, 200)


    '''move rain'''  
    for sr in srain:
        sr[0] -= 1
        sr[1] += 4

        if sr[1] > sr[4]:
            sr[0] = random.randrange(0, 1000)
            sr[1] = random.randrange(-100, 0)

    for br in brain:
        br[0] -= 2
        br[1] += 8

        if br[1] > br[4]:
            br[0] = random.randrange(0, 1000)
            br[1] = random.randrange(-100, 0)

        ''' set sky color '''
    if daytime:
        sky = BLUE
    else:
        sky = BLACK

        ''' set window color (if there was a house)'''
    if lights_on:
        window_color = YELLOW
    else:
        window_color = WHITE
        
    # Drawing code
    ''' sky '''
    screen.fill(sky)

    ''' sun '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])


    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)

    ''' small rain ''' 
    for sr in srain:
        draw_small_drop(sr)

    '''clouds'''
    for c in clouds:
        draw_cloud(c)

    ''' big rain '''
    for br in brain:
        draw_big_drop(br)

        
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
