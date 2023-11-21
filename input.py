import pygame
pygame.init()
void = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
run = True
while run:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                 print(event)