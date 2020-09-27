# On importe pygame et sys
import pygame
# On importe les constantes pygame
from pygame.locals import *
# On importe les parametres de notre projet
from parametres import *

class Cellule:
    """
    On cree une classe cellule qui prend comme argument :
    -la ligne de la cellule dans la grille
    -la colonne de la cellule dans la grille
    -le statut de la cellule (vivante (1) ou morte (0))
    """
    def __init__(self, ligne, colonne, statut):
        self.ligne = ligne
        self.colonne = colonne
        self.statut = statut
        # Au lancement du programme, toutes les cellules sont mortes donc il n'y a pas de voisines
        self.nbVoisines = 0

    def afficher(self, fenetre):
        """
        Cette fonction nous permet d'afficher un rectangle qui correspond a la cellule
        """
        # Si elle est morte (0), la couleur de la cellule sera celle des cellules mortes
        if self.statut == 0:
            self.couleur = COULEUR_MORTE
        # Si elle est vivante (1), la couleur de la cellule sera celle des cellules vivantes
        else:
            self.couleur = COULEUR_VIVANTE
        # On dessine le rectangle sur la fenetre
        # Les arguments sont : (surface, couleur, [positionX, positionY, largeur de la cellule, hauteur de la cellule])
        pygame.draw.rect(fenetre, self.couleur, [(MARGE_CELLULE + LARGEUR_CELLULE) * self.colonne + MARGE_CELLULE,
                                          (MARGE_CELLULE + HAUTEUR_CELLULE) * self.ligne + MARGE_CELLULE,
                                          LARGEUR_CELLULE, HAUTEUR_CELLULE])

    def compterVoisines(self, grille):
        """
        Cette fonction permet de compter le nombre de voisines d'une cellule
        """
        # On declare quelques variables afin de ne pas avoir a ecrire le 'self.' a chaque fois
        # que l'on souhaite utiliser 'self.colonne' ou 'self.ligne' puisqu'on ne les modifie pas
        colonne = self.colonne
        ligne = self.ligne
        self.nbVoisines = 0

        # On verifie si chacune des 8 voisines de la cellule sont vivantes ou morte
        # cellules voisines (O), cellule etudie (X)
        #  V V V
        #  V X V
        #  V V V
        #

        if colonne + 1 < NB_COLONNES:
            if grille[ligne][colonne + 1].statut == 1:
                self.nbVoisines += 1
        if colonne + 1 < NB_COLONNES and ligne + 1 < NB_LIGNES:
            if grille[ligne + 1][colonne + 1].statut == 1:
                self.nbVoisines += 1
        if self.ligne + 1 < NB_LIGNES:
            if grille[ligne + 1][colonne].statut == 1:
                self.nbVoisines += 1
        if 0 <= colonne - 1 and ligne + 1 < NB_LIGNES:
            if grille[ligne + 1][colonne - 1].statut == 1:
                self.nbVoisines += 1
        if 0 <= colonne - 1:
            if grille[ligne][colonne - 1].statut == 1:
                self.nbVoisines += 1
        if 0 <= colonne - 1 and 4 <= ligne - 1:
            if grille[ligne - 1][colonne - 1].statut == 1:
                self.nbVoisines += 1
        if 4 <= ligne - 1:
            if grille[ligne - 1][colonne].statut == 1:
                self.nbVoisines += 1
        if colonne + 1 < NB_COLONNES and 4 <= ligne - 1:
            if grille[ligne - 1][colonne + 1].statut == 1:
                self.nbVoisines += 1

        if self.nbVoisines != 0:
            return self.nbVoisines

    def evoluer(self, grille):
        # On fait evoluer la cellule en fonction de son nombre de voisines

        # On declare quelques variables afin de ne pas avoir a ecrire le 'self.' a chaque fois
        # que l'on souhaite utiliser 'self.colonne', 'self.ligne', 'self.nbVoisines' puisqu'on ne les modifie pas
        colonne = self.colonne
        ligne = self.ligne
        nbVoisines = self.nbVoisines

        # Si la cellule est morte (0) et qu'elle a 3 voisines (qui sont donc vivantes)
        # la cellule devient vivante (1) et on return True pour indiquer qu'il faut modifier
        # cette cellule puisqu'elle a evolue
        if grille[ligne][colonne].statut == 0 and nbVoisines == 3:
            grille[ligne][colonne].statut = 1
            return True

        # Si la cellule est vivante (1) et qu'elle a moins de 2 ou plus de 3 voisines
        # la cellule meurt et on return True pour indiquer qu'il faut modifier cette cellule
        # puisqu'elle a evolue
        elif grille[ligne][colonne].statut == 1:
            if nbVoisines < 2 or nbVoisines > 3:
                grille[ligne][colonne].statut = 0
                return True