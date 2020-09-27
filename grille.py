# On importe pygame et sys
import pygame, sys
# On importe les constantes pygame
from pygame.locals import *
# On importe notre programme 'Cellule.py'
from Cellule import *
# On importe les parametres de notre projet
from parametres import *


class Bouton:
    """
    La classe Bouton permet de creer des images cliquables.
    un objet de cette classe prend en parametres :
    -le chemin d'acces a l'image
    -la position de l'image
    """
    def __init__(self, image, position):
        self.image = image
        self.image = pygame.image.load(self.image).convert_alpha() # convert_alpha permet de conserver la transparence
        self.image = pygame.transform.scale(self.image, (HAUTEUR_BARRE, HAUTEUR_BARRE))# on change la taille de l'image
        # pour la hauteur de la barre d'options
        self.position = position
        self.rectangle = Rect(self.position + self.image.get_size()) #on cree un rectangle qui correcpond a la zone cliquable

class Texte:
    """
    La classe Texte permet de creer des textes.
    Un objet de cette classe prend en parametres:
    -la police de caractere (font)
    -le message (chaine de caracteres)
    - la couleur du texte
    -la position du texte
    """
    def __init__(self, font, message, couleur, position):
        self.font = font
        self.message = str(message)
        self.couleur = couleur
        self.position = position
        self.texte = self.font.render(self.message, True, couleur)

class Barre:
    """
    La classe Barre permet de creer et d'afficher une barre d'options sur la fenetre.
    L'objet Barre prend uniquement la surface (la fenetre) comme parametre
    """
    def __init__(self, fenetre):
        """
        On cree plusieurs objets de la classe Bouton
        """
        self.fenetre = fenetre
        self.retour = Bouton("images/retour.png", (0, 0))
        self.croix = Bouton("images/croix.png", (LARGEUR - HAUTEUR_BARRE, 0))
        self.lecture = Bouton("images/lecture.png", (LARGEUR // 2, 0))
        self.pause = Bouton("images/pause.png", (LARGEUR // 2, 0))
        self.suivant = Bouton("images/suivant.png", (LARGEUR // 2 + HAUTEUR_BARRE, 0))
        self.poubelle = Bouton("images/poubelle.png", (LARGEUR - LARGEUR // 4, 0))
        self.exemple = Bouton("images/exemple2.png", (LARGEUR - LARGEUR // 3, 0))
        self.reset = Bouton("images/reset.png", (LARGEUR // 10 - HAUTEUR_BARRE, 0))

    def afficher(self, stop, generation):
        """
        Cette fonction permet d'afficher et de modfier le contenu de la barre d'options.
        Pour creer cette barre d'options, on dessine un rectangle gris qui prend toute la largeur de la fenetre
        et une certaine hauteur definie dans le fichier 'parametres.py' dans PARAMETRES DE LA GRILLE >> HAUTEUR_BARRE.
        Cette fonction affiche par dessus le rectangle gris les boutons crees precedemment ainsi que le nombre
        de generation. Elle permet egalement de remplacer le bouton 'lecture' par 'pause' et inversement.
        """
        pygame.draw.rect(self.fenetre, COULEUR_BARRE, [0, 0, LARGEUR, HAUTEUR_BARRE]) # On dessine le rectangle
        self.fenetre.blit(self.retour.image, self.retour.position) # on affiche le bouton 'retour'...
        self.fenetre.blit(self.croix.image, self.croix.position) #
        if stop == False:
            self.fenetre.blit(self.pause.image, self.pause.position)
        elif stop == True:
            self.fenetre.blit(self.lecture.image, self.lecture.position)
        self.fenetre.blit(self.suivant.image, self.suivant.position)
        self.fenetre.blit(self.poubelle.image, self.poubelle.position)
        self.fenetre.blit(self.exemple.image, self.exemple.position)
        self.fenetre.blit(self.reset.image, self.reset.position)
        generationTexte = Texte(fontSubTitle, "Generation : " + str(generation), COULEUR_GENERATION, (LARGEUR // 10, 0))
        self.fenetre.blit(generationTexte.texte, generationTexte.position)



class Grille:
    """
    La classe Grille permet d'afficher et de mettre a jour l'ensemble de la fenetre.
    Elle cree la grille de depart (vide) et permet :
    -d'afficher la grille
    -de passer a la generation suivante
    -de remettre a 0 le nombre de generation
    -d'effacer la grille
    -d'afficher la figure d'exemple
    Son seul parametre est la surface (fenetre)
    """
    def __init__(self, fenetre):
        """
        On recouvre la fenetre avec la couleur : COULEUR_FOND_GRILLE qui est aussi la couleur des marges entre chaque
        cellule.
        On initialise la grille (on la remplie de cellules mortes)
        On cree un objet Barre
        """
        self.fenetre = fenetre
        self.fenetre.fill(COULEUR_FOND_GRILLE)
        self.grille = self.initialiserGrille()
        self.generation = 0
        self.stop = True
        self.barre = Barre(self.fenetre)

    def initialiserGrille(self):
        """
        Cette fonction remplie la grille de cellules mortes.
        Elle renvoie la grille une fois remplie
        """
        grille = []
        for ligne in range(NB_LIGNES):
            grille.append([])
            for colonne in range(NB_COLONNES):
                if ligne * (HAUTEUR_CELLULE + MARGE_CELLULE) >= HAUTEUR_BARRE:# pour chaque cellule si elle est
                    # en dessous de la barre d'options
                    nouvelle_cellule = Cellule(ligne, colonne, 0) # On cree un nouvel objet de notre classe 'Cellule'
                    grille[ligne].append(nouvelle_cellule) # On l'ajoute dans notre grille
                    nouvelle_cellule.afficher(self.fenetre) # et on l'affiche
        return grille

    def afficher(self):
        """
        Cette fonction permet de relier les actions de l'utilisateur avec des modifications sur la fenetre.

        """
        clock = pygame.time.Clock()

        # Important : la ligne qui suit cree un evenement USEREVENT toutes les TEMPS_ENTRE_GENERATION millisecondes !
        # C'est cette ligne qui permet de passer a la nouvelle generation de cellules toutes les TEMPS_ENTRE_GENERATION
        # milisecondes
        pygame.time.set_timer(USEREVENT, TEMPS_ENTRE_GENERATION)

        # On cree une boule infinie car on attend une action de l'utilisateur.
        while True:
            self.barre.afficher(self.stop, self.generation)# on affiche la barre d'options
            mouse = pygame.mouse.get_pos() # On recupere la position du curseur de la souris (absisse, ordonnee)
            sourisX = mouse[0]
            sourisY = mouse[1]
            for event in pygame.event.get(): # On etudie les evenements (les actions) qui se produisent
                if event.type == QUIT: # Si l'utilisateur ferme la fenetre
                    sys.exit(0) # on quitte le programme
                elif event.type == MOUSEBUTTONDOWN: # Si l'action est faite sur la souris
                    if sourisY > HAUTEUR_BARRE + HAUTEUR_CELLULE: # et si cette action est realisee lorsque le curseur
                        # de la souris n'est pas sur la barre d'options (donc sur une cellule)
                        colonne = sourisX // (LARGEUR_CELLULE + MARGE_CELLULE) # on recupere la colonne de la cellule
                        ligne = sourisY // (HAUTEUR_CELLULE + MARGE_CELLULE) # on recupere la ligne de la cellule


                        """ LES EVENEMENT LIES A LA SOURIS :
                        event.button = 1 : clic gauche
                        event.button = 2 : clic molette ou clic gauche + clic droit
                        event.button = 3 : clic droit
                        event.button = 4 : molette vers le haut
                        event.button = 5 : molette vers le bas"""
                        if event.button == 1 or event.button == 4: # donc si l'utilisateur a fait clic gauche ou scroll up
                            if self.grille[ligne][colonne].statut == 0: # et si la cellule est morte
                                self.grille[ligne][colonne].statut = 1 # la cellule devient vivante
                        elif event.button == 3 or event.button == 5: # sinon si l'utilisateur fait clic droit ou scroll down
                            if self.grille[ligne][colonne].statut == 1: # et si la cellule est vivante
                                self.grille[ligne][colonne].statut = 0 # la cellule meurt
                        self.grille[ligne][colonne].afficher(self.fenetre) # On affiche la cellule sur laquelle on a
                        # realise une action pour appliquer les modifications

                    elif event.button == 1: # Si on fait clic gauche
                        if self.barre.croix.rectangle.collidepoint(mouse): # et si le curseur de la souris survole le
                            # bouton 'croix'
                            sys.exit(0) # on quitte le programme
                        elif self.barre.retour.rectangle.collidepoint(mouse): # sinon si le curseur survole le bouton
                            # 'retour'
                            import main # on importe notre programme qui affiche la page d'accueil
                            main.afficher_accueil() # et on execute sa fonction 'afficher_accueil'
                        elif self.barre.poubelle.rectangle.collidepoint(mouse): # sinon si le curseur survole la poubelle
                            self.effacer() # on efface la grille
                        elif self.barre.exemple.rectangle.collidepoint(mouse): # sinon si la curseur survole le bouton
                            # 'Exemple'
                            self.afficher_exemple() # on affiche l'exemple
                        elif self.barre.reset.rectangle.collidepoint(mouse): # sinon si le curseur survole le bouton
                            # 'remettre a 0'
                            self.remettre_a_0() # on remet le nombre de generations a 0

                play = False # Par defaut, on ne passe pas a la generation suivante
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and self.barre.suivant.rectangle.collidepoint(mouse):
                    # si on fait clic gauche et que le curseur est sur le bouton 'suivant'
                    play = not play # On inverse la valeur de 'play' qui devient 'True'
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and self.barre.lecture.rectangle.collidepoint(mouse):
                    # si on fait clic gauche et que le curseur survole le bouton 'lecture' (ou le bouton 'pause' car ils
                    # ont le meme rectangle)
                    self.stop = not self.stop # on inverse la valeur de 'self.stop'

                if play or event.type == USEREVENT and not self.stop:
                    # Si on detecte un evenement USEREVENT (il y en a toutes les TEMPS_ENTRE_GENERATION millisecondes)
                    # OU si self.stop == False
                    self.generation_suivante() # On peut passer a la generation suivante
                    # Important : la condition precedente permet de n'avancer que d'une generation si on clique sur
                    # 'suivant' ou d'avancer d'une generation toutes les TEMPS_ENTRE_GENERATION milisecondes si on clique
                    # sur 'lecture'.

            clock.tick(IPS) # On fixe le nombre d'images par secondes a la valeur de IPS dans 'parametres.py'
            pygame.display.flip() # On met a jour la fenetre

    def generation_suivante(self):
        """
        Cette fonction permet de passer a la generation suivante.
        Elle commence par compter le nombre de voisines de chaque cellule.
        Une fois que cela est fait, la fonction fait evoluer les cellules et les affiche
        Elle incremente egalement le nombre de generation de 1 a chaque fois qu'elle est appelee
        """
        self.generation += 1
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if ligne * (HAUTEUR_CELLULE + MARGE_CELLULE) >= HAUTEUR_BARRE: # pour chaque cellule si elle est
                    # en dessous de la barre d'options


                    try:
                        # La ligne de code qui suit peut generer une IndexError s'il s'agit d'une cellule collee a une
                        # bordure de la fenetre
                        # Cette erreur n'est pas derangeante c'est pourquoi on peut placer la ligen qui suit dans un
                        # bloc try/except et ainsi atteindre la suite du programme
                        self.grille[ligne][colonne].compterVoisines(self.grille)
                    except IndexError: # si il y a une IndexError
                        pass # On passe, on ne fait rien

        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if ligne * (HAUTEUR_CELLULE + MARGE_CELLULE) >= HAUTEUR_BARRE:# pour chaque cellule si elle est
                    # en dessous de la barre d'options
                    if self.grille[ligne][colonne].evoluer(self.grille): # si la fonction 'evoluer' retourne 'True'
                        # cela veut dire que la cellule doit changer de statut et qu'il faut donc l'afficher
                        # pour la mettre a jour
                        self.grille[ligne][colonne].afficher(self.fenetre) # on met a jour la cellule qui doit changer
                        # de statut (morte -> vivante ou vivante -> morte)
        self.barre.afficher(self.stop, self.generation) # On affiche ensuite la barre d'options en passant comme
        # argument la valeur de 'self.stop' pour afficher le bouton 'lecture' ou le bouton 'pause' et le nombre de generation
        # pour l'afficher.

    def remettre_a_0(self):
        """
        Cette fonction remet simplement la valeur de 'self.generation' a 0.
        """
        self.generation = 0

    def effacer(self):
        """
        Cette fonction permet d'effacer la grille, c'est-a-dire de remplacer toutes les cellules vivantes
        par des cellules mortes. Elle remet egalement le nombre de generations a 0.
        """
        if not self.stop:
            self.stop = not self.stop
        self.remettre_a_0() # On remet le nombre de generations a 0
        for ligne in range(NB_LIGNES):
            for colonne in range(NB_COLONNES):
                if ligne * (HAUTEUR_CELLULE + MARGE_CELLULE) >= HAUTEUR_BARRE: # # pour chaque cellule si elle est
                    # en dessous de la barre d'options
                    if self.grille[ligne][colonne].statut == 1: # si elle est vivante
                        self.grille[ligne][colonne].statut = 0 # alors elle meurt
                        self.grille[ligne][colonne].afficher(self.fenetre) # et on met a jour la cellule en l'affichant

    def afficher_exemple(self):
        """
        Cette fonction efface la grille et affiche un exemple de figure de depart au milieu de la grille.
        On affiche la figure colonne par colonne.
        ! LES VALEURS SONT CALCULEES EN FONCTION DE LA CELLULE DU MILIEU DE LA GRILLE !
        Exemple : la colonne -5 = 5 colonne AVANT la colonne de la  cellule du milieu

        La largeur de la figure est de 10 cellules, on commence donc 5 cellules avant la cellule du milieu de
        la grille et on finit 4 cellules apres la cellules du milieu de la grille.
        Les colonnes (5, 4) , (-4, -3, 2, 3) et (-2, 1) sont les memes. La hauteur maximale d'une colonne est de 18
        cellules.
        Pour les colonnes 5 et 4:
        Pour les colonnes -4, -3, 2, 3: on affiche uniquement la -8eme et la 9eme cellule
        Pour les colonnes -2 et 1 : on affiche les 18 cellules
        """
        self.effacer() # On efface la grille
        ligne_milieu = NB_LIGNES // 2 # on recupere la ligne de la cellule du milieu
        colonne_milieu = NB_COLONNES // 2 # on recupere la colonne de la cellule du milieu

        for colonne in range(-5, 5): # pour les colonnes entre -5 et 4 (5 exclu)
            if colonne == -5 or colonne == 4: # si la colonne == -5 ou 4
                for ligne in range(-8, 10): # pour les lignes entre -8 et 9 (10 exclu)
                    if ligne != -8 and ligne != 9: # si la ligne est differente de -8 et 9
                        self.grille[ligne_milieu + ligne][colonne_milieu + colonne].statut = 1 # la celulle devient vivante
                        self.grille[ligne_milieu + ligne][colonne_milieu + colonne].afficher(self.fenetre) # on l'affiche
            elif colonne == -4 or colonne == -3 or colonne == 2 or colonne == 3: # Pareil pour le reste
                for ligne in range(-8, 10): # 10 est exclu
                    if ligne == -8 or ligne == 9:
                        self.grille[ligne_milieu + ligne][colonne_milieu + colonne].statut = 1
                        self.grille[ligne_milieu + ligne][colonne_milieu + colonne].afficher(self.fenetre)
            elif colonne == -2 or colonne == 1:
                for ligne in range(-8, 10): # 10 est exclu
                    self.grille[ligne_milieu + ligne][colonne_milieu + colonne].statut = 1
                    self.grille[ligne_milieu + ligne][colonne_milieu + colonne].afficher(self.fenetre)