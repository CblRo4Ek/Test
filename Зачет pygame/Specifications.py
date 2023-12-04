import pygame as pg
import sys
from Asteroid import *
from Explosion import *
from Player import *
from Rocket import *


WIDTH = 900
HEIGHT = 630

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('RiceRocks')
clock = pg.time.Clock()


# Загрузка графики
asteroid_image = pg.image.load('Images/Астероид.png')
asteroid_transparent_image = pg.image.load('Images/Астероид полупрозрачный.png')
ship_image = pg.image.load('Images/Корабль.png')
rocket_image = pg.image.load('Images/Ракета.png')
ship_with_fire_image = pg.image.load('Images/Корабль с огнем.png')
explosion_image = pg.image.load('Images/Взрыв.png')

# Установка фона
sky_image = pg.image.load('Images/Небо.png')
sky = sky_image.get_rect()


asteroids = pg.sprite.Group()
rockets = pg.sprite.Group()
all_sprites = pg.sprite.Group()
#wallpaper = pg.sprite.Group()

# Подсчет жизней и очков
SCORE = 0
MAX_SCORE = 0
LIVES = 3
GAME = 0

# Функция для вывода текста
font_names = [pg.font.match_font('arial'), pg.font.match_font('kacstbook')]
def draw_text(surf, text, font_, size, x, y, color, smoothing = True):
    font = pg.font.Font(font_, size)
    text_surface = font.render(text, smoothing, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
