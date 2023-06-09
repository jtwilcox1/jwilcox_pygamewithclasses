# File created by: JT Wilcox
# Agenda:
# gIT GITHUB    
# Build file and folder structures
# Create libraries
# testing github changes
# I changed something - I changed something else tooooo!

# This file was created by: JT Wilcox
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# Sources: 

# import libs
import pygame as pg
import random
import os
# import settings 
from settings import *
from sprites import *
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# create game class in order to pass properties to the sprites file

class Game: 
    def __init__(self): 
        # init game window etc. 
        pg.init()
        # gives us access to the sound mixer
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
    def new (self): 
        # starting a new game or restarting game 
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for i in range(0,10): 
            m = Mob(20,20(0,255,0))
            self.all_sprites.add(m)
            self.enemies.add(m)
        self.run()
        # starts running the game
    def run(self):
        self.playing = True 
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def event(self): 
        for event in pg.event.get():
            # game stops running
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    
    def update(self): 
        self.all_sprites.update()
    def draw(self): 
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
# is this a method or a function? method because it is inside of the class
        pg.display.flip()
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

g = Game()

while g.running:
    g.new()




pg.quit()
