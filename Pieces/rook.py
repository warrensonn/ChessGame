from Pieces.piece import Piece


class Rook(Piece): # Tour

    def __init__(self, game, image, color, position, name):
        super().__init__(game, image, color, position, name)
        self.hasMoved = False
        self.game.all_Pieces.add(self)

    def possibleMoves(self):
        moves = []
        empty= True
        # Pour ordonnées
        i = self.intPosition[1]+1
        k = self.intPosition[1]-1
        # Pour abscisses
        q = self.intPosition[0]+1
        n = self.intPosition[0]-1

        while empty == True and i < 9:  # Ajoute à moves les déplacements possibles vers le haut
            for piece in self.game.all_Pieces:
                if piece.intPosition[0] == self.intPosition[0] and piece.intPosition[1] == i:
                    empty = False
                    if piece.team != self.team:
                        moves.append(piece.intPosition)
            if empty == True:
                moves.append((self.intPosition[0], i))
            i+=1

        empty = True
        while empty == True and k > 0:  # Ajoute à moves les déplacements possibles vers le bas
            for piece in self.game.all_Pieces:
                if piece.intPosition[0] == self.intPosition[0] and piece.intPosition[1] == k:
                    empty = False
                    if piece.team != self.team:
                        moves.append(piece.intPosition)
            if empty == True:
                moves.append((self.intPosition[0], k))
            k-=1

        empty = True
        while empty == True and n > 0:  # Ajoute à moves les déplacements possibles vers la gauche
            for piece in self.game.all_Pieces:
                if piece.intPosition[1] == self.intPosition[1] and piece.intPosition[0] == n:
                    empty = False
                    if piece.team != self.team:
                        moves.append(piece.intPosition)
            if empty == True:
                moves.append((n, self.intPosition[1]))
            n-=1

        empty = True
        while empty == True and q < 9:  # Ajoute à moves les déplacements possibles vers la droite
            for piece in self.game.all_Pieces:
                if piece.intPosition[1] == self.intPosition[1] and piece.intPosition[0] == q:
                    empty = False
                    if piece.team != self.team:
                        moves.append(piece.intPosition)
            if empty == True:
                moves.append((q, self.intPosition[1]))
            q+=1
               
        return moves