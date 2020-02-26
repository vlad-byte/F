import os
import pygame
from static_map import get_map


def draw_image(content):
    map_file = 'image.png'
    with open(map_file, 'wb') as file:
        file.write(get_map(content))
    pygame.init()
    screen = pygame.display.set_mode((650, 450))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    running = True
    fps = 30
    clock = pygame.time.Clock()
    t = tt = 0
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    content["ll"] = str(float(content["ll"][:content["ll"].find(',')]) - content["z"] * 90 / 650) + ',' + content["ll"][content["ll"].find(',') + 1:]
                elif event.key == pygame.K_RIGHT:
                    content["ll"] = str(float(content["ll"][:content["ll"].find(',')]) + content["z"] * 90 / 650) + ',' + content["ll"][content["ll"].find(',') + 1:]
                elif event.key == pygame.K_UP:
                    content["ll"] = content["ll"][:content["ll"].find(',')] + ',' + str(float(content["ll"][content["ll"].find(',') + 1:]) - content["z"] * 90 / 450)
                    print(content["ll"])
                elif event.key == pygame.K_DOWN:
                    content["ll"] = content["ll"][:content["ll"].find(',')] + ',' + str(float(content["ll"][content["ll"].find(',') + 1:]) + content["z"] * 90 / 450)
        with open(map_file, 'wb') as file:
            file.write(get_map(content))
        pygame.init()
        screen = pygame.display.set_mode((650, 450))
        screen.blit(pygame.image.load(map_file), (t, tt))
        pygame.display.flip()
    pygame.quit()
    os.remove(map_file)
