# testing image display with pygame
import pygame, os
f = './DCFC0689.JPG'
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
pygame.display.set_caption('Imager')
clock = pygame.time.Clock()
void = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
image = pygame.image.load(f).convert()
run = True
while run:
    clock.tick(120)
    void.blit(image, (0, 0))
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.display.flip()


# import pygame, os
# pygame.init()
# clock = pygame.time.Clock()
# os.environ['SDL_VIDEO_CENTERED'] = '1'
# screen = (pygame.display.Info().current_w/2, pygame.display.Info().current_h/2)
# window = pygame.display.set_mode(screen, pygame.RESIZABLE)
# run = True
# while run:
#     clock.tick(300)
#     window.fill('white')
#     for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#             if event.type == pygame.KEYDOWN:
#                  print(event)
#     pygame.display.flip()