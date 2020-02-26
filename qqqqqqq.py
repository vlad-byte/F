from os import path
import sys
import pygame


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def load_image(name):
    fullname = path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    return image


pygame.init()
player = None
size = width, height = 600, 500
screen = pygame.display.set_mode(size)

fps = 30
clock = pygame.time.Clock()
tile_width = tile_height = 50


class Player(pygame.sprite.Sprite):
    image = load_image('mar.png')

    def __init__(self, x, y):
        super().__init__()
        self.image = Player.image
        self.rect = self.image.get_rect()
        self.move(x, y)

    def move(self, x, y):
        self.rect.x = x * tile_width + (tile_width - self.rect.width) // 2
        self.rect.y = y * tile_height + (tile_height - self.rect.height) // 2
        self.x = x
        self.y = y


class Tile(pygame.sprite.Sprite):
    grass_image = load_image('grass.png')
    box_image = load_image('box.png')

    def __init__(self, tile_tipe, x, y):
        super().__init__()
        if tile_tipe == 'grass':
            self.image = Tile.grass_image
            self.rect = self.grass_image.get_rect()
        elif tile_tipe == 'box':
            self.image = Tile.box_image
            self.rect = self.box_image.get_rect()
        self.rect.x = x * tile_width
        self.rect.y = y * tile_height


level = [list(line) for line in load_level('mro.txt')]

tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
for y in range(len(level)):
    for x in range(len(level[y])):
        if level[y][x] == '.':
            tiles_group.add(Tile('grass', x, y))
        elif level[y][x] == '#':
            tiles_group.add(Tile('box', x, y))
        elif level[y][x] == '@':
            tiles_group.add(Tile('grass', x, y))
            player = Player(x, y)
            level[y][x] = '.'
            player_group.add(player)


def start_screen():
    fon_image = load_image('fon.jpg')
    fon_image = pygame.transform.scale(fon_image, (600, 500))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main_game()
                    return
        screen.fill((0, 0, 0))
        text_cord = [0, 0]
        rect = fon_image.get_rect()
        rect.x = text_cord[0]
        rect.y = text_cord[1]
        screen.blit(fon_image, rect)
        clock.tick(fps)
        # обновление экрана
        pygame.display.flip()


def terminate():
    pygame.quit()
    sys.exit()


def main_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                x, y = player.x, player. y
                new_x, new_y = x, y
                if event.key == pygame.K_LEFT:
                    new_x, new_y = player.x - 1, player.y
                if event.key == pygame.K_RIGHT:
                    new_x, new_y = player.x + 1, player.y
                if event.key == pygame.K_UP:
                    new_x, new_y = player.x, player.y - 1
                if event.key == pygame.K_DOWN:
                    new_x, new_y = player.x, player.y + 1
                if 0 <= new_y < len(level) and 0 <= new_x < len(level[y]):
                    if level[new_y][new_x] == '.':
                        player.move(new_x, new_y)

        screen.fill(pygame.Color('blue'))
        tiles_group.draw(screen)
        player_group.draw(screen)
        pygame.display.flip()


start_screen()
main_game()
terminate()
