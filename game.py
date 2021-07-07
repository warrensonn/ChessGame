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
        self.dead_Pieces = pygame.sprite.Group()
        self.turn = "white"
        self.selectedBox = False
        self.possibleMoves = []
        self.launchGame()
        self.blackKingPosition = self.BlackKing.intPosition
        self.whiteKingPosition = self.WhiteKing.intPosition


        
    def update(self, screen):
        screen.blit(self.board.image, (200, 10))
        
        self.blackKingPosition = self.BlackKing.intPosition
        self.whiteKingPosition = self.WhiteKing.intPosition
        if self.checkWhiteKing():
            pygame.draw.rect(screen, pygame.Color(255, 0, 0), (self.WhiteKing.rect.x-6, self.WhiteKing.rect.y-7, 76, 75))
        
        if self.checkBlackKing():
            pygame.draw.rect(screen, pygame.Color(255, 0, 0), (self.BlackKing.rect.x-5, self.BlackKing.rect.y-5, 76, 75))
     
        if self.selectedBox != False:      # Si une pièce est sélectionnée, sa case est en surbrillance et les cases de déplacements possibles aussi
            pygame.draw.rect(screen, pygame.Color(227, 173, 11), (self.board.areas.get(self.selectedBox.position)[0][0], self.board.areas.get(self.selectedBox.position)[1][0], 76, 76))
            for move in self.possibleMoves:
                
                if self.selectedBox.isPossibleMove(self.board.intPositionRevert.get(move)) == True:  # parametre de type zone comme A1 A2 etc, ici move == intPosition
                    xs = self.board.areas[list(self.board.intPosition.keys())[list(self.board.intPosition.values()).index(move)]][0][0]
                    ys = self.board.areas[list(self.board.intPosition.keys())[list(self.board.intPosition.values()).index(move)]][1][0]
                    pygame.draw.rect(screen, pygame.Color(0, 173, 11), (xs, ys, 76, 76))
        
        self.all_Pieces.draw(screen)

        for piece in self.all_Pieces:   # Met à jour la position des pièces
            piece.update()
        
        self.eating()

        for piece in self.dead_Pieces:
            screen.blit(piece.image, (piece.rect.x, piece.rect.y))


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


    def eating(self): 
        for piece in self.all_Pieces:
            for piece1 in self.all_Pieces:
                if piece.position == piece1.position and piece.name != piece1.name:
                    if self.turn != piece.team:
                        self.dead(piece1)
                    else:
                        self.dead(piece)
                        
    def dead(self, piece):
        self.all_Pieces.remove(piece)
        self.dead_Pieces.add(piece)
        if piece.team == "white":
            if len([x for x in self.dead_Pieces if x.team == "white"]) < 9:
                piece.rect.x = 50
                piece.rect.y = 30 + (len([x for x in self.dead_Pieces if x.team == "white"]) *50)
            else:
                piece.rect.x = 100
                piece.rect.y = 30 + ((len([x for x in self.dead_Pieces if x.team == "white"])-8) *50)

        else:  
            if len([x for x in self.dead_Pieces if x.team == "black"]) < 9:
                piece.rect.x = 930
                piece.rect.y = 30 + (len([x for x in self.dead_Pieces if x.team == "black"]) *50)
            else:
                piece.rect.x = 980
                piece.rect.y = 30 + ((len([x for x in self.dead_Pieces if x.team == "black"])-8) *50)


    def moving(self, selectedArea):
        if self.turn == "black":
                self.turn = "white"
        else:
            self.turn = "black"
                
        if isinstance(self.selectedBox, Rook) or isinstance(self.selectedBox, King):
            self.selectedBox.hasMoved = True
            # if self.selectedBox.team == "black" and type(self.selectedBox) == King and self.selectedBox.intPosition[0] == self.board.intPosition.get(selectedArea)[0]-2:
            #     self.BlackRook2.position = "c8"
            # elif self.selectedBox.team == "black" and type(self.selectedBox) == King and self.selectedBox.intPosition[0] == self.board.intPosition.get(selectedArea)[0]+2:
            #     self.BlackRook2.position = "f8"
            # elif self.selectedBox.team == "white" and type(self.selectedBox) == King and self.selectedBox.intPosition[0] == self.board.intPosition.get(selectedArea)[0]-2:
            #     self.WhiteRook2.position = "c1"
            # elif self.selectedBox.team == "white" and type(self.selectedBox) == King and self.selectedBox.intPosition[0] == self.board.intPosition.get(selectedArea)[0]+2:
            #     self.WhiteRook2.position = "f1"

            if type(self.selectedBox) == King and self.selectedBox.intPosition[0] == self.board.intPosition.get(selectedArea)[0]+2:
                if self.selectedBox.team == "black":
                    self.BlackRook1.position = "d8"
                else:
                    self.WhiteRook1.position = "d1"

            if type(self.selectedBox) == King and self.selectedBox.intPosition[0] == self.board.intPosition.get(selectedArea)[0]-2:
                if self.selectedBox.team == "black":
                    self.BlackRook2.position = "f8"
                else:
                    self.WhiteRook2.position = "f1"

        self.selectedBox.position = selectedArea
        self.selectedBox = False 


    def launchGame(self):
        # White spawn
        self.WhiteKing = King(self, 'assets/wK.png', 'white', "e1", "King1")
        self.WhiteQueen = Queen(self, 'assets/wQ.png', 'white', "d1", "Queen1")

        self.WhiteRook1 = Rook(self, 'assets/wR.png', 'white', "a1", "Rook1")
        self.WhiteRook2 = Rook(self, 'assets/wR.png', 'white', "h1", "Rook2")
        
        self.WhiteBishop1 = Bishop(self, 'assets/wB.png', 'white', "c1", "Bishop1")
        self.WhiteBishop2 = Bishop(self, 'assets/wB.png', 'white', "f1", "Bishop2")

        self.WhiteKnight1 = Knight(self, 'assets/wN.png', 'white', "b1", "Knight1")
        self.WhiteKnight2 = Knight(self, 'assets/wN.png', 'white', "g1", "Knight2")

        self.WhitePawn1 = WhitePawn(self, 'assets/wp.png', 'white', "a2", "Pawn1")
        self.WhitePawn2 = WhitePawn(self, 'assets/wp.png', 'white', "b2", "Pawn2")
        self.WhitePawn3 = WhitePawn(self, 'assets/wp.png', 'white', "c2", "Pawn3")
        self.WhitePawn4 = WhitePawn(self, 'assets/wp.png', 'white', "d2", "Pawn4")
        self.WhitePawn5 = WhitePawn(self, 'assets/wp.png', 'white', "e2", "Pawn5")
        self.WhitePawn6 = WhitePawn(self, 'assets/wp.png', 'white', "f2", "Pawn6")
        self.WhitePawn7 = WhitePawn(self, 'assets/wp.png', 'white', "g2", "Pawn7")
        self.WhitePawn8 = WhitePawn(self, 'assets/wp.png', 'white', "h2", "Pawn8")

        # black spawn
        self.BlackKing = King(self, 'assets/bK.png', 'black', "e8", "King2")
        self.BlackQueen = Queen(self, 'assets/bQ.png', 'black', "d8", "Queen2")

        self.BlackRook1 = Rook(self, 'assets/bR.png', 'black', "a8", "Rook3")
        self.BlackRook2 = Rook(self, 'assets/bR.png', 'black', "h8", "Rook4")

        self.BlackBishop1 = Bishop(self, 'assets/bB.png', 'black', "c8", "Bishop3")
        self.BlackBishop2 = Bishop(self, 'assets/bB.png', 'black', "f8", "Bishop4")

        self.BlackKnight1 = Knight(self, 'assets/bN.png', 'black', "b8", "Knight3")
        self.BlackKnight2 = Knight(self, 'assets/bN.png', 'black', "g8", "Knight4")

        self.BlackPawn1 = BlackPawn(self, 'assets/bp.png', 'black', "a7", "Pawn9")
        self.BlackPawn2 = BlackPawn(self, 'assets/bp.png', 'black', "b7", "Pawn10")
        self.BlackPawn3 = BlackPawn(self, 'assets/bp.png', 'black', "c7", "Pawn11")
        self.BlackPawn4 = BlackPawn(self, 'assets/bp.png', 'black', "d7", "Pawn12")
        self.BlackPawn5 = BlackPawn(self, 'assets/bp.png', 'black', "e7", "Pawn13")
        self.BlackPawn6 = BlackPawn(self, 'assets/bp.png', 'black', "f7", "Pawn14")
        self.BlackPawn7 = BlackPawn(self, 'assets/bp.png', 'black', "g7", "Pawn15")
        self.BlackPawn8 = BlackPawn(self, 'assets/bp.png', 'black', "h7", "Pawn16")