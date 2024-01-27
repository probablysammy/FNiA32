#import libraries
import pygame
import sys
import math
import random

from config import *

#SAVE SYSTEM
try:
  open("savefile.csv","r")
except:
  save = open("savefile.csv","a")
  save.write("savename,c_type,c_colour,level,equip,inv1,inv2\n")
  save.close()

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#SPRITE CLASSES

#player 
class Player(pygame.sprite.Sprite):
    
    def __init__(self, game, x, y):

        self.game = game
        self._layer = player_layer
        self.groups = self.game.all_sprites, self.game.player #adds player to 'all_sprites' group
        pygame.sprite.Sprite.__init__(self, self.groups)

        #image coordinates
        self.x = x * tilesize
        self.y = y * tilesize

        #image size
        self.width = tilesize
        self.height = tilesize

        print(g.c_type)
        print(g.c_colour)
        
        #sprite image
        if g.c_type == "dog":
            if g.c_colour == "1":
                image_to_load = pygame.image.load("img/dog1_sprite.png")
            else:
                image_to_load = pygame.image.load("img/dog2_sprite.png")
        elif g.c_type == "cat":
            if g.c_colour == "1":
                image_to_load = pygame.image.load("img/cat1_sprite.png")
            else:
                image_to_load = pygame.image.load("img/cat2_sprite.png")

        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(keygrey)
        self.image.blit(image_to_load, (0,0))

        #movement
        self.x_change = 0
        self.y_change = 0
        self.facing = 'down'

        #hitbox position
        self.rect = self.image.get_rect() #set rect to same size as image
        self.rect.x = self.x
        self.rect.y = self.y

    #update
    def update(self):
        #get amounts to move
        self.movement()

        #collisions
        self.collide_enemies()
        self.collide_doors()
        self.esc_pressed()

        #update player position
        self.rect.x += self.x_change #update x position
        self.collide_blocks("x") #check x block collisions
        self.rect.y += self.y_change #update y position
        self.collide_blocks("y") #check y block collisions

        #reset position change
        self.x_change = 0
        self.y_change = 0

    #movement
    def movement(self):
        
        keys = pygame.key.get_pressed() #check if keys are pressed
        
        #move left
        if keys[pygame.K_LEFT]:
            self.x_change -= player_speed #move the player to the left
        
        #move right
        if keys[pygame.K_RIGHT]:
            self.x_change += player_speed #move the player to the right
        
        #move up
        if keys[pygame.K_UP]:
            self.y_change -= player_speed #move player up
        
        #move down
        if keys[pygame.K_DOWN]:
            self.y_change += player_speed #move the player down

#COLLISION CLASSES
    #wall collisions
    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False) #get boolean value

            if hits:

                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width #prevent the player from moving past the block

                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right #prevent the player from moving past the block

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False) #get boolean value

            if hits:

                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height #prevent the player from moving past the block

                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom #prevent the player from moving past the block

    #enemy collisions
    def collide_enemies(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            g.create_map(levelmap[g.level])

    #door collisions
    def collide_doors(self):
        hits = pygame.sprite.spritecollide(self, self.game.doors, False)
        if hits:
            if g.equip == itemlist[g.level]:
                self.kill() #remove player from all_sprites group
                g.playing = False


    def esc_pressed(self):
        if g.inv_open ==  False: #check if the menu is already open
            for event in pygame.event.get(): #check events
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    Inventorymenu(g)

#enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = enemy_layer
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        #image coordinates
        self.x = x * tilesize
        self.y = y * tilesize

        #image size
        self.width = tilesize
        self.height = tilesize

        #sprite image
        image_to_load = pygame.image.load("img/enemy.png")
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(white)
        self.image.blit(image_to_load, (0,0))

        #movement
        self.x_change = 0
        self.y_change = 0
        self.facing = random.choice(['left', 'right'])
        self.movement_loop = 0
        self.max_travel = 40
        
        #hitbox position
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

#MOVEMENT CLASSES
    #update
    def update(self):
        self.movement()
        
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

#friend class
class Friend(pygame.sprite.Sprite):
    def __init__(self, game, x, y, friend_num):

        self.game = game
        self._layer = friend_layer
        self.groups = self.game.all_sprites, self.game.friends
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.friend_num = friend_num

        #image coordinates
        self.x = x * tilesize
        self.y = y * tilesize

        #image size
        self.width = tilesize
        self.height = tilesize

        #sprite image
        image_to_load = pygame.image.load("img/friend.png")
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(white)
        self.image.blit(image_to_load, (0,0))
        
        #hitbox position
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.interact()

    def interact(self):
        #collision detection
        hits = pygame.sprite.spritecollide(self, self.game.player, False)
        if hits:
            #input detection
            for event in pygame.event.get(): #check events
                if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                    Dialogue(g, friend_dialogue[self.friend_num])

#item class
class Item(pygame.sprite.Sprite):
    def __init__(self, game, x, y,item_num):

        self.game = game
        self._layer = item_layer
        self.groups = self.game.all_sprites, self.game.items
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.item_num = item_num

        #image coordinates
        self.x = x * tilesize
        self.y = y * tilesize

        #image size
        self.width = tilesize
        self.height = tilesize

        #sprite image
        image_to_load = pygame.image.load("img/item.png")
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(white)
        self.image.blit(image_to_load, (0,0))
        
        #hitbox position
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.interact()

    def interact(self):

        def item_to_write(item_num):
            if item_num == 0:
                return("item")
            elif item_num == 1:
                return("flashlight")
            elif item_num == 2:
                return("key")
            elif item_num == 3:
                return("cake")
        

        #collision detection
        hits = pygame.sprite.spritecollide(self, self.game.player, False)
        if hits:
            #input detection
            for event in pygame.event.get(): #check events
                if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                    Dialogue(g, item_dialogue[self.item_num])
                    if g.inv1 == "0":
                        g.inv1 = item_to_write(self.item_num)
                    else:
                        g.inv2 = item_to_write(self.item_num)
                    self.kill()
#ground class
class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = ground_layer
        self.groups = self.game.all_sprites, self.game.ground
        pygame.sprite.Sprite.__init__(self,self.groups)

        #image coordinates
        self.x = x * tilesize
        self.y = y * tilesize

        #image size
        self.width = tilesize
        self.height = tilesize

        #sprite image
        image_to_load = pygame.image.load("img/grass.png")
        self.image = pygame.Surface([self.width, self.height])
        self.image.blit(image_to_load, (0,0))
        
        #hitbox position
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

#block class
class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = block_layer
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self,self.groups)

        #image coordinates
        self.x = x * tilesize
        self.y = y * tilesize

        #image size
        self.width = tilesize
        self.height = tilesize

        #sprite image
        image_to_load = pygame.image.load("img/wall.png")
        self.image = pygame.Surface([self.width, self.height])
        self.image.blit(image_to_load, (0,0))
        
        #hitbox position
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y 

#door class
class Door(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = item_layer
        self.groups = self.game.all_sprites, self.game.doors
        pygame.sprite.Sprite.__init__(self,self.groups)

        #image coordinates
        self.x = x * tilesize
        self.y = y * tilesize

        #image size
        self.width = tilesize
        self.height = tilesize

        #sprite image
        image_to_load = pygame.image.load("img/door.png")
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(white)
        self.image.blit(image_to_load, (0,0))
        
        #hitbox position
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y       

#dialogue class
class Dialogue(pygame.sprite.Sprite):
    #constructor
    def __init__(self, game, dialogue):
        self.box = 0
        self.dialogue = dialogue

        self.game = game
        self._layer = dialogue_layer
        self.groups = self.game.all_sprites, self.game.dialogue
        pygame.sprite.Sprite.__init__(self,self.groups)

        #set size and position
        self.x = 20
        self.y = 20
        self.width = 600
        self.height = 100

        #set image
        self.image = pygame.Surface((self.width, self.height)) #create dialogue box surface
        self.image.fill(brown) #set box colour to brown
        self.rect = self.image.get_rect() #set dialogue hitbox to image size
        #set dialogue position
        self.rect.x = self.x
        self.rect.y = self.y

        self.image.blit(self.image, self.rect)
        
        #text
        self.font = pygame.font.Font('arial.ttf', 32) #sets font and size used in dialogue
        
        #line 1
        self.line1 = dialogue[self.box][0]
        self.line1_text = self.font.render(self.line1, True, black) #render line1 as text
        self.line1_rect = 10, 5 #set text position
        self.image.blit(self.line1_text, self.line1_rect)
            
        #line 2
        self.line2 = dialogue[self.box][1]
        self.line2_text = self.font.render(self.line2, True, black) #render line2 as text
        self.line2_rect = 10, 50 #set text position
        self.image.blit(self.line2_text, self.line2_rect)

    #update method
    def update(self):
        self.x_pressed()

    #changing dialogue displayed when x is pressed
    def x_pressed(self):
        for event in pygame.event.get(): #check events
            if event.type == pygame.KEYDOWN and event.key == pygame.K_x:

                self.box = self.box + 1   #change to next dialogue box
                if self.box > len(self.dialogue) - 1:
                    self.box = 0
                    self.kill()
                
                self.image.fill(brown) #fill box with brown (to cover up prev text)
                self.image.blit(self.image, self.rect) #show box on screen
                
                #line 1
                self.line1 = self.dialogue[self.box][0]
                self.line1_text = self.font.render(self.line1, True, black) #render line1 as text
                self.image.blit(self.line1_text, self.line1_rect)
                    
                #line 2
                self.line2 = self.dialogue[self.box][1]
                self.line2_text = self.font.render(self.line2, True, black) #render line2 as text
                self.image.blit(self.line2_text, self.line2_rect)
        
#save point class
class Savepoint(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = item_layer
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)

        #image coordinates
        self.x = x * tilesize
        self.y = y * tilesize

        #image size
        self.width = tilesize
        self.height = tilesize

        #sprite image
        image_to_load = pygame.image.load("img/save.png")
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(white)
        self.image.blit(image_to_load, (0,0))
        
        #hitbox position
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x_pressed()

    def x_pressed(self):
        #collision detection
        hits = pygame.sprite.spritecollide(self, self.game.player, False)
        if hits:
            #input detection
            for event in pygame.event.get(): #check events
                if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                    #writing to save file
                    save = open("savefile.csv","a")
                    save.seek(5)
                    to_write = str(g.savename), ",", str(g.c_type), ",", str(g.c_colour), ",", str(g.level), ",", g.equip, ",", g.inv1, ",", g.inv2, "\n"
                    for x in to_write:
                        save.write(x)
                    save.close()

class HubDoor(pygame.sprite.Sprite):
    def __init__(self, game, x, y, door_num):

        self.door_num = door_num
        self.game = game
        self._layer = item_layer
        self.groups = self.game.all_sprites, self.game.hubdoors
        pygame.sprite.Sprite.__init__(self,self.groups)

        #image coordinates
        self.x = x * tilesize
        self.y = y * tilesize

        #image size
        self.width = tilesize
        self.height = tilesize

        #sprite image
        image_to_load = pygame.image.load("img/door.png")
        self.image = pygame.Surface([self.width, self.height])
        self.image.set_colorkey(white)
        self.image.blit(image_to_load, (0,0))
        
        #hitbox position
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y 

    def update(self):
        self.collide()

    def collide(self):
        #collision detection
        hits = pygame.sprite.spritecollide(self, self.game.player, False)
        if hits:
            #input detection
            if self.door_num == g.level:
                g.playing = False



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#MENU CLASSES

class Thumbnail(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img_source):

        self.game = game
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)

        #image coordinates
        self.x = x
        self.y = y 

        #image size
        self.width = 95
        self.height = 95

        #sprite image
        image_to_load = pygame.image.load(img_source)
        self.image = pygame.Surface([self.width, self.height])
        self.image.blit(image_to_load, (0,0))
        
        #hitbox position
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y 

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False

class Box(pygame.sprite.Sprite):
    #constructor
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):

        self.font = pygame.font.Font('arial.ttf', fontsize) #sets font used in box
        self.content = content
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg = fg #text colour
        self.bg = bg #box colour

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False

class Inventorymenu(pygame.sprite.Sprite):

    def __init__(self, game):

        g.inv_open = True

        self.game = game
        self._layer = dialogue_layer
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)

        #sprite image
        #set size
        self.width = 640
        self.height = 480

        #set image
        self.image = pygame.Surface((self.width, self.height)) #create menu surface
        self.image.fill(white) #set colour to white
        self.rect = self.image.get_rect() 

        self.image.blit(self.image, self.rect)
            
        #text
        self.font = pygame.font.Font('arial.ttf', 32) #sets font and size used in dialogue

        menu_title = Box(10,10,620,80,white,black,"INVENTORY MENU",36)
        left_box = Box(15,100,200,250,white,black,"",0)
        inv1_box = Box(230,100,400,150,white,black,"INV1",36)
        inv2_box = Box(230,265,400,150,white,black,"INV2",36)

        self.image.blit(menu_title.image,menu_title.rect)
        self.image.blit(left_box.image,left_box.rect)
        self.image.blit(inv1_box.image,inv1_box.rect)
        self.image.blit(inv2_box.image,inv2_box.rect)

        #left box
        self.exit_box = Box(20,265,190,80,black,grey,"EXIT GAME",20)
        equip_box = Box (20,105,190,30,black,grey,"ITEM EQUIPPED",20)

        self.image.blit(self.exit_box.image,self.exit_box.rect)
        self.image.blit(equip_box.image,equip_box.rect)


        #inventory slots

        #generate description based on item
        def gen_desc(name_to_blit):
            if name_to_blit == "FLASHLIGHT":
                return("Lets you see in the dark.")
            elif name_to_blit == "KEY":
                return("Opens door 3.")
            elif name_to_blit == "CAKE":
                return("Is a lie.")
            elif name_to_blit == "ITEM":
                return("Your reward for the tutorial!")
            else:
                return("Nothing here!")
            
        #generate thumbnail image based on item
        def gen_img(name_to_blit):
            if name_to_blit == "FLASHLIGHT":
                return("img/flashlight.png")
            elif name_to_blit == "KEY":
                return("img/key.png")
            elif name_to_blit == "CAKE":
                return("img/cake.png")
            elif name_to_blit == "ITEM":
                return("img/invitem.png")
            else:
                return("img/empty.png") 
            
        #INV1 - slot 1
        if g.inv1 == "0":
            name_to_blit = "EMPTY"
        else:
            name_to_blit = g.inv1.upper()
        #name
        inv1_name = Box(235,105,390,40,black,grey,name_to_blit,20)
        self.image.blit(inv1_name.image,inv1_name.rect)
        #description
        inv1_desc = Box(335,150,290,95,black,grey,gen_desc(name_to_blit),20)
        self.image.blit(inv1_desc.image,inv1_desc.rect)

        self.inv1_img = Thumbnail(g,235,150,gen_img(name_to_blit))
        self.image.blit(self.inv1_img.image,self.inv1_img.rect)

        #INV2 - slot 2
        if g.inv2 == "0":
            name_to_blit = "EMPTY"
        else:
            name_to_blit = g.inv2.upper()
        #name
        inv2_name = Box(235,270,390,40,black,grey,name_to_blit,20)
        self.image.blit(inv2_name.image,inv2_name.rect)
        #description
        inv2_desc = Box(335,315,290,95,black,grey,gen_desc(name_to_blit),20)
        self.image.blit(inv2_desc.image,inv2_desc.rect)

        self.inv2_img = Thumbnail(g,235,315,gen_img(name_to_blit))
        self.image.blit(self.inv2_img.image,self.inv2_img.rect)

        if g.equip == "0":
            name_to_blit = "EMPTY"
        else:
            name_to_blit = g.equip.upper()
        equip_img = Thumbnail(g,70,150,gen_img(g.equip.upper))
        self.image.blit(equip_img.image,equip_img.rect)


    def update(self):
        self.esc_pressed()
        self.exit_game()
        self.equip()

    #equip inventory slot clicked
    def equip(self):

        def gen_img(name_to_blit):
            if name_to_blit == "FLASHLIGHT":
                return("img/flashlight.png")
            elif name_to_blit == "KEY":
                return("img/key.png")
            elif name_to_blit == "CAKE":
                return("img/cake.png")
            elif name_to_blit == "ITEM":
                return("img/invitem.png")
            else:
                return("img/empty.png")

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if self.inv1_img.is_pressed(mouse_pos, mouse_pressed):
            g.equip = g.inv1
            equip_img = Thumbnail(g,70,150,gen_img(g.equip.upper()))
            equip_img.image.fill(brown)
            equip_img = Thumbnail(g,70,150,gen_img(g.equip.upper()))
            self.image.blit(equip_img.image,equip_img.rect) 

        if self.inv2_img.is_pressed(mouse_pos, mouse_pressed):
            g.equip = g.inv2
            equip_img = Thumbnail(g,70,150,gen_img(g.equip.upper()))
            equip_img.image.fill(brown)
            equip_img = Thumbnail(g,70,150,gen_img(g.equip.upper()))
            self.image.blit(equip_img.image,equip_img.rect) 

    #closing game when exit button clicked
    def exit_game(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if self.exit_box.is_pressed(mouse_pos, mouse_pressed):
            self.kill()
            g.inv_open = False
            #sys.exit()

    #closing menu when esc pressed
    def esc_pressed(self):
        for event in pygame.event.get(): #check events
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                print("BOY LET ME OUT")
                self.kill()
                g.inv_open = False

                
#main game class
class Game:
    
    def __init__(self):

        pygame.init() #initialise pygame
        
        self.screen = pygame.display.set_mode((win_width, win_height)) #create game window
        self.clock = pygame.time.Clock() #set framerate
        self.running = True
        self.font = pygame.font.Font('arial.ttf', 32) #set font for game

        self.savename = "temp"
        self.c_type = "0"
        self.c_colour = "0"
        self.level = "0"
        self.equip = "0"
        self.inv1 = "0"
        self.inv2 = "0"

        self.inv_open = False #describes if the inventory menu is open or not

    #starts and sets up a new game
    def new(self):
        
        self.friend_count = 0
        self.item_count = 0

        self.playing = True #defines player as alive/playing

        #sprite groups
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.player = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.friends = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.ground = pygame.sprite.LayeredUpdates()
        self.items = pygame.sprite.LayeredUpdates()
        self.doors = pygame.sprite.LayeredUpdates()
        self.dialogue = pygame.sprite.LayeredUpdates()
        self.hubdoors = pygame.sprite.LayeredUpdates()

    #checks for events
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if user exits window
                self.playing = False
                self.running = False
    
    #updates all sprites
    def update(self):
        self.all_sprites.update()

    #draws the sprites on the screen
    def draw(self):
            self.screen.fill(black) #fill background with black
            self.screen.blit(self.screen, (0,0))
            self.all_sprites.draw(self.screen) #draws rect and image for all sprites
            self.clock.tick(fps)
            pygame.display.update()

    #GAME LOOPS
    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    #generate level
    def create_map(self, level):

        self.all_sprites.empty()
        self.enemies.empty()
        self.friends.empty()
        self.blocks.empty()
        self.items.empty()
        self.doors.empty()
        self.dialogue.empty()
        self.hubdoors.empty()

        self.screen.fill(black)
        for i, row in enumerate(level):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    Player(self, j, i)
                if column == "I":
                    Item(self, j, i, self.item_count)
                if column == "D":
                    Door(self, j, i)
                if column == "E":
                    Enemy(self, j, i)
                if column == "N":
                    Friend(self, j, i, self.friend_count)
                    self.friend_count += 1
                if column == "S":
                    Savepoint(self, j, i)

    #GAME LOOPS
    def tutorial(self):
        self.level = 0
        self.playing = True
        self.screen.fill(black)
        self.create_map(levelmap[self.level])
        while self.playing == True:
            self.events()
            self.update()
            self.draw()

    def level1(self):
        self.item_count += 1
        self.level = 1
        self.playing = True
        self.screen.fill(black)
        self.create_map(levelmap[self.level])
        while self.playing == True:
            self.events()
            self.update()
            self.draw()

    def level2(self):
        self.item_count += 1
        self.level = 2
        self.playing = True
        self.screen.fill(black)
        self.create_map(levelmap[self.level])
        while self.playing == True:
            self.events()
            self.update()
            self.draw()

    def level3(self):
        self.item_count += 1
        self.level = 3
        self.playing = True
        self.screen.fill(black)
        self.create_map(levelmap[self.level])
        while self.playing == True:
            self.events()
            self.update()
            self.draw()
    
    def hub(self):

        self.door_count = 0

        print(self.level)
        self.playing = True
        self.screen.fill(black)
        self.create_map(levelmap[4])

        self.doors.empty()

        for i, row in enumerate(levelmap[4]):
            for j, column in enumerate(row):
                if column == "D":
                    HubDoor(self, j, i,self.door_count)
                    self.door_count += 1

        while self.playing == True:
            self.events()
            self.update()
            self.draw()

    #CHARACTER CREATOR
    def char_creator(self):
        char = True
        
        char_title = Box(10,10,620,80,white,black,"CHARACTER CREATOR",36)
        dog_box = Box(365,150,100,50,white,black,'DOG',32)
        cat_box = Box(500,150,100,50,white,black,'CAT',32)
        col1_box = Box(365,225,100,50,white,black,'1',32)
        col2_box = Box(500,225,100,50,white,black,'2',32)
        name_box = Box(50,300,250,50,white,black,"ENTER NAME",32)
        confirm_button = Box(300,400, 300, 50, white, black, 'CONFIRM', 32)

        user_text = ''

        def gen_img():
            if g.c_type == "dog":
                if g.c_colour == "1":
                    return("img/dog1.png")
                else:
                    return("img/dog2.png")
            elif g.c_type == "cat":
                if g.c_colour == "1":
                    return("img/cat1.png")
                else:
                    return("img/cat2.png")
            else:
                return("img/empty.png")
            
        preview = Thumbnail(g,130,150,gen_img())

        while char:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    char = False
                    self.running = False

            #draw buttons on screen
            self.image = pygame.Surface((640,480))
            self.image.fill(white)
            self.screen.blit(self.image, (0,0))

            self.screen.blit(char_title.image, char_title.rect)
            self.screen.blit(dog_box.image, dog_box.rect)
            self.screen.blit(cat_box.image, cat_box.rect)
            self.screen.blit(col1_box.image, col1_box.rect)
            self.screen.blit(col2_box.image, col2_box.rect)
            self.screen.blit(name_box.image, name_box.rect)
            self.screen.blit(confirm_button.image, confirm_button.rect)

            self.screen.blit(preview.image,preview.rect)

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if confirm_button.is_pressed(mouse_pos, mouse_pressed):
                self.savename = user_text
                char = False
                
            if dog_box.is_pressed(mouse_pos, mouse_pressed):
                g.c_type = "dog"
                preview = Thumbnail(g,130,150,gen_img())
            if cat_box.is_pressed(mouse_pos, mouse_pressed):
                g.c_type = "cat"
                preview = Thumbnail(g,130,150,gen_img())
            if col1_box.is_pressed(mouse_pos, mouse_pressed):
                g.c_colour = "1"
                preview = Thumbnail(g,130,150,gen_img())
            if col2_box.is_pressed(mouse_pos, mouse_pressed):
                g.c_colour = "2"
                preview = Thumbnail(g,130,150,gen_img())

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text [:-1]
                    else:
                        user_text += event.unicode

            userbox = Box(315,300,300,50,black,grey,user_text,32)
            self.screen.blit(userbox.image,userbox.rect)

            self.clock.tick(fps)
            pygame.display.update()

    #INTRO SCREEN
    def intro(self):
        intro = True
        
        char_title = Box(10,10,620,80,white,black,"PROGRAMMING PROJECT",36)
        new_game = Box(70,100,500,100,white,black,'NEW GAME',32)
        load_game = Box(70,215,500,100,white,black,'LOAD GAME',32)
        confirm_button = Box(70,330,500,100, white, black, 'EXIT', 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            #draw buttons on screen
            self.image = pygame.Surface((640,480))
            self.image.fill(white)
            self.screen.blit(self.image, (0,0))

            self.screen.blit(char_title.image, char_title.rect)
            self.screen.blit(new_game.image,new_game.rect)
            self.screen.blit(load_game.image,load_game.rect)
            self.screen.blit(confirm_button.image, confirm_button.rect)

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if confirm_button.is_pressed(mouse_pos, mouse_pressed):
                sys.exit()

            if new_game.is_pressed(mouse_pos, mouse_pressed):
                g.savename = "temp"
                g.c_type = "0"
                g.c_colour = "0"
                g.level = "0"
                g.equip = "0"
                g.inv1 = "0"
                g.inv2 = "0"
                intro = False
                g.char_creator()

            if load_game.is_pressed(mouse_pos, mouse_pressed):

                save = open("savefile.csv","r")

                saves = save.readlines() #make savefile.csv contents a list
                loadsave = saves[len(saves) - 1] #select most recent save
                loadsave = loadsave[:-2] #remove \n from save
                loadsave = loadsave.split(",") #turn loadsave into list

                #set game attributes to save file
                g.savename = loadsave[0]
                g.c_type = loadsave[1]
                g.c_colour = loadsave[2]
                g.level = loadsave[3]
                g.equip = loadsave [4]
                g.inv1 = loadsave [5]
                g.inv2 = loadsave[6]

                save.close()
                intro = False


            self.clock.tick(fps)
            pygame.display.update()

#running the game
g = Game() #instantiate game object
g.new()
g.intro()

#loop main to keep game running continuously
while g.running:
    g.tutorial()
    g.hub()
    g.level1()
    g.hub()
    g.level2()
    g.hub()
    g.level3()
    break

pygame.quit()
sys.exit()

