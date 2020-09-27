# On importe pygame, sys
import pygame, sys
# On importe les constantes pygame
from pygame.locals import *
# On importe les parametres de notre projet
from parametres import *
# On importe notre programme grille
from grille import *

def afficher_accueil():
    """
    Cette fonction affiche la page d'accueil
    """
    clock = pygame.time.Clock()  # On cree un objet horloge
    if PLEIN_ECRAN: # si PLEIN_ECRAN == True dans le 'parametres.py'
        fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR), FULLSCREEN) # On cree la fenetre avec les dimensions demandees dans
        # le fichier 'parametres.py' en plein ecran
    else: # Sinon on cree la fenetre avec les dimensions demandees dans le fichier 'parametres.py' sans le plein ecran
        fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
    pygame.display.set_caption("Jeu de la Vie par RedBetta") # On met le titre de la fenetre
    fenetre.fill(COULEUR_FOND_ACCUEIL) # On recouvre la fenetre avec la couleur COULEUR_FOND_ACCUEIL

    titre = BigPixelFont.render("Le Jeu de la Vie", True, COULEUR_TITRE)
    auteurs = SmallPixelFont.render("par RedBetta", True, COULEUR_AUTEUR)
    fenetre.blit(titre, ((LARGEUR - titre.get_width()) // 2, (HAUTEUR - titre.get_height()) // 4))
    fenetre.blit(auteurs, ((LARGEUR - auteurs.get_width()) // 2, (HAUTEUR - auteurs.get_height()) // 4 + ECART_INTER_LIGNE))

    texte_Jouer = MediumPixelFont.render("Jouer", True, NOIR)
    texte_Quitter = MediumPixelFont.render("Quitter", True, NOIR)

    while True: # On cree une boucle infinie car on attend une action de l'utilisateur
        rectangle_Jouer = pygame.draw.rect(fenetre, VERT_CLAIR,(POSX_RECT_JOUER, POSY_RECT_JOUER, LARGEUR_RECT, HAUTEUR_RECT))
        # On dessine le rectangle vert clair
        rectangle_quitter = pygame.draw.rect(fenetre, ROUGE_CLAIR,(POSX_RECT_QUIT, POSY_RECT_QUIT, LARGEUR_RECT, HAUTEUR_RECT))
        # On dessine le rectangle rouge clair
        sourisX, sourisY = pygame.mouse.get_pos() # On recupere la position du curseur de la souris

        if rectangle_Jouer.collidepoint(sourisX, sourisY): # Si le curseur survole le rectangle 'Jouer'
            rectangle_Jouer = pygame.draw.rect(fenetre, VERT, (POSX_RECT_JOUER, POSY_RECT_JOUER, LARGEUR_RECT, HAUTEUR_RECT))
            # On affiche le rectangle 'Jouer' en vert pour donner l'impression que le bouton est enfonce
        elif rectangle_quitter.collidepoint(sourisX, sourisY):  # On fait de meme pour le rectangle rouge
            rectangle_quitter = pygame.draw.rect(fenetre, ROUGE, (POSX_RECT_QUIT, POSY_RECT_QUIT, LARGEUR_RECT, HAUTEUR_RECT))

        for event in pygame.event.get(): # On etudie les evenements (actions) realises par l'utilisateur
            if event.type == QUIT: # Si l'utilisateur ferme la fenetre
                sys.exit(0) # On quitte le programme

            elif event.type == MOUSEBUTTONDOWN: # Sinon si l'action est liee a la souris (clic droit, clic gauche,...)
                """ LES EVENEMENT LIES A LA SOURIS :
                event.button = 1 : clic gauche
                event.button = 2 : clic molette ou clic gauche + clic droit
                event.button = 3 : clic droit
                event.button = 4 : molette vers le haut
                event.button = 5 : molette vers le bas"""
                if event.button == 1: # Si c'est un clic gauche
                    if rectangle_Jouer.collidepoint(sourisX, sourisY): # et si le curseur survole le rectangle 'Jouer'
                        grille = Grille(fenetre) # on cree un objet Grille
                        grille.afficher() # Et on appelle la fonction 'afficher' de notre programme 'grille'
                    elif rectangle_quitter.collidepoint(sourisX, sourisY): # Sinon si le curseur survole le rectangle 'Quitter'
                        sys.exit(0) # on quitte le programme

        fenetre.blit(texte_Jouer, (LARGEUR_RECT + (LARGEUR_RECT - texte_Jouer.get_width()) // 2,
                                   HAUTEUR - HAUTEUR // 3 + (HAUTEUR // 5 - texte_Jouer.get_height()) // 2))
        # On affiche le texte 'Jouer' par-dessus (apres) le rectangle 'Jouer'
        fenetre.blit(texte_Quitter, (LARGEUR - (LARGEUR // 5) * 2 + (LARGEUR // 5 - texte_Quitter.get_width()) // 2,
                                     HAUTEUR - HAUTEUR // 3 + (HAUTEUR // 5 - texte_Quitter.get_height()) // 2))
        # On affiche le texte 'Quitter' par-dessus (apres) le rectangle 'Quitter'

        clock.tick(IPS) # On fixe le nombre d'images par secondes a la valeur de IPS dans le fichier 'parametres.py'
        pygame.display.flip() # On met a jour la fenetre

if __name__ == '__main__':
    afficher_accueil()