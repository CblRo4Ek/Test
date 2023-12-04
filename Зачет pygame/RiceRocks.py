from Specifications import *

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and GAME > 1:
                # ship.shoot()
                rocket = Rocket(rocket_image, ship.rect.center, ship.corner)
                all_sprites.add(rocket)
                rockets.add(rocket)
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1 and GAME < 2:
            GAME = 2
            for asteroid in asteroids:
                asteroid.kill()
                all_sprites.remove(asteroid)
                asteroids.remove(asteroid)


    if GAME < 2:  # Если заставка
        if GAME == 0:
            # Создание астероидов
            for asteroid in range(10):
                Asteroid_ = Asteroid(0, asteroid_image, asteroid_transparent_image, [WIDTH, HEIGHT])
                all_sprites.add(Asteroid_)
                asteroids.add(Asteroid_)
                GAME = 1
        screen.blit(sky_image, sky)
        draw_text(screen, 'RiceRocks', None, 70, WIDTH / 2, HEIGHT / 2 - 60, (255, 255, 0))
        draw_text(screen, 'Click to start', None, 24, WIDTH / 2, HEIGHT / 2, (255, 255, 255))
        all_sprites.update()
        all_sprites.draw(screen)
        draw_text(screen, 'LIVES: ' + str(LIVES), font_names[0], 22, 75, 10, (0, 255, 0))
        draw_text(screen, 'SCORE: ' + str(SCORE), font_names[0], 22, 750, 10, (0, 255, 0))
        draw_text(screen, '(MAX: ' + str(MAX_SCORE) + ')', font_names[0], 22, 850, 10, (255, 255, 0))

    else:
        if GAME == 2:
            LIVES = 3
            SCORE = 0

            # Размещение корабля
            ship = Player(0, 0, ship_image, ship_with_fire_image, [WIDTH, HEIGHT])
            all_sprites.add(ship)

            # Создание астероидов
            for asteroid in range(10):
                Asteroid_ = Asteroid(1, asteroid_image, asteroid_transparent_image, [WIDTH, HEIGHT])
                all_sprites.add(Asteroid_)
                asteroids.add(Asteroid_)
                GAME = 3
        # Проверка на столкновение метеорита и ракеты
        for rocket in rockets:
            for asteroid in asteroids:
                #if pg.sprite.collide_circle(rocket, asteroid):
                if pg.sprite.collide_circle(rocket, asteroid):
                    rocket.kill()

                    # Создание взрыва
                    Explosion_ = Explosion(explosion_image, asteroid.size, asteroid.rect.center)
                    all_sprites.add(Explosion_)

                    # Удаление астероида и ракеты
                    all_sprites.remove(rocket)
                    rockets.remove(rocket)
                    asteroid.kill()
                    all_sprites.remove(asteroid)
                    asteroids.remove(asteroid)

                    # Увеличение очков и создание нового астероида
                    SCORE += 1
                    MAX_SCORE = max(SCORE, MAX_SCORE)

                    Asteroid_ = Asteroid(1, asteroid_image, asteroid_transparent_image, [WIDTH, HEIGHT])
                    all_sprites.add(Asteroid_)
                    asteroids.add(Asteroid_)

        # Проверка на столкновение метеорита и корабля
        for asteroid in asteroids:
            if pg.sprite.collide_circle(ship, asteroid):

                # Создание взрыва
                Explosion_ = Explosion(explosion_image, asteroid.size, asteroid.rect.center)
                all_sprites.add(Explosion_)

                # Удаление астероида
                asteroid.kill()
                all_sprites.remove(asteroid)
                asteroids.remove(asteroid)

                # Проверка жизней и перемещение корабля в середину экрана
                LIVES -= 1
                if LIVES > 0:
                    ship.rect.center = (WIDTH / 2, HEIGHT / 2)
                    Asteroid_ = Asteroid(1, asteroid_image, asteroid_transparent_image, [WIDTH, HEIGHT])
                    all_sprites.add(Asteroid_)
                    asteroids.add(Asteroid_)
                else:
                    GAME = 0
                    ship.kill()
                    for asteroid in asteroids:
                        asteroid.kill()
                        all_sprites.remove(asteroid)
                        asteroids.remove(asteroid)
                    for rocket in rockets:
                        rocket.kill()
                        all_sprites.remove(rocket)
                        asteroids.remove(rocket)


    #  Обновляем данные и отрисовываем их
    all_sprites.update()
    if GAME > 1:
        screen.blit(sky_image, sky)
    all_sprites.draw(screen)
    draw_text(screen, 'LIVES: ' + str(LIVES), font_names[0], 22, 75, 10, (0, 255, 0))
    draw_text(screen, 'SCORE: ' + str(SCORE), font_names[0], 22, 750, 10, (0, 255, 0))
    draw_text(screen, '(MAX: ' + str(MAX_SCORE) + ')', font_names[0], 22, 850, 10, (255, 255, 0))
    pg.display.flip()