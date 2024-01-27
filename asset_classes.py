import pygame

W = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

class Map(pygame.sprite.Sprite):
    
    def __init__(self, game):
        
        self.game = game
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.all_sprites)

        self.x = 0
        self.y = 0

        image_to_load = pygame.image.load("assets/images/map.png") #load sprite image
        self.image = pygame.Surface([1920, 1080])
        self.image.blit(image_to_load, (0,0))
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y