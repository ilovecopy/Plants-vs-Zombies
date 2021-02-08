import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, wdrect, bg_size):
        super(Bullet, self).__init__()
        self.image = pygame.image.load('resources/images/bullet/Bullet_1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = wdrect[0] + 45
        self.rect.y = wdrect[1]
        self.width = bg_size[0]
        self.speed = 5

    def update(self, *args, **kwargs) -> None:
        if self.rect.x < self.width:
            self.rect.x += self.speed
        else:
            self.kill()
