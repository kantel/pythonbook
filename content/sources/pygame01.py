# Ein minimales PyGame Grundgerüst

import pygame

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("PyGame 01")
    
    background = pygame.Surface(screen.get_size())
    background.fill((0, 200, 255))
    
    mrburns = pygame.image.load("/Users/admin/git/pythonbook/content/sources/images/mrburns.png").convert_alpha()
    
    clock = pygame.time.Clock()
    keep_going = True
    
    while keep_going:
        # maximal Framerate = 30 fps
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print ("Hallo Again!")
                keep_going = False
            

        screen.blit(background, (0, 0))
        screen.blit(mrburns, (275, 100))
        pygame.display.flip()
    
    pygame.quit()
    
if __name__ == "__main__":
    main()