import pygame


class Wallnut(pygame.sprite.Sprite):
    def __init__(self):
        super(Wallnut, self).__init__()
        self.image = pygame.image.load('resources/images/wall_nut/WallNut_00.png').convert_alpha()
        self.images = [pygame.image.load('resources/images/wall_nut/WallNut_{:02d}.png'.format(i)).convert_alpha()
                       for i in range(0, 13)]
        self.crackedimg = [pygame.transform.smoothscale(
            pygame.image.load('resources/images/wall_nut/Wallnut_body.png').convert_alpha(),
            (self.image.get_rect().width, self.image.get_rect().height)),
            pygame.transform.smoothscale(
                pygame.image.load('resources/images/wall_nut/Wallnut_cracked1.png').convert_alpha(),
                (self.image.get_rect().width, self.image.get_rect().height)),
            pygame.transform.smoothscale(
                pygame.image.load('resources/images/wall_nut/Wallnut_cracked2.png').convert_alpha(),
                (self.image.get_rect().width, self.image.get_rect().height))]
        self.rect = self.images[0].get_rect()
        self.energy = 8 * 15
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

        if self.energy == 8 * 15:
            self.image = self.images[args[0] % len(self.images)]
        elif 6 * 15 <= self.energy < 8 * 15:
            self.image = self.crackedimg[0]
        elif 3 * 15 <= self.energy < 6 * 15:
            self.image = self.crackedimg[1]
        else:
            self.image = self.crackedimg[2]
