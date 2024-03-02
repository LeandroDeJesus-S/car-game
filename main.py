import random
import pygame as pg
from street import Street
from car import Car, EnemyCar

# log.basicConfig(filemode='w', filename='logs.log', format=log.BASIC_FORMAT, level=log.DEBUG)
pg.init()

            

win_size = wx, wy = (800, 600)
window = pg.display.set_mode(win_size)
fps = pg.time.Clock()

street = Street()
car = Car()
enemy_car = EnemyCar(window)

enemies_cars = pg.sprite.Group()
enemies_cars.add(enemy_car)

while True:
    fps.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
    
    keys = pg.key.get_pressed()
    
    # moving sides
    if keys[pg.K_LEFT]:
        car.move_left()
    
    elif keys[pg.K_RIGHT]:
        car.move_right()
    
    # moving up/down
    if keys[pg.K_UP]:
        car.move_up()
    
    elif keys[pg.K_DOWN]:
        car.move_down()

    car.set_car_extremes_positions(wx, wy)
    
    street.draw_street(window)
    car.draw_car(window)
    
    enemies_cars.update()

            
    
    street.movement()
    pg.display.update()
