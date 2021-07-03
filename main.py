from game import Game
import pygame
from Pieces.piece import Piece

pygame.init()
game = Game()


pygame.display.set_caption('Bevilacqua Warren Chess Game')
screen = pygame.display.set_mode((1080, 720))

BLACK = pygame.Color(0,0,0)

running = True

while running: 
    
    screen.fill(BLACK)         # on injecte l'image sur l'écran  

    game.update(screen)
    
    pygame.display.flip() 

    for event in pygame.event.get(): 

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()


        elif event.type == pygame.MOUSEBUTTONUP:
            if isinstance(game.selectedBox, Piece):

                for area in game.board.areas:   # Mettre en fonction
                    if game.board.areas.get(area)[0][0] <= event.pos[0] <= game.board.areas.get(area)[0][1] and game.board.areas.get(area)[1][0] <= event.pos[1] <= game.board.areas.get(area)[1][1]:   
                        selectedArea = area  # = à un nom de case style a1 a2 etc
                
                if game.selectedBox.isPossibleMove(selectedArea) == True:
                    game.selectedBox.position = selectedArea
                    game.selectedBox = False 
                    print("Au tour des", game.turn)
                else:
                    print(game.selectedBox.isPossibleMove(selectedArea))
                    game.selectedBox = False

            else:
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

