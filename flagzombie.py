from zombie import Zombie
import pygame


class Flagzombie(Zombie):
    def __init__(self):
        super(Flagzombie, self).__init__()
        self.image = pygame.image.load('resources/images/flag_zombie/FlagZombie_0.png').convert_alpha()
        self.images = [pygame.image.load('resources/images/flag_zombie/FlagZombie_{}.png'.format(i)).convert_alpha()
                       for i in range(0, 12)]
        self.speed = 4
        self.energy=7
        self.dietimes = 0
        self.ismeetwallnut = False