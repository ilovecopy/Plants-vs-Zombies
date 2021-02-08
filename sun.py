import random

import pygame


class Sun(pygame.sprite.Sprite):
    def __init__(self, rect):
        super(Sun, self).__init__()
        self.image = pygame.image.load('resources/images/sun/Sun_1.png').convert_alpha()

        self.images = [pygame.image.load('resources/images/sun/Sun_{}.png'.format(i)).convert_alpha()
                       for i in range(1, 18)]
        self.rect = self.images[0].get_rect()
        offsettop = random.randint(-50, 50)
        offsetleft = random.randint(-50, 50)

        self.rect.y = rect.y + offsettop
        self.rect.x = rect.x + offsetleft

    def update(self, *args, **kwargs) -> None:
        self.image = self.images[args[0] % len(self.images)]
