import pygame
from Pieces.piece import Piece


class Bishop(Piece): # Fou

    def __init__(self, game, image, color, position, name):
        super().__init__(game, image, color, position, name)
        self.game.all_Pieces.add(self)

    def possibleMoves(self):
        moves = []
        empty = True
        n = self.intPosition[0]+1
        q = self.intPosition[1]+1

        while empty == True and n < 9 and q < 9:  # Ajoute à moves les déplacements possibles vers la gauche
            for piece in self.game.all_Pieces:
                if piece.intPosition[0] == n and piece.intPosition[1] == q:
                    empty = False
                    if piece.team != self.team:
                        moves.append(piece.intPosition)
            if empty == True:
                moves.append((n, q))
            n+=1
            q+=1

        empty = True
        n = self.intPosition[0]+1
        q = self.intPosition[1]-1

        while empty == True and n < 9 and q > 0:  # Ajoute à moves les déplacements possibles vers la gauche
            for piece in self.game.all_Pieces:
                if piece.intPosition[0] == n and piece.intPosition[1] == q:
                    empty = False
                    if piece.team != self.team:
                        moves.append(piece.intPosition)
            if empty == True:
                moves.append((n, q))
            n+=1
            q-=1

        empty = True
        n = self.intPosition[0]-1
        q = self.intPosition[1]-1

        while empty == True and n > 0 and q > 0:  # Ajoute à moves les déplacements possibles vers la gauche
            for piece in self.game.all_Pieces:
                if piece.intPosition[0] == n and piece.intPosition[1] == q:
                    empty = False
                    if piece.team != self.team:
                        moves.append(piece.intPosition)
            if empty == True:
                moves.append((n, q))
            n-=1
            q-=1

        empty = True
        n = self.intPosition[0]-1
        q = self.intPosition[1]+1

        while empty == True and n > 0 and q < 9:  # Ajoute à moves les déplacements possibles vers la gauche
            for piece in self.game.all_Pieces:
                if piece.intPosition[0] == n and piece.intPosition[1] == q:
                    empty = False
                    if piece.team != self.team:
                        moves.append(piece.intPosition)
            if empty == True:
                moves.append((n, q))
            n-=1
            q+=1
        
        return moves


# memory = self.intPosition

#         while empty == True and n < 9 and q < 9:  # Ajoute à moves les déplacements possibles vers la gauche
#             for piece in self.game.all_Pieces:
#                 if piece.intPosition[0] == n and piece.intPosition[1] == q:
#                     empty = False
#                     self.intPosition = piece.intPosition
#                     if piece.team != self.team:
#                         for piece1 in self.game.all_Pieces:
#                             if piece1.team != self.team:
#                                 possible.extend(piece1.possibleMoves())
#                         if self.team == "black":
#                             if self.game.blackKingPosition not in possible:
#                                 moves.append(piece.intPosition)
#                         else:
#                             if self.game.whiteKingPosition not in possible:
#                                 moves.append(piece.intPosition)
#                     self.intPosition = memory
                    
#             if empty == True:
#                 moves.append((n, q))
#             n+=1
#             q+=1