import pygame


class Piece(pygame.sprite.Sprite):

    def __init__(self, game, image, color, position, name):
        super().__init__()
        self.game = game
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = game.board.position.get(position)[0]
        self.rect.y = game.board.position.get(position)[1]
        self.team = color
        self.name = name
        self.position = position
        self.intPosition = game.board.intPosition.get(position)

    def update(self):
        self.rect.x = self.game.board.position.get(self.position)[0]
        self.rect.y = self.game.board.position.get(self.position)[1]
        self.intPosition = self.game.board.intPosition.get(self.position)

    def isPossibleMove(self, area):     
        if self.game.board.intPosition.get(area) in self.possibleMoves():
            moves = []
            check = False
            memory = self.intPosition
            self.intPosition = self.game.board.intPosition.get(area)
            self.game.blackKingPosition = self.game.BlackKing.intPosition
            self.game.whiteKingPosition = self.game.WhiteKing.intPosition

            for piece in self.game.all_Pieces:
                if piece.team != self.team and piece.intPosition != self.intPosition:
                    moves.extend(piece.possibleMoves())
                    
            if self.team == "black":
                if self.game.blackKingPosition in moves:
                    check = True
            else: 
                if self.game.whiteKingPosition in moves:  
                    check = True
            
            self.intPosition = memory

            if check == False:
                return True
            
            else:
                return "Déplacement impossible, place votre roi en situation d'échec"
        
        else:
            return "Déplacement non autorisé"