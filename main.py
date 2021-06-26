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

    game.update(screen)
    
    pygame.display.flip() 

    for event in pygame.event.get():            # tous les évènements du joueur 

        if event.type == pygame.KEYDOWN:        # si le joueur utilise une touche du clavier
            print("oui")

        elif event.type == pygame.QUIT:         # si le joueur veut quitter
            running = False
            pygame.quit()
            quit()