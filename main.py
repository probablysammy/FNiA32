from typing import Any
import pygame
import random
import time
from pygame import mixer

WIDTH = 1920
HEIGHT = 1080

W = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

BUTTON_LAYER = 5
MAP_LAYER = 4
SECRET_LAYER = 3
HEAVISIDE_LAYER = 2
STEVE_LAYER = 1
HELL_LAYER = 0

NIGHT = 1

global jumpscare
jumpscare = True

global power
power = 100

global door
door = 0

global HOUR
HOUR = 0

global camera
camera = 7

global timer
timer = 0

global counter
counter = 0

global AILEVEL
AILEVEL = 10

global jamiePos
jamiePos = 0

global b52, foodatrium, library, path, csatrium, leftentrance, rightentrance

mixer.init()

global cameratoggle_sound
global doortoggle_sound
global jumpscare_sound
cameratoggle_sound = pygame.mixer.Sound("assets/audio/cameratoggle.wav")
doortoggle_sound = pygame.mixer.Sound("assets/audio/door.wav")
jumpscare_sound = pygame.mixer.Sound("assets/audio/jamiescare.wav")

global markiplier
markiplier = pygame.mixer.Sound("assets/audio/mark.wav")

#5350 TICKS IN 8:55 - LEN OF NIGHT
#892 TICKS IN 1:29 - LEN OF HOUR

# SPRITE CODE

class Map(pygame.sprite.Sprite):
    def __init__(self, game, i0, i1, i2, i3, i4):
        
        self.game = game
        self._layer = MAP_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = 0
        self.y = 0

        self.img0 = pygame.image.load(i0) #load sprite image
        self.img1 = pygame.image.load(i1)
        self.img2 = pygame.image.load(i2)
        self.img3 = pygame.image.load(i3)
        self.img4 = pygame.image.load(i4)
        self.image = pygame.Surface([1920, 1080], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def show(self):
        self.game.all_sprites.change_layer(self, MAP_LAYER)

    def hide(self):
        self.game.all_sprites.change_layer(self, HELL_LAYER)

    def map_check(self):
        if camera == 0:
            self.image.blit(self.img0, (0,0))
            self.show()
        elif camera == 1:
            self.image.blit(self.img1, (0,0))
            self.show()
        elif camera == 2:
            self.image.blit(self.img2, (0,0))
            self.show()
        elif camera == 3:
            self.image.blit(self.img3, (0,0))
            self.show()
        elif camera == 4:
            self.image.blit(self.img4, (0,0))
            self.show()
        else:
            self.hide()

    def update(self):
        self.map_check()


class Time(pygame.sprite.Sprite):
    def __init__(self, game, i0, i1, i2, i3, i4, i5, i6):
        self.game = game
        self._layer = BUTTON_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = 20
        self.y = 20

        self.img0 = pygame.image.load(i0) #load sprite image
        self.img1 = pygame.image.load(i1)
        self.img2 = pygame.image.load(i2)
        self.img3 = pygame.image.load(i3)
        self.img4 = pygame.image.load(i4)
        self.img5 = pygame.image.load(i5)
        self.img6 = pygame.image.load(i6)

        self.image = pygame.Surface([70, 40],pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def time_check(self):
        if HOUR == 0:
            self.image.blit(self.img0, (0,0))
        elif HOUR == 1:
            self.image.blit(self.img1, (0,0))
        elif HOUR == 2:
            self.image.blit(self.img2, (0,0))
        elif HOUR == 3:
            self.image.blit(self.img3, (0,0))
        elif HOUR == 4:
            self.image.blit(self.img4, (0,0))
        elif HOUR == 5:
            self.image.blit(self.img5, (0,0))
        else:
            self.image.blit(self.img6, (0,0))

    def update(self):
        self.time_check()
    

class Power(pygame.sprite.Sprite):
    def __init__(self, game, i0, i1, i2, i3, i4, i5, i6, i7, i8, i9):
        self.game = game
        self._layer = BUTTON_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = 20
        self.y = 80

        self.img0 = pygame.image.load(i0) #load sprite image
        self.img1 = pygame.image.load(i1)
        self.img2 = pygame.image.load(i2)
        self.img3 = pygame.image.load(i3)
        self.img4 = pygame.image.load(i4)
        self.img5 = pygame.image.load(i5)
        self.img6 = pygame.image.load(i6)
        self.img7 = pygame.image.load(i7)
        self.img8 = pygame.image.load(i8)
        self.img9 = pygame.image.load(i9)

        self.image = pygame.Surface([332, 80],pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def power_check(self):
        if power > 90:
            self.image.blit(self.img0, (0,0))
        elif power > 80:
            self.image.blit(self.img1, (0,0))
        elif power > 70:
            self.image.blit(self.img2, (0,0))
        elif power > 60:
            self.image.blit(self.img3, (0,0))
        elif power > 50:
            self.image.blit(self.img4, (0,0))
        elif power > 40:
            self.image.blit(self.img5, (0,0))
        elif power > 30:
            self.image.blit(self.img6, (0,0))
        elif power > 20:
            self.image.blit(self.img7, (0,0))
        elif power > 10:
            self.image.blit(self.img8, (0,0))
        else:
            self.image.blit(self.img9, (0,0))

    def update(self):
        global power
        self.power_check()
        
        if timer % 10 == 0:
            if door != 0 and camera != 7:
                power -= 0.6            
            elif door != 0 or camera != 7:
                power -= 0.33
            else:
                power -= 0.08
        
        #print("power: ", power)


class MapButton(pygame.sprite.Sprite):
    def __init__(self, game, image, mapid, x, y, width, height):
        
        self.game = game
        self._layer = BUTTON_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.mapid = mapid

        self.x = x
        self.y = y

        image_to_load = pygame.image.load(image) #load sprite image
        self.image = pygame.Surface([width, height], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.image.set_colorkey(RED)
        self.image.blit(image_to_load, (0,0))
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                pygame.mixer.Sound.play(cameratoggle_sound)
                return True
            return False
        return False
    
    #OCCURS EVERY FRAME!
    def update(self):
        global camera
        global HOUR
        global timer
        global AILEVEL
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        self.map_check()
        HOUR = timer // 892
        
        #if timer % 900 == 0:
            #AILEVEL += 1

        if self.is_pressed(mouse_pos, mouse_pressed):
            camera = self.mapid #changing camera value
        

    def show(self):
        self.game.all_sprites.change_layer(self, BUTTON_LAYER)

    def hide(self):
        self.game.all_sprites.change_layer(self, HELL_LAYER)

    def map_check(self):
        if camera == 7:
            self.hide()
        else:
            self.show()
            
class DoorButton(pygame.sprite.Sprite):
    def __init__(self, game, image, x, y, doorid):
        
        self.game = game
        self._layer = BUTTON_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y

        self.doorid = doorid

        image_to_load = pygame.image.load(image) #load sprite image
        self.image = pygame.Surface([210, 120], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.image.blit(image_to_load, (0,0))
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                pygame.mixer.Sound.play(doortoggle_sound)
                return True
            return False
        return False
    
    #OCCURS EVERY FRAME!
    def update(self):
        global door
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        self.map_check()

        if self.is_pressed(mouse_pos, mouse_pressed):
            if door == self.doorid:
                door = 0
            else:
                door = self.doorid  
        
    def show(self):
        self.game.all_sprites.change_layer(self, BUTTON_LAYER)

    def hide(self):
        self.game.all_sprites.change_layer(self, HELL_LAYER)

    def map_check(self):
        if camera != 7:
            self.hide()
        else:
            self.show()
    

class CameraButton(pygame.sprite.Sprite):
    def __init__(self,game):
        self.game = game
        self._layer = BUTTON_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = 182
        self.y = 990

        self.image_to_load = pygame.image.load("assets/images/camerabutton.png")
        self.image = pygame.Surface([1920, 1080], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.image.blit(self.image_to_load, (0,0))
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                if camera == 7:
                    music = pygame.mixer.music.load("assets/audio/camera.wav")
                    pygame.mixer.music.set_volume(1)
                if camera != 7:
                    music = pygame.mixer.music.load("assets/audio/office.wav")
                    pygame.mixer.music.set_volume(0.5)
                pygame.mixer.Sound.play(cameratoggle_sound)
                pygame.mixer.music.play(-1)
                return True
            return False
        return False
    
    def update(self):
        global camera
        global timer
        global HOUR
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if self.is_pressed(mouse_pos, mouse_pressed):
            if camera == 7:
                camera = 0
            else:
                camera = 7
        
        timer += 1        
                
                    
class A32(pygame.sprite.Sprite):
    def __init__(self,game):
        self.game = game
        self._layer = STEVE_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = 0
        self.y = 0

        self.sammyleft = False
        self.sammyright = False

        self.a32_image = pygame.image.load("assets/images/a32.png")
        self.left_image = pygame.image.load("assets/images/a32jamieleft.png")
        self.right_image = pygame.image.load("assets/images/a32jamieright.png")
        self.left_door = pygame.image.load("assets/images/a32leftclosed.png")
        self.right_door = pygame.image.load("assets/images/a32rightclosed.png")

        self.image = pygame.Surface([1920, 1080])
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.image.blit(self.a32_image, (0,0))
        
    def jamie_check(self):
        if self.sammyleft == True:
            self.image.blit(self.left_image, (0,0))
            
        elif self.sammyright == True:
            self.image.blit(self.right_image, (0,0))
            
    def door_check(self):
        if door == 0:
            self.image.blit(self.a32_image, (0,0))
            self.jamie_check()
        if door == 1:
            self.image.blit(self.left_door, (0,0))
        if door == 2:
            self.image.blit(self.right_door, (0,0))
        
    def update(self):
        self.jamie_check()
        self.door_check()


class Room(pygame.sprite.Sprite):
    def __init__(self, game, image, jimage, adj_list, id):
        
        self.game = game
        self._layer = HELL_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.sammy = False
        self.adj_list = adj_list
        self.id = id

        self.x = 0
        self.y = 0

        self.image_to_load = pygame.image.load(image)
        self.jimage_to_load = pygame.image.load(jimage)
        self.image = pygame.Surface([1920, 1080])
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def show(self):
        self.game.all_sprites.change_layer(self, HEAVISIDE_LAYER)

    def hide(self):
        self.game.all_sprites.change_layer(self, HELL_LAYER)

    def map_check(self):
        if camera == 7:
            self.hide()
        else:
            self.show()

    def jamie_check(self):
        if self.sammy:
            self.image.blit(self.jimage_to_load, (0,0))
        else:
            self.image.blit(self.image_to_load, (0,0))

    def camera_check(self):
        if self.id == camera:
            self.show()
        else:
            self.hide()

    def update(self):
        self.map_check()
        self.jamie_check()
        self.camera_check()

class Entrance(pygame.sprite.Sprite):
    def __init__(self, game, image, adj_list, id):
        
        self.game = game
        self._layer = HEAVISIDE_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.sammy = False
        self.adj_list = adj_list
        self.id = id

        self.x = 0
        self.y = 0

        self.image = pygame.Surface([1920, 1080])
        self.rect = self.image.get_rect()


class Jamie(pygame.sprite.Sprite):

    def __init__(self,game):

        self.room = 0
        self.roomlist = b52.adj_list
        b52.sammy = True

        self.game = game
        self._layer = HELL_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.Surface([1920, 1080])
        self.rect = self.image.get_rect()

    def move_check(self):
        
        global counter
        global AILEVEL
        global jumpscare
        global door
        global camera
        global timer
        global HOUR
        global power
        global jamiePos
        global b52, foodatrium, library, path, csatrium, leftentrance, rightentrance, a32

        if self.room == 0:
            self.roomlist = b52.adj_list
        if self.room == 1:
            self.roomlist = foodatrium.adj_list
        if self.room == 2:
            self.roomlist = library.adj_list
        if self.room == 3:
            self.roomlist = path.adj_list
        if self.room == 4:
            self.roomlist = csatrium.adj_list
        if self.room == 5:
            self.roomlist = leftentrance.adj_list
        if self.room == 6:
            self.roomlist = rightentrance.adj_list

        if timer % 44 == 0:
            if random.randint(0, 20) <= AILEVEL:
                index = random.randint(0, 4)
                self.room = self.roomlist[index]
                if self.room == 0:
                    b52.sammy = True
                    foodatrium.sammy = False
                    library.sammy = False
                elif self.room == 1:
                    foodatrium.sammy = True
                    b52.sammy = False
                    a32.sammyleft = False
                elif self.room == 2:
                    library.sammy = True
                    b52.sammy = False
                    path.sammy = False
                elif self.room == 3:
                    path.sammy = True
                    library.sammy = False
                    csatrium.sammy = False
                elif self.room == 4:
                    csatrium.sammy = True
                    path.sammy = False
                    a32.sammyright = False
                elif self.room == 5:
                    a32.sammyleft = True
                    foodatrium.sammy = False
                elif self.room == 6:
                    a32.sammyright = True
                    csatrium.sammy = False
                elif self.room == 7:
                    if a32.sammyleft == True and door == 1:
                        self.room = 0
                        a32.sammyleft = False
                        b52.sammy = True
                    elif a32.sammyright == True and door == 2:
                        self.room = 0
                        a32.sammyright = False
                        b52.sammy = True
                    else:
                        power = 0

    def update(self):
        self.move_check()


#doorbutton changes global door with door id so 1 is left door and 2 is right

# GAME CODE
#                                 |\    /|
#                              ___| \,,/_/
#                           ---__/ \/    \
#                          __--/     (D)  \
#                          _ -/    (_      \
#                         // /       \_ /  -\
#   __-------_____--___--/           / \_ O o)
#  /                                 /   \__/
# /                                 /
#||          )                   \_/\
#||         /              _      /  |
#| |      /--______      ___\    /\  :
#| /   __-  - _/   ------    |  |   \ \
# |   -  -   /                | |     \ )
# |  |   -  |                 | )     | |
#  | |    | |                 | |    | |
#  | |    < |                 | |   |_/
#  < |    /__\                <  \
#  /__\                       /___\

class Game:

    #constructor
    def __init__(self):
        pygame.init() #initialises pygame
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) #create game window
        self.clock = pygame.time.Clock() #set framerate
        
        icon = pygame.image.load('assets/images/icon.png')
        pygame.display.set_icon(icon)
        
        pygame.display.set_caption("Five Nights in A32")
        self.running = True #main game loop
        self.playing = True

        self.endimage = pygame.image.load("assets/images/newspaper.png") #background
        self.dieimage = pygame.image.load("assets/images/jumpscare.png") #jumpscare image

    #start game
    def start(self):
        #sprite groups
        global b52, foodatrium, library, path, csatrium, leftentrance, rightentrance, a32
        self.all_sprites = pygame.sprite.LayeredUpdates()

        music = pygame.mixer.music.load("assets/audio/office.wav")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        
        Map(self, "assets/images/minimap_b52.png", "assets/images/minimap_foodatrium.png", "assets/images/minimap_library.png", "assets/images/minimap_path.png", "assets/images/minimap_csatrium.png", )
        Time(self, "assets/images/time/12.png", "assets/images/time/1.png", "assets/images/time/2.png", "assets/images/time/3.png", "assets/images/time/4.png", "assets/images/time/5.png", "assets/images/time/6.png")
        Power(self, "assets/images/power/100.png", "assets/images/power/90.png", "assets/images/power/80.png", "assets/images/power/70.png", "assets/images/power/60.png", "assets/images/power/50.png", "assets/images/power/40.png", "assets/images/power/30.png", "assets/images/power/20.png", "assets/images/power/10.png")

        MapButton(self,"assets/images/b52_button.png",0,1085,425,235,124)
        MapButton(self, "assets/images/foodatrium_button.png",1,1175,601,235,125)
        MapButton(self, "assets/images/library_button.png",2,1569,405,282,125)
        MapButton(self, "assets/images/path_button.png",3,1528,573,131,125)
        MapButton(self, "assets/images/csatrium_button.png",4,1587,742,206,110)
        
        DoorButton(self, "assets/images/leftdoor.png", 25, 800, 1)
        DoorButton(self, "assets/images/rightdoor.png", 1685, 80, 2)

        b52 = Room(self,"assets/images/b52.png","assets/images/b52jamie.png",[1,2,2,2,1],0)
        foodatrium = Room(self,"assets/images/foodatrium.png","assets/images/foodatriumjamie.png",[0,5,5,5,0],1)
        library = Room(self,"assets/images/library.png","assets/images/libraryjamie.png",[3,0,0,0,3],2)
        path = Room(self,"assets/images/path.png","assets/images/pathjamie.png",[2,4,4,4,2],3)
        csatrium = Room(self,"assets/images/csatrium.png","assets/images/csatriumjamie.png",[3,6,6,6,3],4)
        
        a32 = A32(self)
        rightentrance = Room(self,"assets/images/a32jamieright.png","assets/images/a32jamieright.png",[4,7,4,7,4],6)
        leftentrance = Room(self,"assets/images/a32jamieleft.png","assets/images/a32jamieleft.png",[1,7,1,7,1],5)

        CameraButton(self)
        Jamie(self)

    #whatever events is
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if user exits window
                self.running = False
                self.playing = False

    #game loop updates
    def update(self):
        self.all_sprites.update() #update sprites in 'all_sprites' group

    #game loop updates
    def draw(self):
        self.screen.fill(BLACK) #fill background with black
        self.all_sprites.draw(self.screen) #draws rect and image for all sprites
        self.clock.tick(60)
        pygame.display.update()
        
    def jumpscare(self):
        self.playing = True
        pygame.mixer.music.play(-1)
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(jumpscare_sound)
        while self.playing:
            self.events()
            self.update()
            self.screen.fill(BLACK) #fill background with black
            self.screen.blit(self.dieimage,(0,0)) #jumpscare background
            self.clock.tick(60)
            pygame.display.update()
        
    #game loop
    def main(self):
        global jumpscare
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            if timer == 5352:
                self.playing = False
                jumpscare = False
            if power <= 0:
                self.playing = False
                jumpscare = True

    def end(self):
        self.playing = True
        music = pygame.mixer.music.load("assets/audio/end.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(markiplier)
        while self.playing:
            self.events()
            self.update()
            self.screen.fill(BLACK) #fill background with black
            self.screen.blit(self.endimage,(0,0)) #end background
            self.clock.tick(60)
            pygame.display.update()     

game = Game()
game.start()
while game.running:
    game.main()
    if jumpscare == True:
        game.jumpscare()
    else:
        game.end()


pygame.quit()

#            ^__^
#            (oo)\_______
#            (__)\       )\/\
#                ||----w |
#                ||     ||
#                ||     ||

#                MOOOOOOO