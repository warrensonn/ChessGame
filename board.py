import pygame

class Board(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/echiquier.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def piecePlace(self, surface): 
        pass