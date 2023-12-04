import pygame as pg
import random

class Asteroid(pg.sprite.Sprite):
    def __init__(self, type_asteroid, image_orig, image_transparent, field_size):
        pg.sprite.Sprite.__init__(self)
        self.size = random.randint(45, 80)
        self.type_asteroid = type_asteroid
        self.image_orig = pg.transform.scale(image_orig, [self.size, self.size])
        self.image_transparent = pg.transform.scale(image_transparent, [self.size, self.size])
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.WIDTH = field_size[0]
        self.HEIGHT = field_size[1]
        self.rect.x = random.randint(0, self.WIDTH - self.rect.width)
        self.rect.y = random.randint(0, self.HEIGHT - self.rect.height)
        self.corner = 0
        self.radius = 15
        self.speed = random.choice([i for i in range(-5, 5) if i != 0])
        self.last_update = pg.time.get_ticks()

    def update(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 25:  # если прошло достаточно времени
            self.last_update = now
            self.corner = (self.corner + self.speed) % 360
            if self.type_asteroid == 0:
                new_image = pg.transform.rotate(self.image_transparent, self.corner)
            else:
                new_image = pg.transform.rotate(self.image_orig, self.corner)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

            if self.type_asteroid == 0:  # Если заставка и астероиды прозрачные
                self.rect.x -= 4
            else:  # Если игра
                self.rect.x += self.speed
                self.rect.y += self.speed

            if self.rect.x < 0 or self.rect.x > self.WIDTH:
                self.rect.x = abs(self.rect.x - self.WIDTH)
            if self.rect.y < 0 or self.rect.y > self.HEIGHT:
                self.rect.y = abs(self.rect.y - self.HEIGHT)
