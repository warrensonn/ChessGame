import pygame
from board import Board

class Game:
    def __init__(self):
        self.isplaying = False
        self.board = Board()


    
    def update(self, screen):
        screen.blit(self.board.image, (200, 10))    # appliquer l'image de mon joueur
        self.board.piecePlace(screen)
        