import pygame

class Piece(pygame.sprite.Sprite):

    def __init__(self, game, x, y, image, color):
        super().__init__()
        self.game = game
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xmax = 0
        self.ymax = 500
        self.xmin = 0
        self.ymin = 500
        self.team = color
        # self.position = position

    def move(self):
        print("bonjour")

    def possibleMove(self):
        pass

    def death(self):
        pass

    def eating(self, eatenPiece):
        pass

        



# print(dict.get(1)[0])