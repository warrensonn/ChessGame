from Pieces.piece import Piece
import pygame
from board import Board
from Pieces.king import *

class Game:
    def __init__(self):
        self.isplaying = False
        self.board = Board()
        self.all_Pieces = pygame.sprite.Group()   # ensemble des pièces
        self.turn = "white"

        # White spawn
        self.WhiteKing = King(self, 'assets/wK.png', 'white', "d1")
        self.WhiteQueen = Queen(self, 'assets/wQ.png', 'white', "e1")

        self.WhiteRook1 = Rook(self, 'assets/wR.png', 'white', "a1")
        self.WhiteRook2 = Rook(self, 'assets/wR.png', 'white', "h1")
        
        self.WhiteBishop1 = Bishop(self, 'assets/wB.png', 'white', "c1")
        self.WhiteBishop2 = Bishop(self, 'assets/wB.png', 'white', "f1")

        self.WhiteKnight1 = Knight(self, 'assets/wN.png', 'white', "b1")
        self.WhiteKnight2 = Knight(self, 'assets/WN.png', 'white', "g1")

        self.WhitePawn1 = Pawn(self, 'assets/wp.png', 'white', "a2")
        self.WhitePawn2 = Pawn(self, 'assets/wp.png', 'white', "b2")
        self.WhitePawn3 = Pawn(self, 'assets/wp.png', 'white', "c4")
        self.WhitePawn4 = Pawn(self, 'assets/wp.png', 'white', "d2")
        self.WhitePawn5 = Pawn(self, 'assets/wp.png', 'white', "e2")
        self.WhitePawn6 = Pawn(self, 'assets/wp.png', 'white', "f2")
        self.WhitePawn7 = Pawn(self, 'assets/wp.png', 'white', "g2")
        self.WhitePawn8 = Pawn(self, 'assets/wp.png', 'white', "h2")

        # black spawn
        self.BlackKing = King(self, 'assets/bK.png', 'black', "e8")
        self.BlackQueen = Queen(self, 'assets/bQ.png', 'black', "d8")

        self.BlackRook1 = Rook(self, 'assets/bR.png', 'black', "a8")
        self.BlackRook2 = Rook(self, 'assets/bR.png', 'black', "h8")

        self.BlackBishop1 = Bishop(self, 'assets/bB.png', 'black', "b8")
        self.BlackBishop2 = Bishop(self, 'assets/bB.png', 'black', "g8")

        self.BlackKnight1 = Knight(self, 'assets/bR.png', 'black', "c8")
        self.BlackKnight2 = Knight(self, 'assets/bR.png', 'black', "f8")

        self.BlackPawn1 = Pawn(self, 'assets/bp.png', 'black', "a7")
        self.BlackPawn2 = Pawn(self, 'assets/bp.png', 'black', "b7")
        self.BlackPawn3 = Pawn(self, 'assets/bp.png', 'black', "c7")
        self.BlackPawn4 = Pawn(self, 'assets/bp.png', 'black', "d7")
        self.BlackPawn5 = Pawn(self, 'assets/bp.png', 'black', "e7")
        self.BlackPawn6 = Pawn(self, 'assets/bp.png', 'black', "f7")
        self.BlackPawn7 = Pawn(self, 'assets/bp.png', 'black', "g7")
        self.BlackPawn8 = Pawn(self, 'assets/bp.png', 'black', "h7")
        
    
    def update(self, screen):

        screen.blit(self.board.image, (200, 10))    # appliquer l'image de mon joueur
        # self.piece.draw(screen)
        
        # for piece in self.all_Pieces:
        #     piece.draw(screen)
        self.all_Pieces.draw(screen)


    # def spawnPiece(self, x, y, image, color):
    #     piece = Piece(self, x, y, image, color)
    #     self.all_Pieces.add(piece)

    def spawnKing(self, image, color, position):
        king = King(self, image, color, position)
        self.all_Pieces.add(king)

    def spawnQueen(self, image, color, position):
        queen = Queen(self, image, color, position)
        self.all_Pieces.add(queen)

    def spawnRook(self, image, color, position):
        rook = Rook(self, image, color, position)
        self.all_Pieces.add(rook)

    def spawnBishop(self, image, color, position):
        bishop = Bishop(self, image, color, position)
        self.all_Pieces.add(bishop)
    
    def spawnKnight(self, image, color, position):
        knight = Knight(self, image, color, position)
        self.all_Pieces.add(knight)
    
    def spawnPawn(self, image, color, position):
        pawn = Pawn(self, image, color, position)
        self.all_Pieces.add(pawn)
