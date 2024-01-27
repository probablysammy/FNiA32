import pygame

WIDTH = 1920
HEIGHT = 1080

W = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

BUTTON_LAYER = 4
MAP_LAYER = 3
HEAVISIDE_LAYER = 2
STEVE_LAYER = 1
HELL_LAYER = 0

global camera
camera = 7

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
        elif camera == 1:
            self.image.blit(self.img1, (0,0))
        elif camera == 2:
            self.image.blit(self.img2, (0,0))
        elif camera == 3:
            self.image.blit(self.img3, (0,0))
        elif camera == 4:
            self.image.blit(self.img4, (0,0))
        else:
            self.hide()

    def update(self):
        self.map_check()


class MapButton(pygame.sprite.Sprite):
    def __init__(self, game, image, mapid, x, y):
        
        self.game = game
        self._layer = BUTTON_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.mapid = mapid

        self.x = x
        self.y = y

        image_to_load = pygame.image.load(image) #load sprite image
        self.image = pygame.Surface([1920, 1080], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.image.set_colorkey(RED)
        self.image.blit(image_to_load, (0,0))
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False
    
    def update(self):
        global camera
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if self.is_pressed(mouse_pos, mouse_pressed):
            camera = self.mapid #changing camera value
            
        print(camera)



class A32(pygame.sprite.Sprite):
    def __init__(self,game):
        self.game = game
        self._layer = STEVE_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = 0
        self.y = 0

        self.image_to_load = pygame.image.load("assets/images/a32.png")
        self.image = pygame.Surface([1920, 1080])
        self.image.blit(self.image_to_load, (0,0))
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

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

        if self.sammy:
            self.image.blit(self.jimage_to_load, (0,0))
        else:
            self.image.blit(self.image_to_load, (0,0))
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


    def show(self):
        self.game.all_sprites.change_layer(self, HEAVISIDE_LAYER)

    def hide(self):
        self.game.all_sprites.change_layer(self, HELL_LAYER)

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
        self.jamie_check()
        self.camera_check()



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
        self.running = True #maisn game loop
        self.playing = True

        self.image = pygame.image.load("assets/images/a32.png") #background

    #start game
    def start(self):
        #sprite groups
        self.all_sprites = pygame.sprite.LayeredUpdates()

        A32(self)
        Map(self, "assets/images/minimap_b52.png", "assets/images/minimap_foodatrium.png", "assets/images/minimap_library.png", "assets/images/minimap_path.png", "assets/images/minimap_csatrium.png", )

        b52_button = MapButton(self,"assets/images/b52_button.png",0,1085,425)
        foodatrium_button = MapButton(self, "assets/images/foodatrium_button.png",1,1175,601)
        library_button = MapButton(self, "assets/images/library_button.png",2,1569,405)
        path_button = MapButton(self, "assets/images/path_button.png",3,1528,573)
        csatrium_button = MapButton(self, "assets/images/csatrium_button.png",4,1587,742)

        b52 = Room(self,"assets/images/b52.png","assets/images/b52jamie.png",[1,2],0)
        foodatrium = Room(self,"assets/images/foodatrium.png","assets/images/foodatriumjamie.png",[0,5],1)
        library = Room(self,"assets/images/library.png","assets/images/libraryjamie.png",[0,3],2)
        path = Room(self,"assets/images/path.png","assets/images/pathjamie.png",[2,4],3)
        csatrium = Room(self,"assets/images/csatrium.png","assets/images/csatriumjamie.png",[3,6],4)
        
        b52.sammy = True

    #whatever events is
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
        self.screen.fill(BLACK) #fill background with black
        self.screen.blit(self.image,(0,0)) #office background
        self.all_sprites.draw(self.screen) #draws rect and image for all sprites
        self.clock.tick(60)
        pygame.display.update()
        
    #game loop
    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

        

game = Game()
game.start()
while game.running:
    game.main()

pygame.quit()

#            ^__^
#            (oo)\_______
#            (__)\       )\/\
#                ||----w |
#                ||     ||
#                ||     ||

#                MOOOOOOO