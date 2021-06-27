import pygame
from Pieces.piece import Piece

class King(Piece):

    def __init__(self, game, x, y, image, color):  # x et y doivent devenir Coordonnées
        super().__init__(game, x, y, image, color)

    def move(self):
        return super().move()
        
class Queen(Piece):

    def __init__(self, game, x, y, image, color):
        super().__init__(game, x, y, image, color)
        
class Rook(Piece): # Tour

    def __init__(self, game, x, y, image, color):
        super().__init__(game, x, y, image, color)

class Bishop(Piece): # Fou

    def __init__(self, game, x, y, image, color):
        super().__init__(game, x, y, image, color)

class Knight(Piece):

    def __init__(self, game, x, y, image, color):
        super().__init__(game, x, y, image, color)

class Pawn(Piece):

    def __init__(self, game, x, y, image, color):
        super().__init__(game, x, y, image, color)
