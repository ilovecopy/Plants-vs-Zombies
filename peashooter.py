import pygame


class Peashooter(pygame.sprite.Sprite):
    def __init__(self):
        super(Peashooter, self).__init__()
        self.image = pygame.image.load('resources/images/peashooter/Peashooter_00.png').convert_alpha()
        self.images = [pygame.image.load('resources/images/peashooter/Peashooter_{:02d}.png'.format(i)).convert_alpha()
                       for i in range(0, 13)]
        self.rect = self.images[0].get_rect()
        self.energy = 3 * 15
        self.zombies = set()

    def update(self, *args, **kwargs) -> None:
        for zombie in self.zombies:
            if zombie.isalive == False:
                continue
            self.energy -= 1
        if self.energy <= 0:
            self.kill()
            for zombie in self.zombies:
                zombie.ismeetwallnut = False
