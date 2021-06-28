import pygame

class Piece(pygame.sprite.Sprite):

    def __init__(self, game, image, color, position):
        super().__init__()
        self.game = game
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = game.board.position.get(position)[0]
        self.rect.y = game.board.position.get(position)[1]
        self.team = color
        self.position = position

    def move(self):
        print("bonjour")

    def possibleMove(self):
        pass

    def death(self):
        pass

    def eating(self, eatenPiece):
        pass

        



# print(dict.get(1)[0])