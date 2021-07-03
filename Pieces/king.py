from Pieces.piece import Piece


class King(Piece):

    def __init__(self, game, image, color, position, name):
        super().__init__(game, image, color, position, name)
        self.game.all_Pieces.add(self)

    def possibleMoves(self):
        moves = []
        empty = True
        
        # LES 3 DEPLACEMENTS VERS LE HAUT 
        if self.intPosition[1] < 8: 
            for piece in self.game.all_Pieces:
                if piece.intPosition[0] == self.intPosition[0] and piece.intPosition[1] == self.intPosition[1]+1 and piece.team == self.team:
                    empty = False
            if empty == True:
                moves.append((self.intPosition[0], self.intPosition[1]+1))

        empty= True
        if self.intPosition[1] < 8 and self.intPosition[0] > 1:
            for piece in self.game.all_Pieces:
                if piece.intPosition[0] == self.intPosition[0]-1 and piece.intPosition[1] == self.intPosition[1]+1 and piece.team == self.team:
                    empty = False
            if empty == True:
                moves.append((self.intPosition[0]-1, self.intPosition[1]+1))

        empty= True
        if self.intPosition[1] < 8 and self.intPosition[0] < 8:
            for piece in self.game.all_Pieces:
                if piece.intPosition[0] == self.intPosition[0]+1 and piece.intPosition[1] == self.intPosition[1]+1 and piece.team == self.team:
                    empty = False
            if empty == True:
                moves.append((self.intPosition[0]+1, self.intPosition[1]+1))


        # LES 3 DEPLACEMENTS VERS LE BAS 
        empty= True
        if self.intPosition[1] > 1 and self.intPosition[0] < 8:
            for piece in self.game.all_Pieces:
                if piece.intPosition[0] == self.intPosition[0]+1 and piece.intPosition[1] == self.intPosition[1]-1 and piece.team == self.team:
                    empty = False
            if empty == True:
                moves.append((self.intPosition[0]+1, self.intPosition[1]-1))

        empty= True
        if self.intPosition[1] > 1 and self.intPosition[0] > 1:
            for piece in self.game.all_Pieces:
                if piece.intPosition[0] == self.intPosition[0]-1 and piece.intPosition[1] == self.intPosition[1]-1 and piece.team == self.team:
                    empty = False
            if empty == True:
                moves.append((self.intPosition[0]-1, self.intPosition[1]-1))

        empty= True
        if self.intPosition[1] > 1:
            for piece in self.game.all_Pieces:
                if piece.intPosition[0] == self.intPosition[0] and piece.intPosition[1] == self.intPosition[1]-1 and piece.team == self.team:
                    empty = False
            if empty == True:
                moves.append((self.intPosition[0], self.intPosition[1]-1))


        # LES 2 DEPLACEMENTS GAUCHE ET DROITE 
        empty= True
        if self.intPosition[0] > 1:
            for piece in self.game.all_Pieces:
                if piece.intPosition[0] == self.intPosition[0]-1 and piece.intPosition[1] == self.intPosition[1] and piece.team == self.team:
                    empty = False
            if empty == True:
                moves.append((self.intPosition[0]-1, self.intPosition[1]))

        empty= True
        if self.intPosition[0] < 8:
            for piece in self.game.all_Pieces:
                if piece.intPosition[0] == self.intPosition[0]+1 and piece.intPosition[1] == self.intPosition[1] and piece.team == self.team:
                    empty = False
            if empty == True:
                moves.append((self.intPosition[0]+1, self.intPosition[1]))

        return moves