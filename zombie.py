import random

import pygame


class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super(Zombie, self).__init__()
        self.image = pygame.image.load('resources/images/zombie/Zombie_0.png').convert_alpha()
        self.images = [pygame.image.load('resources/images/zombie/Zombie_{}.png'.format(i)).convert_alpha()
                       for i in range(0, 22)]
        self.dieimages = [pygame.image.load('resources/images/zombie/ZombieDie_{}.png'.format(i)).convert_alpha()
                          for i in range(0, 10)]
        self.attackimages = [pygame.image.load('resources/images/zombie/ZombieAttack_{}.png'.format(i)).convert_alpha()
                             for i in range(0, 21)]
        self.rect = self.images[0].get_rect()
        self.rect.y = 25 + random.randrange(0, 5) * 100
        self.rect.x = 1000
        self.speed = 5
        self.energy = 6
        self.dietimes = 0
        self.ismeetwallnut = False
        self.isalive = True

    def update(self, *args, **kwargs) -> None:
        if self.energy > 0:
            self.image = self.images[args[0] % len(self.images)]
            if self.rect.x > 250 and self.ismeetwallnut:
                self.image = self.attackimages[args[0] % len(self.attackimages)]
            if self.rect.x > 250 and not self.ismeetwallnut:
                self.rect.x -= self.speed
        else:
            if self.dietimes < 20:
                self.image = self.dieimages[self.dietimes // 2]
                self.dietimes += 1
            elif self.dietimes > 30:
                self.isalive = False
                self.kill()
            else:
                self.dietimes += 1
