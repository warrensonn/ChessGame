from game import Game
import pygame

pygame.init()
game = Game()

# on charge les images de fond
background = pygame.image.load('assets/blackBox.png')


pygame.display.set_caption('Chess game')
screen = pygame.display.set_mode((1080, 720))

running = True

while running: 
    
    screen.blit(background, (0, 0))          # on injecte l'image sur l'écran  
    # screen.blit(game.piece.image, (140, 50)) 

    game.update(screen)
    
    pygame.display.flip() 

    for event in pygame.event.get():            # tous les évènements du joueur 

        if event.type == pygame.KEYDOWN:        # si le joueur utilise une touche du clavier
            print("oui")

        elif event.type == pygame.QUIT:         # si le joueur veut quitter
            running = False
            pygame.quit()
            quit()


        # def principale():<br>    
        # stop = False<br>    
        # while not stop:<br>        
        # for event in pygame.event.get():<br>            
        # if event.type ==pygame.QUIT:<br>                
        # stop = True       <br><br>            
        # elif event.type == MOUSEBUTTONUP: # quand je relache le bouton<br>                if event.button == 1: # 1= clique gauche<br>                    if 100<event.pos[0]<200: # création d'un carré 100x100<br>                        
        # if 100<event.pos[1]<200:<br>                            
        # print("hello")

#         clickable_area = pygame.Rect((100, 100), (100, 100))
# rect_surf = pygame.Surface(clickable_area.size)
# rect_surf.fill(COLORS[color_index])
 
# while not stop:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             stop = True
         
#         elif event.type == MOUSEBUTTONUP: # quand je relache le bouton
#             if event.button == 1: # 1= clique gauche
#                 if clickable_area.collidepoint(event.pos):
#                     color_index = (color_index + 1) % 3
#                     rect_surf.fill(COLORS[color_index])
     
#     screen.fill(0) # On efface tout l'écran
#     screen.blit(rect_surf, clickable_area)