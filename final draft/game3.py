
import pygame, sys
from Classes import player1Sprite, player2Sprite, ball, collision, Net, kick, goal, bar, barHit
from easypg.colours import AQUA, GREEN, NAVY, PURPLE, RED, WHITE, BLUE
from easypg.fonts import FONTS

pygame.init()

# D: Display configuration

size = (1000, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Robo Football")

# E: Entity creation
# background image

background = pygame.Surface(size).convert()
background.fill(BLUE)
grass=pygame.draw.rect(background, (GREEN), ((0, 300), (1000, 400)), 0)
rightNet = Net(900,150, "R")
leftNet = Net(0, 150, "L")
rightBar = bar(950, 160)
leftBar = bar(50, 160)
player1 = player1Sprite("Player1", 900, 50)
player2 = player2Sprite("Player2", 100, 50)
football = ball(500, 290)



# Create a group of multiple sprites

playerGroup = pygame.sprite.Group(player1, player2 )
ballGroup = pygame.sprite.Group(football)                        
everything = pygame.sprite.Group(player1, player2, rightNet, leftNet, football, rightBar, leftBar)

#collison action



# Define variables to control the action

clock = pygame.time.Clock()
running = True

    
# A: Action, broken down as ALTER steps...

# A: Assign values to key variables
clock = pygame.time.Clock()
running = True
vx = 5
vy = 5

# L: Loop
while running:
    # T: Timing, to control frame rate
    clock.tick(30)

    # E: Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # R: Refresh display
    screen.blit(background, (0, 0))
    playerGroup.clear(screen, background)
    everything.clear(screen, background)
    everything.update()
    everything.draw(screen)

    # collissions:
##    if collision(football, playerGroup) == True:
##        print("yay")
    kick(player1,football, ballGroup)
    kick(player2, football, ballGroup)
    goal(football, screen)
    barHit(leftBar, football, ballGroup)
    barHit(rightBar, football, ballGroup)
  
    pygame.display.flip()
