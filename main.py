import sys
import pygame
import os

pygame.init()
size = width, height = 789, 500
screen = pygame.display.set_mode(size)

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Mountain(pygame.sprite.Sprite):
    image = load_image("mountains.png", colorkey=-1)
    def __init__(self):
        super().__init__(all_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.bottom = height


class Landing(pygame.sprite.Sprite):
    image = load_image("pt.png", colorkey=-1)
    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        cabina = pygame.Rect(self.rect.x + 16, self.rect.y + 38, 9, 7)
        if pygame.sprite.collide_mask(self, mountain) and\
            cabina.colliderect(mountain.rect):
            pass
        else:
            self.rect = self.rect.move(0, 1)




if __name__ == '__main__':
    v = 100
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    running = True
    mountain = Mountain()

    while running:
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Landing(event.pos)
        for val in all_sprites:
            val.update()
        clock.tick(100)
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()