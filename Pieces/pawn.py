from Pieces.piece import Piece


class WhitePawn(Piece):

    def __init__(self, game, image, color, position, name):
        super().__init__(game, image, color, position, name)
        self.game.all_Pieces.add(self)

    def possibleMoves(self):
        moves = []
        empty = True
        
        if self.intPosition[1] < 8 :
            for piece in self.game.all_Pieces:
                if piece.intPosition[0] == self.intPosition[0] and piece.intPosition[1] == self.intPosition[1]+1:
                    empty = False
            if empty == True:
                moves.append((self.intPosition[0], self.intPosition[1]+1))

        for piece in self.game.all_Pieces:          
            if (piece.intPosition[0] == self.intPosition[0]+1 or piece.intPosition[0] == self.intPosition[0]-1) and piece.intPosition[1] == self.intPosition[1]+1 and piece.team != self.team:
                moves.append((piece.intPosition[0], piece.intPosition[1]))

        empty = True
        if self.intPosition[1] == 2:
            for piece in self.game.all_Pieces:          
                if piece.intPosition[0] == self.intPosition[0] and (piece.intPosition[1] == self.intPosition[1]+2 or piece.intPosition[1] == self.intPosition[1]+1):
                    empty = False
            if empty == True:
                moves.append((self.intPosition[0], self.intPosition[1]+2))

        return moves


class BlackPawn(Piece):

    def __init__(self, game, image, color, position, name):
        super().__init__(game, image, color, position, name)
        self.game.all_Pieces.add(self)

    def possibleMoves(self):
        moves = []
        empty = True

        if self.intPosition[1] < 8 :
            for piece in self.game.all_Pieces:
                if piece.intPosition[0] == self.intPosition[0] and piece.intPosition[1] == self.intPosition[1]-1:
                    empty = False
            if empty == True:
                moves.append((self.intPosition[0], self.intPosition[1]-1))

        for piece in self.game.all_Pieces:          
            if (piece.intPosition[0] == self.intPosition[0]+1 or piece.intPosition[0] == self.intPosition[0]-1) and piece.intPosition[1] == self.intPosition[1]-1 and piece.team != self.team:
                moves.append((piece.intPosition[0], piece.intPosition[1]))

        empty = True
        if self.intPosition[1] == 7:
            for piece in self.game.all_Pieces:          
                if piece.intPosition[0] == self.intPosition[0] and (piece.intPosition[1] == self.intPosition[1]-2 or piece.intPosition[1] == self.intPosition[1]-1):
                    empty = False
            if empty == True:
                moves.append((self.intPosition[0], self.intPosition[1]-2))
        
        return moves