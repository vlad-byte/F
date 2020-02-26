import os
import pygame
from static_map import get_map


def draw_image(content):
    map_file = 'image.png'
    with open(map_file, 'wb') as file:
        file.write(get_map(content))
    pygame.init()
    screen = pygame.display.set_mode((450, 450))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    running = True
    fps = 30
    clock = pygame.time.Clock()
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_RIGHT:
                    if content["z"] < 18:
                        content["z"] += 1
                elif event.button == pygame.BUTTON_LEFT:
                    if content["z"] > 1:
                        content["z"] -= 1
        with open(map_file, 'wb') as file:
            file.write(get_map(content))
        pygame.init()
        screen = pygame.display.set_mode((450, 450))
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
    pygame.quit()
    os.remove(map_file)
