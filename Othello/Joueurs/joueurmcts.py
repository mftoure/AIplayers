#!/usr/bin/env python
# -*- coding: utf-8 -*-


import entrainementmcts

import sys
import pickle


sys.path.append("../..")
import game
import math
import random





# chargement du modèle
with open('modeleOthello','rb') as f:
	modele = pickle.load(f)






def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    
    global moi
    moi = game.getJoueur(jeu)
    global adv
    adv = moi%2 + 1
    


    return recherche(modele,jeu)






# parcous de l'arbe pour trouver le noeud dont state = jeu
def recherche(modele,jeu):
	
	
	
	modelen=modele
	

	for child in modelen.children:

		if child.state == jeu:
			
			return meill_state(child)
			
		else:
			
			if len(child.children)!=0:
				return recherche(child,jeu)

			else:
				pass

		
		








# retourne le meilleur etat parmi les noeuds fils 
def meill_state(etat):

	print("aaaaaaaaa")


	meill_state=None
	
	for el in etat.children:
		
		N= float('-inf')
		if N < el.n:
			N=el.n
			meill_state = el.state

	
	return meill_coup(meill_state,etat)




# retourne le coup correspondant
def meill_coup(meill_state,etat):
	
	for cp in game.getCoupsValides(etat.state):
		copie =game.getCopieJeu(etat.state)
		game.joueCoup(copie,cp)
		if (copie == meill_state):
			return cp

		

	



