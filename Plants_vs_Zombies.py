import time
import pygame

from bullet import Bullet
from flagzombie import Flagzombie
from peashooter import Peashooter
from sun import Sun
from sunflower import Sunflower
from wallnut import Wallnut
from zombie import Zombie

pygame.init()
backgdsize = (1000, 600)
screen = pygame.display.set_mode(backgdsize)
pygame.display.set_caption("植物大战僵尸")

# 初始化音乐模块
pygame.mixer.init()
# 加载音乐
pygame.mixer.music.load("resources/music/18 - Crazy Dave IN-GAME.mp3")

# 用于跟随鼠标
sunflowerImg = pygame.image.load('resources/images/sunflower/SunFlower_00.png').convert_alpha()
peashooterImg = pygame.image.load('resources/images/peashooter/Peashooter_00.png').convert_alpha()
wallnutImg = pygame.image.load('resources/images/wall_nut/WallNut_00.png').convert_alpha()
# 植物槽
flowerSeed = pygame.image.load('resources/images/cards/card_sunflower.png').convert_alpha()
wallnutSeed = pygame.image.load('resources/images/cards/card_wallnut.png').convert_alpha()
peashooterSeed = pygame.image.load('resources/images/cards/card_peashooter.png').convert_alpha()
bg_img = pygame.image.load('resources/images/screen/background.jpg').convert_alpha()
seedbank_img = pygame.image.load('resources/images/screen/SeedBank.png').convert_alpha()

text = 900
sun_font = pygame.font.SysFont('arial', 25)
sun_num_surface = sun_font.render(str(text), True, (0, 0, 0))

sunFlowerGroup = pygame.sprite.Group()
peashooterGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()
zombieGroup = pygame.sprite.Group()
wallnutGroup = pygame.sprite.Group()
sunGroup = pygame.sprite.Group()

GEN_SUN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(GEN_SUN_EVENT, 1000)

GEN_BULLET_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(GEN_BULLET_EVENT, 1000)

GEN_ZOMBIE_EVENT = pygame.USEREVENT + 3
pygame.time.set_timer(GEN_ZOMBIE_EVENT, 3000)

GEN_FLAGZOMBIE_EVENT = pygame.USEREVENT + 4
pygame.time.set_timer(GEN_FLAGZOMBIE_EVENT, 3000)

choose = 0
clock = pygame.time.Clock()


def main():
    global sun_num_surface, choose
    global text
    index = 0
    while True:
        clock.tick(20)
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
        index += 1
        # 碰撞检测
        for bullet in bulletGroup:
            for zombie in zombieGroup:
                if pygame.sprite.collide_mask(bullet, zombie):
                    zombie.energy -= 1
                    bulletGroup.remove(bullet)
        for wallNut in wallnutGroup:
            for zombie in zombieGroup:
                if pygame.sprite.collide_mask(wallNut, zombie):
                    zombie.ismeetwallnut = True
                    wallNut.zombies.add(zombie)
        for peashooter in peashooterGroup:
            for zombie in zombieGroup:
                if pygame.sprite.collide_mask(peashooter, zombie):
                    zombie.ismeetwallnut = True
                    peashooter.zombies.add(zombie)
        for sunflower in sunFlowerGroup:
            for zombie in zombieGroup:
                if pygame.sprite.collide_mask(sunflower, zombie):
                    zombie.ismeetwallnut = True
                    sunflower.zombies.add(zombie)
        screen.blit(bg_img, (0, 0))
        screen.blit(seedbank_img, (250, 0))
        screen.blit(sun_num_surface, (270, 60))

        screen.blit(flowerSeed, (320, 0))
        screen.blit(peashooterSeed, (382, 0))
        screen.blit(wallnutSeed, (446, 0))
        sunFlowerGroup.update(index)
        sunFlowerGroup.draw(screen)
        peashooterGroup.update(index)
        peashooterGroup.draw(screen)
        bulletGroup.update(index)
        bulletGroup.draw(screen)
        zombieGroup.update(index)
        zombieGroup.draw(screen)
        wallnutGroup.update(index)
        wallnutGroup.draw(screen)
        sunGroup.update(index)
        sunGroup.draw(screen)

        (x, y) = pygame.mouse.get_pos()
        if choose == 1:
            screen.blit(sunflowerImg, (x, y))
        elif choose == 2:
            screen.blit(peashooterImg, (x, y))
        elif choose == 3:
            screen.blit(wallnutImg, (x, y))
        for event in pygame.event.get():
            if event.type == GEN_SUN_EVENT:
                for sprite in sunFlowerGroup:
                    now = time.time()
                    if now - sprite.lasttime >= 5:
                        sun = Sun(sprite.rect)
                        sunGroup.add(sun)
                        sprite.lasttime = now

            if event.type == GEN_BULLET_EVENT:
                for sprite in peashooterGroup:
                    bullet = Bullet(sprite.rect, backgdsize)
                    bulletGroup.add(bullet)

            if event.type == GEN_ZOMBIE_EVENT:
                zombie = Zombie()
                zombieGroup.add(zombie)

            if event.type == GEN_FLAGZOMBIE_EVENT:
                flagzombie = Flagzombie()
                zombieGroup.add(flagzombie)

            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed_key = pygame.mouse.get_pressed()
                if pressed_key[0] == 1:
                    x, y = pygame.mouse.get_pos()
                    print(x, y)
                    if 320 <= x <= 382 and 0 <= y <= 89 and text >= 50:
                        # 点中了太阳花
                        choose = 1
                    elif 383 <= x < 446 and 0 <= y <= 89 and text >= 100:
                        # 点中了豌豆射手
                        choose = 2
                    elif 447 <= x < 511 and 0 <= y <= 89 and text >= 50:
                        # 点中了坚果墙
                        choose = 3
                    elif 250 < x < 1200 and 90 < y < 600:
                        if choose == 1:
                            current_time = time.time()
                            sunflower = Sunflower(current_time)
                            sunflower.rect.x = x
                            sunflower.rect.y = y
                            sunFlowerGroup.add(sunflower)
                            choose = 0

                            text -= 50
                            sun_font = pygame.font.SysFont('arial', 25)
                            sun_num_surface = sun_font.render(str(text), True, (0, 0, 0))
                        elif choose == 2:
                            peashooter = Peashooter()
                            peashooter.rect.y = y
                            peashooter.rect.x = x
                            peashooterGroup.add(peashooter)
                            choose = 0

                            text -= 100
                            sun_font = pygame.font.SysFont('arial', 25)
                            sun_num_surface = sun_font.render(str(text), True, (0, 0, 0))
                        elif choose == 3:
                            wallnut = Wallnut()
                            wallnut.rect.y = y
                            wallnut.rect.x = x
                            wallnutGroup.add(wallnut)
                            choose = 0

                            text -= 50
                            sun_font = pygame.font.SysFont('arial', 25)
                            sun_num_surface = sun_font.render(str(text), True, (0, 0, 0))
                    for sun in sunGroup:
                        if sun.rect.collidepoint(x, y):
                            sunGroup.remove(sun)
                            text += 50
                            sun_font = pygame.font.SysFont('arial', 25)
                            sun_num_surface = sun_font.render(str(text), True, (0, 0, 0))

        pygame.display.update()


if __name__ == '__main__':
    main()
