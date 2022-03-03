#main imports
import pygame
import sys
#imports from local config files
from sprites import *
from config import *

#main game class
class Game:
    def __init__(self):
        #initialize pygame
        pygame.init()
        #create game window
        self.stream = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        #create Clock
        self.clock = pygame.time.Clock()
        #set main font
        self.font = pygame.font.Font('Arial', 32)
        #boolean var to control exititng the gmae
        self.running = True
    def new(self):
        #a game starts
        self.playing = True
        #sprites updating
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        #player object
        self.player = Player()
