#RC, 1st, test
import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)


sky_surface = pygame.image.load('images/Sky.png')
ground_surface = pygame.image.load('images/ground.png')
text_surface = test_font.render('My game', False, 'black')

###CREATE A MOVING SNAIL HERE THAT WILL CROSS THE SCREEN


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300,50))

    pygame.display.update()
    clock.tick(60)