import random
import pygame


class Car:
    def __init__(self):
        self.rotation = -90
        self.img_path = 'imgs/maincar.png'
        self.SPEED = 5
        self.IMAGE = self.adjusted_image()
        self.WIDTH = self.IMAGE.get_width()
        self.HEIGHT = self.IMAGE.get_height()
        self.x = 450
        self.y = 500
        self.car_rect = self.IMAGE.get_rect()
    
    def adjusted_image(self):
        img_rotated = pygame.transform.rotate(
            (pygame.image.load(self.img_path)), self.rotation
        )
        
        div = 3
        new_size = (img_rotated.get_width() / div, 
                    img_rotated.get_height() / div)
        
        return pygame.transform.scale(img_rotated, new_size)
    
    def draw_car(self, window):
        window.blit(self.IMAGE, (self.x, self.y))
    
    def move_right(self):
        self.x += self.SPEED
    
    def move_left(self):
        self.x -= self.SPEED
    
    def move_up(self):
        self.y -= self.SPEED
    
    def move_down(self):
        self.y += self.SPEED
    
    def set_car_extremes_positions(self, x, y):
        max_y_pos = 0
        min_y_pos = y - 60
        if self.y <= max_y_pos:
            self.y = max_y_pos
        
        if self.y >= min_y_pos:
            self.y = min_y_pos
        
        min_x_pos = 165
        max_x_pos = x - min_x_pos
        if self.x <= min_x_pos:
            self.x = min_x_pos
        
        if self.x >= max_x_pos:
            self.x = max_x_pos


class EnemyCar:
    def __init__(self, surface) -> None:
        self.surface = surface
        self.img_path = 'imgs/enemy_car.png'
        self.image = pygame.image.load(self.img_path)
        self.adjusted_img = self.adjust_img_size()
        self.car_rect = self.image.get_rect()
        self.spawn_positions = (
            450, 550, 350, 200
        )
        self.x = random.choice(self.spawn_positions)
        self.y = 0 - self.adjusted_img.get_height()
        self.cars = [self.adjusted_img, self.adjusted_img,]
        self.SPEED = 5
        
    def adjust_img_size(self):
        div = 3
        new_size = (self.image.get_width() / div, 
                    self.image.get_height() / div)
        
        return pygame.transform.scale(self.image, new_size)
    
    def draw_car(self):
        self.surface.blits(self.cars)
            
    def move(self):
        self.y += self.SPEED
        
    
    def spawn(self):
        ...
    
    
            
        