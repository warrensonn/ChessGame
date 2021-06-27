from Pieces.piece import Piece
import pygame
from board import Board
from Pieces.king import King

class Game:
    def __init__(self):
        self.isplaying = False
        self.board = Board()
        self.all_Pieces = pygame.sprite.Group()   # groupe de monstres

        self.position = {1 : (200, 50), 2 : (400, 300)}

        self.spawnKing(self.position.get(1)[0], self.position.get(1)[1], 'assets/wK.png', 'white')
        self.spawnKing(self.position.get(2)[0], self.position.get(2)[1], 'assets/bK.png', 'black')

    
    def update(self, screen):

        screen.blit(self.board.image, (200, 10))    # appliquer l'image de mon joueur
        # self.piece.draw(screen)
        
        # for piece in self.all_Pieces:
        #     piece.draw(screen)
        self.all_Pieces.draw(screen)


    # def spawnPiece(self, x, y, image, color):
    #     piece = Piece(self, x, y, image, color)
    #     self.all_Pieces.add(piece)

    def spawnKing(self, x, y, image, color):
        king = King(self, x, y, image, color)
        self.all_Pieces.add(king)