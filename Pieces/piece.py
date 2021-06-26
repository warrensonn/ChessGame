import pygame

class Piece(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.rect.x = x
        self.rect.y = y
        self.xmax = 0
        self.ymax = 500
        self.xmin = 0
        self.ymin = 500
        self.team = "white"

        def move(self):
            pass

        def possibleMove(self):
            pass

        def death(self):
            pass

        def eating(self, eatenPiece):
            pass

        

