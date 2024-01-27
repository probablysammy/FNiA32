import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    pygame.display.set_caption("FNiA32")

    #for the main game loop
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                

    pygame.quit() #quits if the game loop exits

main()