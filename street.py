import pygame


class Street:
    IMG1 = pygame.image.load('imgs/street.png')
    HEIGHT = IMG1.get_height()
    SPEED = 5
    def __init__(self) -> None:
        self.street1_y = 0
        self.street2_y = self.street1_y - self.HEIGHT
        self.x = 0
        
    def movement(self):
        self.street1_y += self.SPEED
        self.street2_y += self.SPEED
        
        if self.street1_y > self.HEIGHT:
            self.street1_y = self.street2_y - self.HEIGHT
            
        if self.street2_y > self.HEIGHT:
            self.street2_y = self.street1_y - self.HEIGHT


    def draw_street(self, screen):
        screen.blit(self.IMG1, (self.x, self.street1_y))
        screen.blit(self.IMG1, (self.x, self.street2_y))
        
