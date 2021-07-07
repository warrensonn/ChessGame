from Pieces.piece import Piece


class King(Piece):

    def __init__(self, game, image, color, position, name):
        super().__init__(game, image, color, position, name)
        self.hasMoved = False
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

        # PETIT ET GRAND ROQUE
        if self.team == "black" and self.hasMoved == False:
            if self.game.BlackRook2.hasMoved == False:
                self.KingSideCastle(moves)
            if self.game.BlackRook1.hasMoved == False:
                self.queenSideCastle(moves)
        elif self.team == "white" and self.hasMoved == False:
            if self.game.WhiteRook2.hasMoved == False:
                self.KingSideCastle(moves)
            if self.game.WhiteRook1.hasMoved == False:
                self.queenSideCastle(moves)

        return moves



    # GRAND ROQUE
    def queenSideCastle(self, list):
        possible = True
        
        if self.team == "black":
            for piece in self.game.all_Pieces:
                if piece.position == "b8" or piece.position == "c8" or piece.position == "d8":
                    possible = False     

        else:
            for piece in self.game.all_Pieces:
                if piece.position == "b1" or piece.position == "c1" or piece.position == "d1":
                    possible = False
            
        if possible:
            list.append((self.intPosition[0]-2, self.intPosition[1]))

    # PETIT ROQUE
    def KingSideCastle(self, list):
        possible = True
        
        if self.team == "black":
            for piece in self.game.all_Pieces:
                if piece.position == "f8" or piece.position == "g8":
                    possible = False     

        else:
            for piece in self.game.all_Pieces:
                if piece.position == "f1" or piece.position == "g1":
                    possible = False
            
        if possible:
            list.append((self.intPosition[0]+2, self.intPosition[1]))

        