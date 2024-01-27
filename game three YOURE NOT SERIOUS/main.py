#import libraries
import pygame
from config import *
import sys
import math
import random

#watch this

#SPRITES DOT PEE WHY

#player class 
class Player(pygame.sprite.Sprite): #inherits from pygame sprite module
    
    def __init__(self, game, x, y):
        
        self.game = game
        self._layer = player_layer
        self.groups = self.game.all_sprites #adds player to 'all_sprites' group
        pygame.sprite.Sprite.__init__(self, self.groups) #calls inhertied constructor

        self.x = x * tilesize
        self.y = y * tilesize
        self.width = tilesize
        self.height = tilesize

        #movement
        self.x_change = 0
        self.y_change = 0
        self.facing = 'down'


        #sprite image
        image_to_load = pygame.image.load("img/cat1.png") #load sprite image
        # !! CHANGE TO SPRITESHEET FOR ANIMATIONS
        self.image = pygame.Surface([self.width, self.height]) #sets the sprite image to a rectangle
        self.image.set_colorkey(white) #removes white from sprite image
        self.image.blit(image_to_load, (0,0)) #adds image to surface

        #sprite position
        self.rect = self.image.get_rect() #set rect to same size as image
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.collide_enemies(level)

        self.rect.x += self.x_change
        self.collide_blocks("x")
        self.rect.y += self.y_change
        self.collide_blocks("y")

        self.x_change = 0
        self.y_change = 0

    #movement
    def movement(self):
        keys = pygame.key.get_pressed() #check if keys are pressed
        #move left
        if keys[pygame.K_LEFT]:
            #player movement
            self.x_change -= player_speed #move the player to the left
            self.facing = 'left'
        #move right
        if keys[pygame.K_RIGHT]:
            #player movement
            self.x_change += player_speed #move the player to the right
            self.facing = 'right'
        #move up
        if keys[pygame.K_UP]:
            #player movement
            self.y_change -= player_speed #move player up
            self.facing = 'up'
        #move down
        if keys[pygame.K_DOWN]:
            #player movement
            self.y_change += player_speed #move the player down
            self.facing = 'down'

    #movement with camera
    def camera_movement(self):
        keys = pygame.key.get_pressed() #check if keys are pressed
        #move left
        if keys[pygame.K_LEFT]:
            #all sprite movement (camera)
            for sprite in self.game.all_sprites: #move all sprites...
                sprite.rect.x += player_speed   #... to the right
            #player movement
            self.x_change -= player_speed #move the player to the left
            self.facing = 'left'
        #move right
        if keys[pygame.K_RIGHT]:
            #all sprite movement (camera)
            for sprite in self.game.all_sprites: #move all sprites...
                sprite.rect.x -= player_speed   #... to the left
            #player movement
            self.x_change += player_speed #move the player to the right
            self.facing = 'right'
        #move up
        if keys[pygame.K_UP]:
            #all sprite movement (camera)
            for sprite in self.game.all_sprites: #move all sprites...
                sprite.rect.y += player_speed   #... down
            #player movement
            self.y_change -= player_speed #move player up
            self.facing = 'up'
        #move down
        if keys[pygame.K_DOWN]:
            #all sprite movement(camera)
            for sprite in self.game.all_sprites: #move all sprites...
                sprite.rect.y -= player_speed   #... up
            #player movement
            self.y_change += player_speed #move the player down
            self.facing = 'down'



    #collisions
    #camera wall collisions
    def camera_collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += player_speed
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= player_speed

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += player_speed
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= player_speed

    #wall collisions no camera
    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom


    #enemy collisions
    #def collide_enemies(self):
    #    hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
    #    if hits:
    #        self.kill() #remove player from all_sprites group
    #        self.game.playing = False #exit game

#so. the below test DOES NOT WORK. NEW ATTEMPT: instead of one main method, have a level handler. touching enemies FOR NOW will have you exit each level.

    #enemy collisions to change level state
    def collide_enemies(self,level):
        hits = pygame.sprite.spritecollide(self, self.game.items, False)
        if hits:
            self.kill()
            g.clear_map(level)
            level += 1
            g.create_map(level)

#enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = enemy_layer
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tilesize
        self.y = y * tilesize
        self.width = tilesize
        self.height = tilesize

        self.x_change = 0
        self.y_change = 0

        #movement attributes
        self.facing = random.choice(['left', 'right'])
        self.movement_loop = 0
        self.max_travel = random.randint(7,30)

        #REPLACE WITH SPRITESHEET
        image_to_load = pygame.image.load("img/evil1.png")
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(white)
        self.image.blit(image_to_load, (0,0))
        
        #hitbox
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        #self.movement()
        
        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    #movement
    def movement(self):
        if self.facing == 'left':
            self.x_change -= enemy_speed #move enemy left each frame
            self.movement_loop -= 1 #take from movement loop
            if self.movement_loop <= -self.max_travel:
                self.facing = 'right' #change direction to right

        if self.facing == 'right':
            self.x_change += enemy_speed
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel:
                self.facing = 'left'
        

#item class
class Item(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = block_layer
        self.groups = self.game.all_sprites, self.game.items
        
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tilesize
        self.y = y * tilesize
        self.width = tilesize
        self.height = tilesize

        image_to_load = pygame.image.load("img/item.png") #load sprite image
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(white)
        self.image.blit(image_to_load, (0,0))
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def kill(self):
        self.rect_sprite.kill()
        Item.kill(self)


#ENVIRONMENT CLASSES
#wall class
class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = block_layer
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tilesize
        self.y = y * tilesize
        self.width = tilesize
        self.height = tilesize

        image_to_load = pygame.image.load("img/wall1.png") #load sprite image
        self.image = pygame.Surface([self.width, self.height])
        self.image.blit(image_to_load, (0,0))
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

#ground class
class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = block_layer
        self.groups = self.game.all_sprites, self.game.ground
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = x * tilesize
        self.y = y * tilesize
        self.width = tilesize
        self.height = tilesize


        image_to_load = pygame.image.load("img/grass1.png") #load sprite image
        self.image = pygame.Surface([self.width, self.height])
        self.image.blit(image_to_load, (0,0))
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


#BUTTONS
class Button:
    #constructor
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font('arial.ttf', fontsize) #sets font used in button
        self.content = content
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    #method for when the button is pressed
    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False


#MAIN DOT PEE WHY
#main
class Game:
    #constructor
    def __init__(self):
        pygame.init() #initialises pygame
        self.screen = pygame.display.set_mode((win_width, win_height)) #create game window
        self.clock = pygame.time.Clock() #set framerate
        self.running = True
        self.font = pygame.font.Font('arial.ttf', 32) #set font for game

        #ADD SPRITESHEETS

    #generates the level map
    def create_map(self,level):
        self.screen.fill(black)
        for i, row in enumerate(tilemaps[level]):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "E":
                    Enemy(self, j, i)
                if column == "P":
                    Player(self, j, i)
                if column == "I":
                    Item(self, j, i)

    def clear_map(self,level):
        self.screen.fill(black)
        clear = True
        while clear:
            for i, row in enumerate(tilemaps[level[row]]):
                for j, column in enumerate(row):
                    if column == "B":
                        Block(self, j, i).kill()
                    if column == "I":
                        Item(self, j, i).kill()
                    if column == "E":
                        Enemy(self, j, i).kill()
            clear = False

            #BVG REPORT
            #ENEMIES/ITEMS NOT DISAPPEARING ON NEW LEVEL WOTH BLOCKS
            #KILL ONLY REMOVES SPRITE - WE NEED RECT TO FUCKIN GO TOO

    #a new game starts - setting up
    def new(self):
        self.playing = True #defines player as playing/alive

        #sprite groups
        self.all_sprites = pygame.sprite.LayeredUpdates() #contains all sprites
        self.enemies = pygame.sprite.LayeredUpdates() #contains enemy sprites
        self.attacks = pygame.sprite.LayeredUpdates() #contains attack sprites
        self.blocks = pygame.sprite.LayeredUpdates() #contains wall sprites
        self.ground = pygame.sprite.LayeredUpdates() #contains wall sprites
        self.items = pygame.sprite.LayeredUpdates() #contains item sprites
        self.intro_background = pygame.image.load("./img/introbackground.png")

        self.create_map(level)

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

    