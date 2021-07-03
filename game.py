from Pieces.piece import Piece
import pygame
from board import Board
from Pieces.king import *
from Pieces.queen import *
from Pieces.rook import *
from Pieces.bishop import *
from Pieces.knight import *
from Pieces.pawn import *


class Game:
    def __init__(self):
        self.isplaying = False
        self.board = Board()
        self.all_Pieces = pygame.sprite.Group()   # ensemble des pièces
        self.turn = "white"
        self.selectedBox = False
        self.possibleMoves = []
        self.launchGame()
        self.blackKingPosition = self.BlackKing.intPosition
        self.whiteKingPosition = self.WhiteKing.intPosition

    def die(self, piece):
        self.all_Pieces.remove(piece)

        
    def update(self, screen):
        screen.blit(self.board.image, (200, 10))
        
        self.blackKingPosition = self.BlackKing.intPosition
        self.whiteKingPosition = self.WhiteKing.intPosition
        if self.checkWhiteKing():
            pygame.draw.rect(screen, pygame.Color(255, 0, 0), (self.WhiteKing.rect.x-6, self.WhiteKing.rect.y-7, 76, 75))
        
        if self.checkBlackKing():
            pygame.draw.rect(screen, pygame.Color(255, 0, 0), (self.BlackKing.rect.x-5, self.BlackKing.rect.y-5, 76, 75))
     
        if self.selectedBox != False:      # Si une pièce est sélectionnée, sa case est en surbrillance et les cases de déplacements possibles aussi
            pygame.draw.rect(screen, pygame.Color(227, 173, 11), (self.selectedBox.rect.x - 7, self.selectedBox.rect.y - 7, 76, 75))
            for move in self.possibleMoves:
                # if self.selectedBox.
                xs = self.board.areas[list(self.board.intPosition.keys())[list(self.board.intPosition.values()).index(move)]][0][0]
                ys = self.board.areas[list(self.board.intPosition.keys())[list(self.board.intPosition.values()).index(move)]][1][0]
                pygame.draw.rect(screen, pygame.Color(0, 173, 11), (xs, ys, 76, 75))
        
        self.all_Pieces.draw(screen)

        for piece in self.all_Pieces:   # Met à jour la position des pièces
            piece.update()

        
        

    def checkWhiteKing(self):
        check = False
        for piece in self.all_Pieces:
            if piece.team == "black":
                if self.whiteKingPosition in piece.possibleMoves():
                    check = True
        return check
    
    def checkBlackKing(self):
        check = False
        for piece in self.all_Pieces:
            if piece.team == "white":
                if self.blackKingPosition in piece.possibleMoves():
                    check = True
        return check


    def launchGame(self):
        # White spawn
        self.WhiteKing = King(self, 'assets/wK.png', 'white', "d1", "King")
        self.WhiteQueen = Queen(self, 'assets/wQ.png', 'white', "e1", "Queen")

        self.WhiteRook1 = Rook(self, 'assets/wR.png', 'white', "a1", "Rook")
        self.WhiteRook2 = Rook(self, 'assets/wR.png', 'white', "h1", "Rook")
        
        self.WhiteBishop1 = Bishop(self, 'assets/wB.png', 'white', "c1", "Bishop")
        self.WhiteBishop2 = Bishop(self, 'assets/wB.png', 'white', "f1", "Bishop")

        self.WhiteKnight1 = Knight(self, 'assets/wN.png', 'white', "b1", "Knight")
        self.WhiteKnight2 = Knight(self, 'assets/wN.png', 'white', "g1", "Knight")

        self.WhitePawn1 = WhitePawn(self, 'assets/wp.png', 'white', "a2", "Pawn")
        self.WhitePawn2 = WhitePawn(self, 'assets/wp.png', 'white', "b2", "Pawn")
        self.WhitePawn3 = WhitePawn(self, 'assets/wp.png', 'white', "c2", "Pawn")
        self.WhitePawn4 = WhitePawn(self, 'assets/wp.png', 'white', "d2", "Pawn")
        self.WhitePawn5 = WhitePawn(self, 'assets/wp.png', 'white', "e2", "Pawn")
        self.WhitePawn6 = WhitePawn(self, 'assets/wp.png', 'white', "f2", "Pawn")
        self.WhitePawn7 = WhitePawn(self, 'assets/wp.png', 'white', "g2", "Pawn")
        self.WhitePawn8 = WhitePawn(self, 'assets/wp.png', 'white', "h2", "Pawn")

        # black spawn
        self.BlackKing = King(self, 'assets/bK.png', 'black', "e8", "King")
        self.BlackQueen = Queen(self, 'assets/bQ.png', 'black', "d8", "Queen")

        self.BlackRook1 = Rook(self, 'assets/bR.png', 'black', "a8", "Rook")
        self.BlackRook2 = Rook(self, 'assets/bR.png', 'black', "h8", "Rook")

        self.BlackBishop1 = Bishop(self, 'assets/bB.png', 'black', "c8", "Bishop")
        self.BlackBishop2 = Bishop(self, 'assets/bB.png', 'black', "f8", "Bishop")

        self.BlackKnight1 = Knight(self, 'assets/bN.png', 'black', "b8", "Knight")
        self.BlackKnight2 = Knight(self, 'assets/bN.png', 'black', "g8", "Knight")

        self.BlackPawn1 = BlackPawn(self, 'assets/bp.png', 'black', "a7", "Pawn")
        self.BlackPawn2 = BlackPawn(self, 'assets/bp.png', 'black', "b7", "Pawn")
        self.BlackPawn3 = BlackPawn(self, 'assets/bp.png', 'black', "c7", "Pawn")
        self.BlackPawn4 = BlackPawn(self, 'assets/bp.png', 'black', "d7", "Pawn")
        self.BlackPawn5 = BlackPawn(self, 'assets/bp.png', 'black', "e7", "Pawn")
        self.BlackPawn6 = BlackPawn(self, 'assets/bp.png', 'black', "f7", "Pawn")
        self.BlackPawn7 = BlackPawn(self, 'assets/bp.png', 'black', "g7", "Pawn")
        self.BlackPawn8 = BlackPawn(self, 'assets/bp.png', 'black', "h7", "Pawn")