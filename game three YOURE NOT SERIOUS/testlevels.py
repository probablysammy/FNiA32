#import libraries
import pygame
from sprites import *
from config import *
import sys


#main
class Game:
    #constructor
    def __init__(self):
        pygame.init() #initialises pygame
        self.screen = pygame.display.set_mode((win_width, win_height)) #create game window
        self.clock = pygame.time.Clock() #set framerate
        self.running = True
        self.font = pygame.font.Font('arial.ttf', 32) #set font for game
        self.level = 0 #set level to the first level (hub world)

        #ADD SPRITESHEETS

    #generates the level map
    def create_map(self):
        for i, row in enumerate(tilemaps[self.level]):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "E":
                    Enemy(self, j, i)
                if column == "P":
                    Player(self, j, i)

    #a new game starts
    def new(self):
        self.playing = True #defines player as playing/alive

        #sprite groups
        self.all_sprites = pygame.sprite.LayeredUpdates() #contains all sprites
        self.enemies = pygame.sprite.LayeredUpdates() #contains enemy sprites
        self.attacks = pygame.sprite.LayeredUpdates() #contains attack sprites
        self.blocks = pygame.sprite.LayeredUpdates() #contains wall sprites
        self.ground = pygame.sprite.LayeredUpdates() #contains wall sprites
        self.intro_background = pygame.image.load("./img/introbackground.png")

        self.create_map()

    #game loop events
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if user exits window
                self.playing = False
                self.running = False

    #game loop updates
    def update(self):
        self.all_sprites.update() #update sprites in 'all_sprites' group

    #game loop updates
    def draw(self):
        self.screen.fill(black) #fill background with black
        self.all_sprites.draw(self.screen) #draws rect and image for all sprites
        self.clock.tick(fps)
        pygame.display.update()
        

    #game loop
    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def intro_screen(self):
        intro = True

        title = self.font.render('programming project', True, black)
        title_rect = title.get_rect(x=170, y=170)
        play_button = Button(270,230, 100, 50, white, black, 'Play', 32)
        
        while intro:
            #title event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False

            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(fps)
            pygame.display.update()

    def end_screen(self):
        pass

#instantiate game object
g = Game()
g.new()
g.intro_screen()
while g.running:
    g.main()
    g.end_screen()

pygame.quit()
sys.exit()

    
