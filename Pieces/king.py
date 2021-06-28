import pygame
from Pieces.piece import Piece

class King(Piece):

    def __init__(self, game, image, color, position):  # x et y doivent devenir Coordonnées
        super().__init__(game, image, color, position)
        self.game.all_Pieces.add(self)

    def move(self):
        return super().move()
        
class Queen(Piece):

    def __init__(self, game, image, color, position):
        super().__init__(game, image, color, position)
        self.game.all_Pieces.add(self)
        
class Rook(Piece): # Tour

    def __init__(self, game, image, color, position):
        super().__init__(game, image, color, position)
        self.game.all_Pieces.add(self)

class Bishop(Piece): # Fou

    def __init__(self, game, image, color, position):
        super().__init__(game, image, color, position)
        self.game.all_Pieces.add(self)

class Knight(Piece):

    def __init__(self, game, image, color, position):
        super().__init__(game, image, color, position)
        self.game.all_Pieces.add(self)

class Pawn(Piece):

    def __init__(self, game, image, color, position):
        super().__init__(game, image, color, position)
        self.game.all_Pieces.add(self)
