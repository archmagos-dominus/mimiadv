#imports
import pygame
import sys
import math

#initialize pygame
pygame.init()

#create display area
#800x600px
display = pygame.display.set_mode((800, 600))

#create clock
clock = pygame.time.Clock()

#player class
class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def main(self, display):
        pygame.draw.rect(display, (255, 0, 0), (self.x, self.y, self.width, self.height))

#bullet class
class Player_bullet:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 15
        self.angle = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
    def main(self, display):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)
        pygame.draw.circle(display, (255, 255, 0), (self.x, self.y), 5)


#create player instance
player = Player(400, 300, 32, 32)
#display  scrolling
display_scroll = [0, 0]
#list for bullets
player_bullets = []

#main loop
while True:
    #fill display with a base colour
    display.fill((0, 0, 0))
    #get mouse possition
    mouse_x, mouse_y = pygame.mouse.get_pos()
    #close screen event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT
    #get keypress
    keys = pygame.key.get_pressed()
    #test
    pygame.draw.rect(display, (255, 255, 255), (100-display_scroll[0], 100-display_scroll[1], 16, 16))

    #movement
    if keys[pygame.K_a]:
        display_scroll[0] -= 5
    if keys[pygame.K_d]:
        display_scroll[0] += 5
    if keys[pygame.K_w]:
        display_scroll[1] -= 5
    if keys[pygame.K_s]:
        display_scroll[1] += 5
    #exit
    if keys[pygame.K_ESCAPE]:
        sys.exit()
        pygame.QUIT
    #firing using the mouse
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            player_bullets.append(Player_bullet(player.x, player.y, mouse_x, mouse_y))
    #call player to display
    player.main(display)
    #iterate through the bullets
    for bullet in player_bullets:
        bullet.main(display)
    #set frame rate
    clock.tick(60)
    pygame.display.update()
