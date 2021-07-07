from Pieces.king import King
from Pieces.rook import Rook
from game import Game
import pygame
from Pieces.piece import Piece

pygame.init()
game = Game()


pygame.display.set_caption('Bevilacqua Warren Chess Game v1.0')
screen = pygame.display.set_mode((1080, 720))

BLUE = pygame.Color(10,10,100)

running = True

while running: 
    
    screen.fill(BLUE)   # on injecte l'image sur l'écran  

    game.update(screen)
    
    pygame.display.flip() 

    for event in pygame.event.get(): 

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()


        elif event.type == pygame.MOUSEBUTTONUP:
            if isinstance(game.selectedBox, Piece): # Si une pièce est selectionnée

                for area in game.board.areas:   # Mettre en fonction
                    if game.board.areas.get(area)[0][0] <= event.pos[0] <= game.board.areas.get(area)[0][1] and game.board.areas.get(area)[1][0] <= event.pos[1] <= game.board.areas.get(area)[1][1]:   
                        selectedArea = area  # = à un nom de case style a1 a2 etc
                
                if game.selectedBox.isPossibleMove(selectedArea) == True:
                    game.moving(selectedArea)
                    print("Au tour des", game.turn)
                else:
                    print(game.selectedBox.isPossibleMove(selectedArea))
                    game.selectedBox = False

            else:  # Si aucune pièce n'est sélectionnée

                for area in game.board.areas:
                    if game.board.areas.get(area)[0][0] <= event.pos[0] <= game.board.areas.get(area)[0][1] and game.board.areas.get(area)[1][0] <= event.pos[1] <= game.board.areas.get(area)[1][1]:   
                        selectedArea = area

                try:
                    for piece in game.all_Pieces:
                        if piece.position == selectedArea and piece.team == game.turn:
                            game.selectedBox = piece
                            game.possibleMoves = game.selectedBox.possibleMoves()
                        elif piece.position == selectedArea and piece.team != game.turn:
                            print("C'est au tour des", game.turn)
                except NameError:
                    selectedArea = False

