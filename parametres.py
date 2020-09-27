import pygame
pygame.init()

# -- PARAMETRES DE LA FENETRE --
IPS = 60 # On definit le nombre d'images par seconde
LARGEUR = 1280
HAUTEUR = 720
PLEIN_ECRAN = False # Si True il faut mettre les dimensions de l'écran dans LARGEUR et HAUTEUR

# -- COULEURS --
BLANC = (255, 255, 255)
VERT_CLAIR = (0, 255, 0)
VERT = (0, 200, 0)
ROUGE_CLAIR = (255, 0, 0)
ROUGE = (200, 0, 0)
BLEU = (0, 0, 255)
NOIR = (0, 0, 0)
GRIS = (169, 169, 169)
GRIS_FONCE = (60, 63, 65)
JAUNE = (255, 255, 0)


# -- POLICES DE CARACTERES (FONTS) --
fontTitle = pygame.font.SysFont("Arial", (LARGEUR + HAUTEUR) * 120 // 3000) # police de 120 sur 1920x1080
fontSubTitle = pygame.font.SysFont("Arial", (LARGEUR + HAUTEUR) * 50 // 3000) # police de 50 sur 1920x1080
fontBig = pygame.font.SysFont("Arial", (LARGEUR + HAUTEUR) * 100 // 3000) # police de 100 sur 1920x1080
BigPixelFont = pygame.font.Font("fonts/joystixmonospace.ttf", (LARGEUR + HAUTEUR) * 100 // 3000)
MediumPixelFont = pygame.font.Font("fonts/joystixmonospace.ttf", (LARGEUR + HAUTEUR) * 40 // 3000)
SmallPixelFont = pygame.font.Font("fonts/joystixmonospace.ttf", (LARGEUR + HAUTEUR) * 30 // 3000)

# -- PARAMETRES DE LA PAGE D'ACCUEIL --
LARGEUR_RECT = LARGEUR // 5
HAUTEUR_RECT = HAUTEUR // 5
# La distance qui separe le rectangle 'Jouer' du bord gauche de la fenetre est egale a 1/5 de la largeur de la fenetre
POSX_RECT_JOUER = LARGEUR // 5
# La distance qui separe le rectangle 'Jouer' du haut de la fenetre est egale a 2/3 de la hauteur de la fenetre
POSY_RECT_JOUER = (HAUTEUR // 3) * 2
# La distance qui separe le rectangle 'Quitter' du bord gauche de la fenetre est egale a 3/5 de la largeur de la fenetre
POSX_RECT_QUIT = LARGEUR - (LARGEUR // 5) * 2
# La distance qui separe le rectangle 'Quitter' du haut de la fenetre est egale a 2/3 de la hauteur de la fenetre
POSY_RECT_QUIT = HAUTEUR - HAUTEUR // 3
ECART_INTER_LIGNE = HAUTEUR // 8 # L'ecart entre deux lignes est egale a 1/15 de la hauteur de la fenetre
COULEUR_FOND_ACCUEIL = GRIS_FONCE # On definit la couleur du fond de cette fenetre
COULEUR_TITRE = ROUGE_CLAIR
COULEUR_AUTEUR = BLANC


# -- PARAMETRES DE LA GRILLE --
LARGEUR_CELLULE = 7
HAUTEUR_CELLULE = 7
MARGE_CELLULE = 1
NB_LIGNES = (HAUTEUR // (HAUTEUR_CELLULE + MARGE_CELLULE))
NB_COLONNES = LARGEUR // (LARGEUR_CELLULE + MARGE_CELLULE)
HAUTEUR_BARRE = HAUTEUR // 20 # HAUTEUR_BARRE correspond a la hauteur de la barre d'option en haut de l'ecran
COULEUR_FOND_GRILLE = NOIR # La couleur du fond peut etre assimiler a celle des marges
COULEUR_BARRE = GRIS # La couleur de la barre d'option
COULEUR_GENERATION = NOIR # La couleur du texte qui affiche le nombre de generation
TEMPS_ENTRE_GENERATION = 200 # en millisecondes


# -- PARAMETRES DES CELLULES --
COULEUR_MORTE = GRIS_FONCE
COULEUR_VIVANTE = BLANC
COULEUR_CELLULE_MILIEU = JAUNE